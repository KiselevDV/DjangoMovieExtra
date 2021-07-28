from django.urls import path

from .views import PostListView, PostDetailView1, PostDetailView2

urlpatterns = [
    path('<int:pk>/', PostDetailView1.as_view(), name='post_detail'),
    # path('<int:pk>/', PostDetailView2.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
]
