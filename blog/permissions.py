from django.http import Http404


class AuthorPermissionsMixin:
    """Право доступа для автора (Post.author)"""

    def has_permissions(self):
        """
        Пользователь отправивший запрос 'request.user'
        автор данного поста 'get_object().author'
        """
        return self.get_object().author == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():  # если не автор, то 404
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class MembersPermissionsMixin(AuthorPermissionsMixin):
    """Право для пользователей указанных в members"""

    def has_permissions(self):
        return self.request.user in self.get_object().members.all()
