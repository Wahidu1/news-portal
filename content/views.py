from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib import  messages

from .models import Album, PhotoGallery, VideoGallery, Page, Shortcut
from .forms import PageForm, PhotoGalleryForm, ShortcutForm, VideoGalleryForm
def index(request):
    return render(request,  'backend/base.html', {})


class PhotoGelleryViews(View):
    model_name = PhotoGallery
    form_class  = PhotoGalleryForm
    template_name  = 'backend/content/photo-gallery.html'
    
    def get(self, request):
        photos = self.model_name.objects.all()
        form  = self.form_class()
        context  = {
            'photos': photos,
            'form': form,
            'page_name' : 'category',
            'page_title' : 'Category',
        }
        return render(request, self.template_name, context)
    def post(self, request):
        try:
            album_id  = request.POST.get('album_id')
            if album_id:
                album_name = request.POST.get('album_title')
                try:
                    a = Album(name=album_name)
                    a.save()
                    messages.success(request, 'Album created successfully')
                    return redirect('content:photo_gallery')
                except  Exception as e:
                    messages.error(request, 'Album creation failed')
                    return redirect('content:photo_gallery')
            else:
                form = self.form_class(request.POST,  request.FILES)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Photo gallery created successfully')
                    return redirect('content:photo_gallery')
                else:
                    messages.error(request, 'Photo gallery creation failed')
                    return redirect('content:photo_gallery')

        except Exception as e:
            messages.error(request, 'An error occurred: ' + str(e))
            return redirect('article:category')
        
def  photo_gallery_delete(request, id):
    photo_gallery =  PhotoGallery.objects.get(id=id)
    if photo_gallery is None:
        messages.error(request, 'Photo gallery not found')
        return redirect('content:photo_gallery')
    photo_gallery.delete()
    messages.success(request, 'Photo gallery deleted successfully')
    return redirect('content:photo_gallery')


class VideoGelleryViews(View):
    model_name = VideoGallery
    form_class  = VideoGalleryForm
    template_name  = 'backend/content/video-gallery.html'
    
    def get(self, request):
        videos = self.model_name.objects.all()
        form  = self.form_class()
        context  = {
            'videos': videos,
            'form': form,
            'page_name' : 'category',
            'page_title' : 'Category',
        }
        return render(request, self.template_name, context)
    def post(self, request):
        try:
        
            form = self.form_class(request.POST,  request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Video gallery created successfully')
                return redirect('content:video_gallery')
            else:
                messages.error(request, 'Video gallery creation failed')
                return redirect('content:video_gallery')

        except Exception as e:
            messages.error(request, 'An error occurred: ' + str(e))
            return redirect('article:category')
def  video_gallery_delete(request, id):
    video_gallery =  VideoGallery.objects.get(id=id)
    if video_gallery is None:
        messages.error(request, 'Video gallery not found')
        return redirect('content:video_gallery')
    video_gallery.delete()
    messages.success(request, 'Video gallery deleted successfully')
    return redirect('content:video_gallery')


class CommonPagesViews(View):
    model_name = Page
    form_class = PageForm
    template_name = 'backend/content/common-page.html'

    def get(self, request):
        pages = self.model_name.objects.all()
        page_id = request.GET.get('page_id')
        form = self.form_class()

        if page_id:
            try:
                page = self.model_name.objects.get(id=page_id)
                form = self.form_class(instance=page)
            except self.model_name.DoesNotExist:
                messages.error(request, "Page not found.")

        context = {
            'pages': pages,
            'form': form,
            'page_name': 'page',
            'page_title': 'Pages',
            'page_id': page_id,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        page_id = request.POST.get('page_id')
        if page_id:
            page = get_object_or_404(self.model_name, id=page_id)
            form = self.form_class(request.POST, request.FILES, instance=page)
            success_message = "Page updated successfully"
        else:
            form = self.form_class(request.POST, request.FILES)
            success_message = "Page created successfully"

        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect('content:pages')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors below.')
            pages = self.model_name.objects.all()  # Pass pages again for re-rendering
            context = {
                'pages': pages,
                'form': form,
                'page_name': 'page',
                'page_title': 'Pages',
                'page_id': page_id,
            }
            return render(request, self.template_name, context)



class ShortcutViews(View):
    model_name = Shortcut
    form_class = ShortcutForm
    template_name = 'backend/content/shortcut.html'

    def get(self, request):
        shortcuts = self.model_name.objects.all()
        shortcut_id = request.GET.get('shortcut_id')
        form = self.form_class()

        if shortcut_id:
            try:
                shortcut = self.model_name.objects.get(id=shortcut_id)
                form = self.form_class(instance=shortcut)
            except self.model_name.DoesNotExist:
                messages.error(request, "Shortcut not found.")

        context = {
            'shortcuts': shortcuts,
            'form': form,
            'page_name': 'shortcuts',
            'page_title': 'Shortcuts',
            'shortcut_id': shortcut_id,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        shortcut_id = request.POST.get('shortcut_id')
        if shortcut_id:
            shortcut = get_object_or_404(self.model_name, id=shortcut_id)
            form = self.form_class(request.POST, request.FILES, instance=shortcut)
            success_message = "Shortcut updated successfully"
        else:
            form = self.form_class(request.POST, request.FILES)
            success_message = "Shortcut created successfully"

        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect('content:shortcut')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors below.')
            shortcuts = self.model_name.objects.all()  # Pass pages again for re-rendering
            context = {
                'shortcuts': shortcuts,
                'form': form,
                'page_name': 'shortcuts',
                'page_title': 'Shorcuts',
                'shortcut_id': shortcut_id,
            }
            return render(request, self.template_name, context)
