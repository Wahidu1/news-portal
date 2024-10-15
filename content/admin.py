from django.contrib import admin
from .models import Album, PhotoGallery, VideoGallery, Page, Shortcut

admin.site.register(Album)
admin.site.register(PhotoGallery)
admin.site.register(VideoGallery)
admin.site.register(Page)
admin.site.register(Shortcut)