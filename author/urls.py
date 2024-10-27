from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'author'

urlpatterns = [
    path('author-add/', login_required(views.author_add), name='author_add'),
    path('author-list/', login_required(views.AuthorListView.as_view()), name='author_list'),
    path('author-edit/<id>/', login_required(views.author_edit), name='author_edit'),
    path('author-delete/<id>/', login_required(views.author_delete), name='author_delete'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.author_profile, name='author_profile'),

    
]