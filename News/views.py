from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from .filters import PostFilter
# from django.http import HttpResponseRedirect

class PostsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-time_creation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    paginate_by = 4

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = PostFilter(self.request.GET, queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     return context


class PostsSearch(ListView):
    model = Post
    ordering = '-time_creation'
    template_name = 'search.html'
    context_object_name = 'posts_search'
    paginate_by = 4

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post_details'
    pk_url_kwarg = 'id'


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class ArticleUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
