from django.db import models
from content.models import BaseModel
from django.utils.text import slugify
from django.urls import reverse

class Category(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)  # Optional slug field

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Ensure tag names are unique

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'
        managed = True
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'



class Article(BaseModel):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE, related_name='articles')
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', related_name='articles')
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # Allow blank slug for auto-generation
    tags = models.ManyToManyField('Tag', related_name='articles')
    image = models.ImageField(upload_to='article_image', blank=True, null=True)  # Optional image
    view_count = models.IntegerField(default=0)  # Optional view count through signals
    published_at = models.DateTimeField(null=True, blank=True)  # New field for actual publish time
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    likes = models.IntegerField(default=0)  # New column for likes
    dislikes = models.IntegerField(default=0)  # New column for dislikes

    class Meta:
        db_table = 'article'
        managed = True
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        indexes = [
            models.Index(fields=['slug']),  # Add index for slug for faster lookups
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate slug from title
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})  # Generate URL based on slug

class BreakingNews(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'breaking_news'
        managed = True
        verbose_name = 'Breaking News'
        verbose_name_plural = 'Breaking News' 

class Comment(BaseModel):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    reader = models.ForeignKey('author.Author', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f'Comment by {self.reader.name} on {self.article.title}'  # Corrected

    class Meta:
        db_table = 'comment'
        managed = True
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    @property
    def is_reply(self):
        """Return True if this comment is a reply to another comment."""
        return self.parent is not None

class Like(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='article_likes')
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE, related_name='likes')
    date_liked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like by {self.author.name} on {self.article.title}'

    class Meta:
        db_table = 'like'
        managed = True
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = ('article', 'author')  # Prevent multiple likes by the same author on the same article
  
class VideoNews(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField()  # Link to the video
    date_published = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='video_news')
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)  # Optional thumbnail field
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE, related_name='videos_news')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'video_news'
        managed = True
        verbose_name = 'Video News'
        verbose_name_plural = 'Video News'


class Epaper(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='epaper_pdf')
    date_published = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='epaper')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'epaper'
        managed = True
        verbose_name = 'Epaper'
        verbose_name_plural = 'Epapers'

