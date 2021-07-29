"""
LoginRequiredMixin или login_required - доступ только, для авторизованных
пользователей;
method_decorator - использовать декораторы в классах;
"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin, )
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.utils.decorators import method_decorator

from .models import Post
from .permissions import AuthorPermissionsMixin, MembersPermissionsMixin


@method_decorator(login_required, name='post')
class PostDetailView1(MembersPermissionsMixin, DetailView):
    """Подробное описание статьи"""
    # LoginRequiredMixin - для зарегистрированных пользователей

    # PermissionRequiredMixin - для пользователей с данными правами
    # Указать приложение 'blog', затем право 'view_post' из permission
    # permission_required = 'blog.view_post'

    # AuthorPermissionsMixin - явлеется ли пользователь автором данной статьи

    # MembersPermissionsMixin - входит ли пользователь в список members

    model = Post

    # Определить метод GET, достать из базового View
    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

    def post(self, request):
        pass


@method_decorator(login_required, name='get')
class PostDetailView2(View):
    """Подробное описание статьи"""

    # @method_decorator(login_required)
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        context = {'post': post}
        return render(request, 'blog/post_detail.html', context)

    def post(self, request):
        pass


@login_required
def func(request):
    pass


class PostListView1(ListView):
    """Список постов"""
    model = Post


class PostListView2(ListView):
    """Список постов. Через кастомный менеджер"""
    # queryset = Post.custom_manager.custom_filter()
    queryset = Post.custom_manager.custom_order_by('-title')
