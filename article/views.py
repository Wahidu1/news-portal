from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView
from .models import Article, Category, Tag
from author.models import Author
from .forms import  CategoryForm, ArticleForm
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


def add_article(request):
    try:
        if request.method == 'POST':
            user = Author.objects.first()
            tag_names = request.POST.getlist('tags')
            article_tags = []
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                article_tags.append(tag)
            
            form = ArticleForm(request.POST, request.FILES)
            
            
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
            form = ArticleForm()

        
        return render(request, 'backend/article/article-add.html', {'form': form,  'tag_names': exists_tag_names})

    except Exception as e:
            messages.error(request, 'An error occurred: ' + str(e))
            return redirect('article:add_article')



    
    


    




