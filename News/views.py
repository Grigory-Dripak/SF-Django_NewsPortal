from django.views.generic import ListView, DetailView
from .models import Post

class PostsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # # Filter
    # queryset = Post.objects.filter(
    #     price__lte=300
    # ).order_by('name')

    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'time_creation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'


class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — poduct.html
    template_name = 'post_details.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post_details'
    pk_url_kwarg = 'id'
