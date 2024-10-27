from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("article/", include("article.urls")),
    path("author/", include("author.urls")),
    path("content/", include("content.urls")),
    path("",  include("frontend.urls")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# # urls.py
# from django.shortcuts import render

# def custom_page_not_found_view(request, exception):
#     return render(request, "frontend/404.html", {})

# handler404 = 'portfolio.urls.custom_page_not_found_view'