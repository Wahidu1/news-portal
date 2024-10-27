from django import forms
from .models import Album, PhotoGallery, VideoGallery, Page, Shortcut

class PhotoGalleryForm(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        fields = ('title', 'images', 'album')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'images': forms.FileInput(attrs={'class': 'form-control'}),
            'album': forms.Select(attrs={'class': 'form-control'})
        }
        
class VideoGalleryForm(forms.ModelForm):
    class Meta:
        model = VideoGallery
        fields = ('title', 'video_url')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control'})
        }
        
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('name', 'description', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
        
class ShortcutForm(forms.ModelForm):
    class Meta:
        model = Shortcut
        fields = ('name', 'title', 'value', 'description', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }