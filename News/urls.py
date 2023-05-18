from django.urls import path
from .views import (PostsList,
                    PostDetail,
                    PostsSearch,
                    NewsCreate,
                    ArticleCreate,
                    NewsUpdate,
                    ArticleUpdate,
                    NewsDelete,
                    ArticleDelete
                    )


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:id>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostsSearch.as_view(), name='post_search'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:id>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('<int:id>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('/article/create/', ArticleCreate.as_view(), name='article_create'),
    path('/article/<int:id>/edit/', ArticleUpdate.as_view(), name='article_edit'),
    path('/article/<int:id>/delete/', ArticleDelete.as_view(), name='article_delete'),
]