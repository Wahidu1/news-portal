from django.contrib import admin
from .models import Category, Tag, Article, BreakingNews, Comment, Like, VideoNews, Epaper

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(BreakingNews)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(VideoNews)
admin.site.register(Epaper)
