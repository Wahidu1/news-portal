from django.urls import path
from . import views

app_name  = 'article'


urlpatterns = [
    path('category', views.NewsCategoryView.as_view(), name='category'),
    
    path('add-article', views.add_article, name='add_article'  )

]
