from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name  = 'article'

urlpatterns = [
    path('category/', login_required(views.NewsCategoryView.as_view()), name='category'),
    path('category-delete/<id>/', login_required(views.news_category_delete), name='news_category_delete'),
    
    path('add-article/', login_required(views.add_article), name='add_article'),
    path('article-list/', login_required(views.ArticleListView.as_view()), name='article_list'),
    path('article-delete/<id>/', login_required(views.article_delete), name='article_delete'),
    path('article-edit/<id>/', login_required(views.edit_article), name='edit_article'),
    
    path('breaking-news-add/', login_required(views.BreakingNewsCreateView.as_view()), name='breaking_news_add'),
    path('breaking-news-list/', login_required(views.BreakingNewsListView.as_view()), name='breaking_news_list'),
    path('breaking-news-edit/<pk>/', login_required(views.BreakingNewsUpdateView.as_view()), name='breaking_news_update'),
    path('breaking-news-delete/<int:id>/', login_required(views.breaking_news_delete), name='breaking_news_delete'),
    
    path('video-news-add/', login_required(views.add_videos_news), name='add_videos_news'),
    path('video-news-list/', login_required(views.VideoNewsListView.as_view()), name='video_news_list'),
    path('video-news-update/<id>/', login_required(views.edit_videos_news), name='edit_videos_news'),
    path('video-news-delete/<id>/', login_required(views.video_news_delete), name='video_news_delete'),
    
    path('epaper-add/', login_required(views.EpaperCreateView.as_view()), name='epaper_add'),
    path('epaper-list/', login_required(views.EpaperListView.as_view()), name='epaper_list'),
    path('epaper-edit/<pk>/', login_required(views.EpaperUpdateView.as_view()), name='epaper_update'),
    path('epaper-delete/<id>/', login_required(views.epaper_delete), name='epaper_delete'),
]