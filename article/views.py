from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import Article, BreakingNews, Category, Epaper, Tag, VideoNews
from author.models import Author
from .forms import  BreakingNewsForm, CategoryForm, ArticleForm, EpaperForm, VideoNewsForm
from django.contrib import messages
from django.utils import timezone

class NewsCategoryView(View):
    model_name = Category
    form_class  = CategoryForm
    template_name  = 'backend/article/category.html'
    
    def get(self, request):
        categories = self.model_name.objects.all()
        form  = self.form_class()
        context  = {
            'categories': categories,
            'form': form,
            'page_name' : 'category',
            'page_title' : 'Category',
        }
        return render(request, self.template_name, context)
    def post(self, request):
        try:
            cat_id  = request.POST.get('category_id')
            if  cat_id:
                category = self.model_name.objects.get(id=cat_id)
                form = self.form_class(request.POST, instance=category)
                if  form.is_valid():
                    form.save()
                    messages.success(request, 'Category updated successfully')
                    return redirect('article:category')
                else:
                    messages.error(request, 'Invalid form data')
                    return redirect('article:category')
                    
            else:
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Category created successfully')
                    return redirect('article:category')
                else:
                    messages.error(request, 'Category creation failed')
                    return redirect('article:category')
        except Exception as e:
            messages.error(request, 'An error occurred: ' + str(e))
            return redirect('article:category')

def news_category_delete(request, id ):
    try:
        category = Category.objects.get(id=id)
        if category is None:
            messages.error(request, 'Category not found')
            return redirect('article:category')
        category.delete()
        messages.success(request, 'Category deleted successfully')
        return  redirect('article:category')
    except Exception as e:
        messages.error(request, 'An error occurred: ' + str(e))
        return redirect('article:category')

def add_article(request):
    try:
        if request.method == 'POST':
            user = request.user
            tag_names = request.POST.getlist('tags')
            article_tags = []
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                article_tags.append(tag)
            
            form = ArticleForm(request.POST, request.FILES, author=request.user)
            
            
            if form.is_valid():
                # Save the article instance
                article = form.save(commit=False)
                article.author = user
                # Save the article
                article.save()
                                # Set the categories
                categories = form.cleaned_data['category']
                article.category.set(categories)
                # Set the tags
                article.tags.set(article_tags)
                                # Set the published_at field if status is 'published'
                if article.status == 'published':
                    article.published_at = timezone.now()
                    article.save()
                messages.success(request, 'Article created successfully')

                return redirect('article:add_article')  # Redirect to a list or detail page after saving
            else:
                messages.error(request, form.errors)
                return render(request, 'backend/article/article-add.html', {'form': form})
        else:
            exists_tag_names = Tag.objects.all()
            form = ArticleForm(author=request.user)

        
        return render(request, 'backend/article/article-add.html', {'form': form,  'tag_names': exists_tag_names})

    except Exception as e:
            messages.error(request, 'An error occurred: ' + str(e))
            return redirect('article:add_article')
        
class ArticleListView(ListView):
    model = Article
    paginate_by = 10
    context_object_name = "news_list"
    template_name = "backend/article/article-list.html"
    
    def get_queryset(self):
        # Get the logged-in author
        author = self.request.user
        if author.is_superuser:
            return Article.objects.all()
        # Check if the user is an author
        if author.is_author:  # Ensure the user has an associated Author instance
            
            # Filter articles based on the author's categories
            return Article.objects.filter(author=author)
        
        return Article.objects.none()  # Return an empty queryset if the user is not an author

def article_delete(request, id):
    try:
        news  = Article.objects.get(id=id)
        if news is None:
            messages.error(request, 'Article not found')
            return redirect('article:article_list')
        news.delete()
        messages.success(request, 'Article deleted successfully')
        return redirect('article:article_list')
    except Exception as e:
        messages.error(request, 'An error occurred: ' + str(e))
        return redirect('article:article_list')
        
def edit_article(request, id):
    try:
        article = get_object_or_404(Article, id=id)
        if  article is None:
            messages.error(request, 'Article not found')
            return redirect('article:article_list')

        if request.method == 'POST':
            tag_names = request.POST.getlist('tags')
            article_tags = []
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                article_tags.append(tag)
            
            form = ArticleForm(request.POST, request.FILES, author=request.user, instance=article)
            
            if form.is_valid():
                # Save the article instance
                article = form.save(commit=False)
                
                # Set the categories
                categories = form.cleaned_data['category']
                article.category.set(categories)
                
                # Set the tags
                article.tags.set(article_tags)
                
                # Set the published_at field if status is 'published'
                if article.status == 'published' and not article.published_at:
                    article.published_at = timezone.now()

                article.save()
                
                messages.success(request, 'Article updated successfully')
                return redirect('article:edit_article', id=id)  # Redirect to the edit page or detail page after saving
            else:
                messages.error(request, form.errors)
        else:
            form = ArticleForm(author=request.user, instance=article)
            exists_tag_names = Tag.objects.all()

        return render(request, 'backend/article/article-edit.html', {'form': form, 'article': article, 'tag_names': exists_tag_names})
    
    except Exception as e:
        messages.error(request, 'An error occurred: ' + str(e))
        return redirect('article:article_list')

class BreakingNewsCreateView(CreateView):
    model = BreakingNews
    form_class =  BreakingNewsForm
    template_name = "backend/article/breaking-news-add.html"
    success_url = reverse_lazy('article:breaking_news_add')


class BreakingNewsListView(ListView):
    model = BreakingNews
    paginate_by = 10
    context_object_name = "breaking_news_list"
    template_name = "backend/article/breaking-news-list.html"

class BreakingNewsUpdateView(UpdateView):
    model = BreakingNews
    form_class =  BreakingNewsForm
    template_name = "backend/article/breaking-news-edit.html"
    
    def get_success_url(self):
        return reverse_lazy('article:breaking_news_update', kwargs={'pk': self.object.pk})

def breaking_news_delete(request, id):
    try:
        news  = BreakingNews.objects.get(id=id)
        if news is None:
            messages.error(request, 'Breaking News not found')
            return redirect('article:breaking_news_list')
        news.delete()
        messages.success(request, 'Breaking News deleted successfully')
        return redirect('article:breaking_news_list')
    except Exception as e:
        messages.error(request, 'An error occurred: ' + str(e))
        return redirect('article:breaking_news_list')
    
def add_videos_news(request):
    try:
        if request.method == 'POST':
            user = Author.objects.first()
            form = VideoNewsForm(request.POST, request.FILES)
            if form.is_valid():
                # Save the article instance
                video_news = form.save(commit=False)
                video_news.author = user
                # Save the video_news
                video_news.save()
                                # Set the categories
                categories = form.cleaned_data['categories']
                
                video_news.categories.set(categories)

                messages.success(request, 'video_news created successfully')

                return redirect('article:add_videos_news')  # Redirect to a list or detail page after saving
            else:
                messages.error(request, form.errors)
                return render(request, 'backend/article/video-news-add.html', {'form': form})
        else:
            
            form = VideoNewsForm()

        
        return render(request, 'backend/article/video-news-add.html', {'form': form})

    except Exception as e:
            messages.error(request, 'An error occurred: ' + str(e))
            return redirect('article:add_videos_news')
   
class VideoNewsListView(ListView):
    model = VideoNews
    paginate_by = 10
    context_object_name = "video_news_list"
    template_name = "backend/article/video-news-list.html"


def edit_videos_news(request, id):
    try:
        video_news = get_object_or_404(VideoNews, id=id)
        if video_news is None:
            messages.error(request, 'Video news not found')
            return redirect("article:video_news_list")
        
        if request.method == 'POST':
            form = VideoNewsForm(request.POST, request.FILES, instance=video_news)
            
            if form.is_valid():
                # Save the video_news instance
                video_news = form.save(commit=False)
                
                # Set the categories
                categories = form.cleaned_data['categories']
                video_news.categories.set(categories)

                video_news.save()
                
                messages.success(request, 'Video News updated successfully')
                return redirect('article:edit_videos_news', id=video_news.id)  # Redirect to the edit page or detail page after saving
            else:
                messages.error(request, form.errors)
        else:
            form = VideoNewsForm(instance=video_news)

        return render(request, 'backend/article/video-news-edit.html', {'form': form, 'video_news': video_news})
    
    except Exception as e:
        messages.error(request, 'An error occurred: ' + str(e))
        return redirect('article:edit_videos_news', id=id)

def video_news_delete(request, id):
    try:
        news  = VideoNews.objects.get(id=id)
        if news is None:
            messages.error(request, 'Video News not found')
            return redirect('article:video_news_list')
        news.delete()
        messages.success(request, 'Video News deleted successfully')
        return redirect('article:video_news_list')
    except Exception as e:
        messages.error(request, 'An error occurred: ' + str(e))
        return redirect('article:video_news_list')
 
class EpaperCreateView(CreateView):
    model = Epaper
    form_class = EpaperForm
    template_name = "backend/article/epaper-add.html"
    success_url = reverse_lazy('article:epaper_add')
    
class EpaperListView(ListView):
    model = Epaper
    paginate_by = 10
    context_object_name = 'epapers'
    template_name = "backend/article/epaper-list.html"

class EpaperUpdateView(UpdateView):
    model = Epaper
    form_class = EpaperForm
    template_name = "backend/article/epaper-edit.html"
    
    def get_success_url(self):
        return reverse_lazy('article:epaper_update', kwargs={'pk': self.object.pk})

def epaper_delete(request, id):
    try:
        epaper = Epaper.objects.get(id=id)
        if epaper is None:
            messages.error(request, 'Epaper not found')
            return redirect('article:epaper_list')
        epaper.delete()
        messages.success(request, 'Epaper deleted successfully')
        return redirect('article:epaper_list')
    except  Exception as e:
        messages.error(request, 'An error occurred: ' + str(e))
        return redirect('article:epaper_list')

        
        


    

