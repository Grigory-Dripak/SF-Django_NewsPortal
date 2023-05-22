from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from .filters import PostFilter
# from django.http import HttpResponseRedirect


class PostsList(ListView):
    model = Post
    ordering = '-time_creation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostsSearch(ListView):
    model = Post
    ordering = '-time_creation'
    template_name = 'search.html'
    context_object_name = 'posts_search'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post_details'
    pk_url_kwarg = 'id'


class NewsCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    permission_required = ('News.add_post',)
    template_name = 'post_edit.html'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'N'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='News'
        return context


class ArticleCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    permission_required = ('News.add_post',)
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'A'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Article'
        return context


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    permission_required = ('News.change_post',)
    template_name = 'post_edit.html'


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    permission_required = ('News.change_post',)
    template_name = 'post_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    permission_required = ('News.delete_post',)
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    permission_required = ('News.delete_post',)
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
