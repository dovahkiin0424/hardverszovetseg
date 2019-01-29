from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from .filters import PostFilter


class PostListView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-kelt']

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["filter"] = PostFilter(self.request.GET, queryset=self.get_queryset())
            return context
        

class UserPostListView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(szerzo=user).order_by('-kelt')

class PostDetailView(DetailView):
    model = Post
    def get_object(self):
        object = super(PostDetailView, self).get_object()
        object.megtekintes += 1
        object.save()
        return object

class PostCreateView(CreateView):
    model = Post
    fields = ['cim', 'intro', 'kep', 'tartalom']

    def form_valid(self, form):
        form.instance.szerzo = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['cim', "intro", 'kep', 'tartalom']

    def form_valid(self, form):
        form.instance.szerzo = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.szerzo:
            return True
        else:
            return False

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.szerzo:
            return True
        else:
            return False

def about(request):
    return render(request, 'blog/about.html')
