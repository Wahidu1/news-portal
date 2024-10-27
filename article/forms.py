from django import forms
from .models import Article, BreakingNews, Category, Epaper, Tag, VideoNews, Comment


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

    title = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'title', 'class': 'form-control', 'placeholder': 'Enter article title'}),
        max_length=100
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'id': 'content', 'class': 'form-control', 'placeholder': 'Enter article content'}),
    )
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.none(),  # Set as none initially
        widget=forms.CheckboxSelectMultiple(attrs={'id': 'category'})
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'id': 'image', 'class': 'form-control'}),
        required=False
    )
    status = forms.ChoiceField(
        choices=[('draft', 'Draft'), ('published', 'Published')],
        widget=forms.RadioSelect(attrs={'id': 'status'})
    )

    def __init__(self, *args, **kwargs):
        author = kwargs.pop('author', None)  # Get the author from the kwargs
        super().__init__(*args, **kwargs)
        if author.is_superuser:
            self.fields['category'].queryset = Category.objects.all()  # If superuser, show
        elif author:
            self.fields['category'].queryset = author.category.all()  # Filter categories based on the author


class BreakingNewsForm(forms.ModelForm):
    class Meta:
        model = BreakingNews
        fields = ['title', 'description', 'status']
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id':'title',
                'class': 'form-control',
                'placeholder': 'Enter breaking news title',
            }
        ),
        max_length=255
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'id':'description',
                'class': 'form-control',
                'placeholder': 'Enter breaking news description',
            }
        ),
    )
    status = forms.ChoiceField(
        choices=[('draft', 'Draft'), ('published', 'Published')],
        widget=forms.RadioSelect(attrs={'id': 'status'})
    )
    
class VideoNewsForm(forms.ModelForm):
    class Meta:
        model = VideoNews
        fields = ['title', 'description', 'video_url', 'categories', 'thumbnail', 'status', 'date_published']
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id':'title',
                'class': 'form-control',
                'placeholder': 'Enter video news title',
            }
        ),
        max_length=255
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'id':'description',
                'class': 'form-control',
                'placeholder': 'Enter video news description',
            }
        ),
    )
    video_url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                'id':'video_url',
                'class': 'form-control',
                'placeholder': 'Enter video URL',
            }
        ),
    )
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'id': 'categories'})
    )
    thumbnail = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'id':'thumbnail',
                'class': 'form-control',
            }
        ),
        required=False
    )
    status = forms.ChoiceField(
        choices=[('draft', 'Draft'), ('published', 'Published')],
        widget=forms.RadioSelect(attrs={'id': 'status'})
    )
    date_published = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'id':'date_published',
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD',
                'type':'date'
            }
        ),
        required=False
    )


class EpaperForm(forms.ModelForm):
    class Meta:
        model = Epaper
        fields = ['title', 'pdf_file', 'date_published', 'page_number', 'status']
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id':'title',
                'class': 'form-control',
                'placeholder': 'Enter epaper title',
            }
        ),
        max_length=255
    )
    pdf_file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'id':'pdf_file',
                'class': 'form-control',
            }
        ),
    )
    date_published = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'id':'date_published',
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD',
                'type':'date'
            }
        ),
        required=False
    )
    page_number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'id':'page_number',
                'class': 'form-control',
                'placeholder': 'Enter page number',
            }
        ),
        required=False
    )
    status = forms.ChoiceField(
        choices=[('draft', 'Draft'), ('published', 'Published')],
        widget=forms.RadioSelect(attrs={'id': 'status'})
    )
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content', 'parent']  # Including 'name' and 'email' fields

        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'comment-name',
                'class': 'form-control',
                'placeholder': 'আপনার নাম লিখুন (ঐচ্ছিক)',
            }),
            'email': forms.EmailInput(attrs={
                'id': 'comment-email',
                'class': 'form-control',
                'placeholder': 'আপনার ইমেল লিখুন (ঐচ্ছিক)',
            }),
            'content': forms.Textarea(attrs={
                'id': 'comment-content',
                'class': 'form-control',
                'placeholder': 'এখানে আপনার মন্তব্য লিখুন...',
                'rows': 4
            }),
            'parent': forms.HiddenInput(),  # Hidden field for handling replies
        }