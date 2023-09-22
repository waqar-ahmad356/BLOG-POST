from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_form_create.html'
    form_class = PostForm
    success_url = '/'
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'post_form.html'
    form_class = PostForm
    success_url = '/'

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'comment_form.html'
    form_class = CommentForm
    def form_valid(self, form):
        form.instance.author=self.request.user
        form.instance.post=get_object_or_404(Post,pk=self.kwargs['pk'])
        return super().form_valid(form)
