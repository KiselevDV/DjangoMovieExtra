from django.urls import path

from .views import (
    PostListView1, PostListView2, PostDetailView1, PostDetailView2, )

urlpatterns = [
    # path('<int:pk>/', PostDetailView1.as_view(), name='post_detail'),
    path('<int:pk>/', PostDetailView2.as_view(), name='post_detail'),
    # path('', PostListView1.as_view(), name='post_list'),
    path('', PostListView2.as_view(), name='post_list'),
]
