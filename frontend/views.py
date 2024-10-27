from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from article.models import  Article, BreakingNews, Category, Comment, Tag
from django.utils import timezone
from datetime import timedelta
from content.models import PhotoGallery, VideoGallery
import re
from article.forms import CommentForm
from author.models import Author
from author.forms import AuthorForm


def extract_youtube_id(url):
    """
    Extract YouTube video ID from a URL.
    Supports formats like:
    - https://www.youtube.com/watch?v=ID
    - https://youtu.be/ID
    """
    youtube_regex = (
        r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    )
    match = re.match(youtube_regex, url)
    if match:
        return match.group(1)
    return None

def index(request):
    context =  {}


    # Get the current time
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    

    context['breaking_news_list'] = BreakingNews.objects.filter(status="published", created_at__gte=time_threshold).order_by('-created_at')[:2]
    context['latest_news_list'] = Article.objects.filter(status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['world_news_list'] = Article.objects.filter(category__name="বিশ্ব" ,status="published", created_at__gte=time_threshold).order_by('-created_at')[:4]
    context['national_news_list'] = Article.objects.filter(category__name="বাংলাদেশ" ,status="published", created_at__gte=time_threshold).order_by('-created_at')[:4]
    
    populer_time_threshold = now - timedelta(hours=480)
    context['popular_news_list'] = Article.objects.filter(status="published", created_at__gte=populer_time_threshold).order_by('-view_count')
    context['sports_news_list'] = Article.objects.filter(category__name="খেলা" ,status="published", created_at__gte=time_threshold).order_by('-created_at')[:5]
    context['opinion_list'] = Article.objects.filter(category__name="মতামত" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    context['photo_gallery_list'] = PhotoGallery.objects.filter(created_at__gte=time_threshold).order_by('-created_at')
    context['entertainment_list'] = Article.objects.filter(category__name="বিনোদন" ,status="published", created_at__gte=time_threshold).order_by('-created_at')[:3]
    video_list= VideoGallery.objects.filter(created_at__gte=time_threshold).order_by('-created_at')[:2]
        # Modify video_list to include only the YouTube video ID
    videos_with_ids = []
    for video in video_list:
        video_id = extract_youtube_id(video.video_url)
        videos_with_ids.append({
            'title': video.title,
            'video_id': video_id
        })
    context['video_list'] = videos_with_ids
    
    
    
    context['business_list'] = Article.objects.filter(category__name="বাণিজ্য" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    
    
    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()

    context['page_title'] = "জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'index'
    context['page_color'] = 'red'
    return render(request, 'frontend/index.html', context)


def world_news(request):
    context = {}
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    context['latest_news_list'] = Article.objects.filter(category__name="বিশ্ব", status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['world_news_list'] = Article.objects.filter(category__name="বিশ্ব" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    context['popular_news_list'] = Article.objects.filter(category__name="বিশ্ব" ,status="published", created_at__gte=time_threshold).order_by('-view_count')
    
    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()
    context['page_title'] = "বিশ্ব | জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'world_news'
    context['page_color'] = 'orange'
    return render(request, 'frontend/world_news.html', context)


def politics_news(request):
    context = {}
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    context['latest_news_list'] = Article.objects.filter(category__name="রাজনীতি", status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['politics_news_list'] = Article.objects.filter(category__name="রাজনীতি" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    context['popular_news_list'] = Article.objects.filter(category__name="রাজনীতি" ,status="published", created_at__gte=time_threshold).order_by('-view_count')
    
    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()
    context['page_title'] = "রাজনীতি | জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'politics_news'
    context['page_color'] = 'blue'
    return render(request, 'frontend/politics_news.html', context)

def sports_news(request):
    context = {}
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    context['latest_news_list'] = Article.objects.filter(category__name="খেলা", status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['sports_news_list'] = Article.objects.filter(category__name="খেলা" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    context['popular_news_list'] = Article.objects.filter(category__name="খেলা" ,status="published", created_at__gte=time_threshold).order_by('-view_count')
    
    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()
    context['page_title'] = "খেলা | জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'sports_news'
    context['page_color'] = 'green'

    return render(request, 'frontend/sports_news.html', context)

def bangladesh_news(request):
    context = {}
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    context['latest_news_list'] = Article.objects.filter(category__name="বাংলাদেশ", status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['bangladesh_news_list'] = Article.objects.filter(category__name="বাংলাদেশ" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    context['popular_news_list'] = Article.objects.filter(category__name="বাংলাদেশ" ,status="published", created_at__gte=time_threshold).order_by('-view_count')
    
    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()
    context['page_title'] = "বাংলাদেশ | জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'bangladesh_news'
    context['page_color'] = 'deep-orange'

    return render(request, 'frontend/bangladesh_news.html', context)

def crime_news(request):
    context = {}
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    context['latest_news_list'] = Article.objects.filter(category__name="অপরাধ", status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['crime_news_list'] = Article.objects.filter(category__name="অপরাধ" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    context['popular_news_list'] = Article.objects.filter(category__name="অপরাধ" ,status="published", created_at__gte=time_threshold).order_by('-view_count')
    
    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()
    context['page_title'] = "অপরাধ | জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'crime_news'
    context['page_color'] = 'purple'

    return render(request, 'frontend/crime_news.html', context)

def entertainment_news(request):
    context = {}
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    context['latest_news_list'] = Article.objects.filter(category__name="বিনোদন", status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['entertainment_news_list'] = Article.objects.filter(category__name="বিনোদন" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    context['popular_news_list'] = Article.objects.filter(category__name="বিনোদন" ,status="published", created_at__gte=time_threshold).order_by('-view_count')
    
    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()
    context['page_title'] = "বিনোদন | জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'entertainment_news'
    context['page_color'] = 'slate'

    return render(request, 'frontend/entertainment_news.html', context)

def business_news(request):
    context = {}
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    context['latest_news_list'] = Article.objects.filter(category__name="বাণিজ্য", status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['business_news_list'] = Article.objects.filter(category__name="বাণিজ্য" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    context['popular_news_list'] = Article.objects.filter(category__name="বাণিজ্য" ,status="published", created_at__gte=time_threshold).order_by('-view_count')
    
    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()
    context['page_title'] = "বাণিজ্য | জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'business_news'
    context['page_color'] = 'turquoise'

    return render(request, 'frontend/business_news.html', context)

def opinion_news(request):
    context = {}
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    context['latest_news_list'] = Article.objects.filter(category__name="মতামত", status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['opinion_news_list'] = Article.objects.filter(category__name="মতামত" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    context['popular_news_list'] = Article.objects.filter(category__name="মতামত" ,status="published", created_at__gte=time_threshold).order_by('-view_count')
    
    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()
    context['page_title'] = "মতামত | জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'opinion_news'
    context['page_color'] = 'marron'

    return render(request, 'frontend/opinion_news.html', context)

def job_news(request):
    context = {}
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    context['latest_news_list'] = Article.objects.filter(category__name="চাকরি", status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['job_news_list'] = Article.objects.filter(category__name="চাকরি" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    context['popular_news_list'] = Article.objects.filter(category__name="চাকরি" ,status="published", created_at__gte=time_threshold).order_by('-view_count')
    
    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()
    context['page_title'] = "চাকরি | জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'job_news'
    context['page_color'] = 'deep-orange'

    return render(request, 'frontend/job_news.html', context)

def lifestyle_news(request):
    context = {}
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    context['latest_news_list'] = Article.objects.filter(category__name="জীবনযাপন", status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['lifestyle_news_list'] = Article.objects.filter(category__name="জীবনযাপন" ,status="published", created_at__gte=time_threshold).order_by('-created_at')
    context['popular_news_list'] = Article.objects.filter(category__name="জীবনযাপন" ,status="published", created_at__gte=time_threshold).order_by('-view_count')

    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()
    context['page_title'] = "জীবনযাপন | জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'lifestyle_news'
    context['page_color'] = 'dark-blue'
    return render(request, 'frontend/lifestyle_news.html', context)

def news_details(request, slug):
    now = timezone.now()
    time_threshold = now - timedelta(hours=360)
    context = {}
    article = Article.objects.get(slug=slug)
    context['article'] = article
    # context['related_news_list'] = Article.objects.filter(category=article.category, status="published").exclude(slug=slug).order_by('-created_at')[:5]
    
    context['breaking_news_list'] = BreakingNews.objects.filter(status="published", created_at__gte=time_threshold).order_by('-created_at')[:2]
    context['latest_news_list'] = Article.objects.filter(status="published", created_at__gte=time_threshold).order_by('-created_at')[:8]
    context['comments']  = Comment.objects.filter(article=article)
    context['categories']  = Category.objects.all()
    context['tags'] =  Tag.objects.all()
    context['page_title'] = article.title + " | জনপদ সংবাদ | সত্যের সন্ধানে, প্রতিদিন"
    context['page_name'] = 'news_details'
    context['page_color'] = 'gold'
    
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            
            return redirect('frontend:news_details', slug=article.slug)  # Redirect to article page
    else:
        form = CommentForm()
    context['form'] = form
    
    return render(request, 'frontend/news_details.html', context)


def news_list_tags(request, id, tag):
    context = {}

    # Filter articles by tag id and ensure they are published
    context['news_list'] = Article.objects.filter(
        tags__id=id, 
        status="published"
    ).order_by('-date_published')
    
    context['tag'] = tag

    context['page_color'] = 'olive'
    
    return render(request, 'frontend/tags_news.html', context)




    
