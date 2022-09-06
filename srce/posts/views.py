from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from posts.models import BlogPost
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
# Create your views here.

class HomeBlog(ListView):
    model = BlogPost
    context_object_name = 'posts'

#effectuer des verification
    def get_queryset(self):
        queryset = super().get_queryset()
        #si l'utilisateur est connecter
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)

@method_decorator(login_required, name='dispatch' )
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'posts/blogpost_create.html'
    fields = ['title', 'content']

class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = 'posts/blogpost_edite.html'
    fields = ['title', 'content', 'published']

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = 'post'

class BlogPostDelete(DeleteView):
    model = BlogPost
    template_name = 'posts/blogpost_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:home')