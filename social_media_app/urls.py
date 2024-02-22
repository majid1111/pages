
from django.urls import path
from .views import PageListCreateView, PostListCreateView, LikeListCreateView

urlpatterns = [
    path('pages/', PageListCreateView.as_view(), name='page-list-create'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
]
