from django.shortcuts import render, redirect
from django.views.generic import CreateView,  UpdateView, DeleteView, ListView, DetailView
from django.contrib import  messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate, login, logout, update_session_auth_hash

from .models import Author
from .forms import AuthorForm

def login_view(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('content:index')
            else:
                messages.error(request, 'Invalid email or password')
    except  KeyError as e:
        messages.error(request, f'Invalid email or password: {e}')

    return render(request, 'backend/author/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('author:login')


def author_profile(request):
    author = request.user
    if author is None:
        messages.error(request, 'Author not found')
        return redirect('author:login')
    
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author, show_category=False)
        if form.is_valid():
            author = form.save()
            update_session_auth_hash(request, author)
            messages.success(request, 'Profile updated successfully')
            return redirect('author:author_profile')
        else:
            messages.error(request, f'Invalid form: {form.errors}')
            return redirect('author:author_profile')
            
    else:
        form = AuthorForm(instance=author, show_category=False)
    return render(request, 'backend/author/author-profile.html', {'form': form})




def author_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save()
            categories = form.cleaned_data['category']
            print(categories)
            author.category.set(categories)
            messages.success(request, 'video_news created successfully')
            return redirect('author:author_add')
    else:
        form = AuthorForm()
        return render(request, 'backend/author/author-add.html', {'form': form})

class AuthorListView(ListView):
    model = Author
    paginate_by = 10
    context_object_name = 'author_list'
    template_name = "backend/author/author-list.html"

    def get_queryset(self):
        # Initialize the queryset
        queryset = super().get_queryset()
        
        # Filter the queryset
        queryset = queryset.filter(is_reader=False)
        return queryset
    

def author_edit(request, id):
    author = Author.objects.get(id=id)
    if author is None:
        messages.error(request, 'Author not found')
        return  redirect('author:author_list')

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES,  instance=author)

        if form.is_valid():
            author = form.save()
            categories = form.cleaned_data['category']
            print(categories)
            author.category.set(categories)
            messages.success(request, 'video_news created successfully')
            return redirect('author:author_edit',  id=id)

    else:
        form = AuthorForm(instance=author)
        return render(request, 'backend/author/author-edit.html', {'form': form})

def author_delete(request, id):
    author = Author.objects.get(id=id)
    if author is None:
        messages.error(request, 'Author not found')
        return  redirect('author:author_list')

    author.delete()
    messages.success(request, 'Author deleted successfully')
    return redirect('author:author_list')
