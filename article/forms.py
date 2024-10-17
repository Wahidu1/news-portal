from django import forms
from .models import Article, Category, Tag


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )
        # Optional: You can customize the widget for the name field
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id':'name',
                'class': 'form-control',
                'placeholder': 'Enter category name',
            }
        ),
        max_length=50
    )

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'image', 'status']
    title = forms.CharField( widget=forms.TextInput( attrs={'id':'title', 'class': 'form-control', 'placeholder': 'Enter article title',}),max_length=100)
    content = forms.CharField( widget=forms.Textarea( attrs={'id':'content', 'class': 'form-control', 'placeholder': 'Enter article content',}),)
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'id': 'category'})
    )

    image = forms.ImageField( widget=forms.FileInput( attrs={'id':'image', 'class': 'form-control'}), required=False)
    status = forms.ChoiceField(
        choices=[('draft', 'Draft'), ('published', 'Published')],
        widget=forms.RadioSelect(attrs={'id': 'status'})
    )

