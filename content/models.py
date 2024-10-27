from django.db import models
from django.utils.text import slugify

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Album(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'album'  # Corrected table name
        managed = True
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

class PhotoGallery(BaseModel):
    title = models.CharField(max_length=255)
    images = models.ImageField(upload_to='photo_galleries/')  # Assuming you want to upload a single cover image
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photo_galleries') 

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'photo_gallery'
        managed = True
        verbose_name = 'Photo Gallery'
        verbose_name_plural = 'Photo Galleries'

class VideoGallery(BaseModel):
    title = models.CharField(max_length=255)
    video_url = models.URLField()  # Link to the video (YouTube, Vimeo, etc.)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'video_gallery'
        managed = True
        verbose_name = 'Video Gallery'
        verbose_name_plural = 'Video Galleries'

class Page(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='pages/', blank=True,  null=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'page'
        managed = True
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'


class Shortcut(BaseModel):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='shortcuts/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shortcut'
        managed = True
        verbose_name = 'Shortcut'
        verbose_name_plural = 'Shortcuts'


