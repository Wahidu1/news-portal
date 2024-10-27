from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'content'
urlpatterns = [
    path('', login_required(views.index), name='index'),
    
    path('photo-gallery/', login_required(views.PhotoGelleryViews.as_view()), name='photo_gallery'),
    path('photo-delete/<id>/', login_required(views.photo_gallery_delete), name='photo_gallery_delete'),
    
    path('video-gallery/', login_required(views.VideoGelleryViews.as_view()), name='video_gallery'),
    path('video-delete/<id>/', login_required(views.video_gallery_delete), name='video_gallery_delete'),
    
    path("pages/", views.CommonPagesViews.as_view(), name="pages"),
    path("shortcut/", views.ShortcutViews.as_view(), name="shortcut")
    
]