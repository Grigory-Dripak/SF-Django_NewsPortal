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
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='articles_delete'),
]