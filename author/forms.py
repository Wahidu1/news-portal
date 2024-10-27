from django import forms
from article.models import Category
from .models import Author
from django.core.validators import EmailValidator

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio', 'profile_image', 'password', 'address', 'phone_number', 'category', 'is_active']
    
    name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'name', 'class': 'form-control', 'placeholder': 'Enter your name'}),
        max_length=255
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'placeholder': 'Enter your email'}),
        validators=[EmailValidator()]
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'id': 'bio', 'class': 'form-control', 'placeholder': 'Enter a short bio'}),
        required=False
    )
    profile_image = forms.ImageField(
        widget=forms.FileInput(attrs={'id': 'profile_image', 'class': 'form-control'}),
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control', 'placeholder': 'Enter a password'}),
        max_length=255,
        required=False
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'address', 'class': 'form-control', 'placeholder': 'Enter your address'}),
        required=False
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'phone_number', 'class': 'form-control', 'placeholder': 'Enter phone number'}),
        required=False
    )
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'id': 'category'})
    )
    is_active = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'id': 'is_active', 'class': 'form-check-input'}),
        required=False
    )
    def __init__(self, *args, show_category=True, **kwargs):
        super().__init__(*args, **kwargs)
        if not show_category:
            self.fields.pop('category')
            
    def save(self, commit=True):
        author = super().save(commit=False)
        # যদি ফর্মে password ফিল্ডটি ফাঁকা না থাকে তবে হ্যাশ করুন
        if self.cleaned_data["password"]:
            author.set_password(self.cleaned_data["password"])
        elif author.pk is not None:
            # কোনো পাসওয়ার্ড না থাকলে পূর্বের পাসওয়ার্ড রেখে দিন
            current_password = Author.objects.get(pk=author.pk).password
            author.password = current_password
        
        if commit:
            author.save()
            self.save_m2m()  # মডেল ম্যানি-টু-ম্যানি ফিল্ড সেভ করুন (যেমন category)
        return author
