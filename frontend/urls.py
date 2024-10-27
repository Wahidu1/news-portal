from django.urls import path
from . import views
app_name = 'frontend'

urlpatterns = [
    path('',views.index,  name='index'),
    path('world-news/', views.world_news, name='world_news'),
    path('politics-news/', views.politics_news, name='politics_news'),
    path('sports-news/', views.sports_news, name='sports_news'),
    path('bangladesh-news/', views.bangladesh_news, name='bangladesh_news'),
    path('crime-news/', views.crime_news, name='crime_news'),
    path('entertainment-news/', views.entertainment_news, name='entertainment_news'),
    path('business-news/', views.business_news, name='business_news'),
    path('opinion-news/', views.opinion_news, name='opinion_news'),
    path('job-news/', views.job_news, name='job_news'),
    path('lifestyle-news/', views.lifestyle_news, name='lifestyle_news'),
    
    
    path('news/<slug:slug>/', views.news_details, name='news_details'),
    
    path('news-tag/<int:id>/<tag>/', views.news_list_tags, name='news_list_tags'),
    


]
