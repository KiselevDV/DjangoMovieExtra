from django.contrib.auth.models import User
from django.db import models


class MyManager(models.Manager):
    """Кастомный менеджер"""

    # Кастомные методы, аналоги: get, all, filter ...
    def custom_filter(self, **kwargs):
        """custom_filter == filters(published=True)"""
        kwargs['published'] = True
        return super().get_queryset().filter(**kwargs)

    def custom_order_by(self, *args):
        """custom_order_by == order_by(published, ...)"""
        args = ('published',) + args
        return super().get_queryset().order_by(*args)


class Post(models.Model):
    title = models.CharField(verbose_name='Название статьи', max_length=100)
    text = models.TextField(
        verbose_name='Текст', max_length=10000,
        help_text='Длинна статьи не должна превышать 10000 символов')
    author = models.ForeignKey(
        User, verbose_name='Автор', on_delete=models.CASCADE,
        related_name='post')
    members = models.ManyToManyField(
        User, verbose_name='Пользователи с доступом',
        related_name='members', blank=True)
    published = models.BooleanField(verbose_name='Опубликовано', default=False)
    # Привязка стандартного и кастомного менеджеров
    objects = models.Manager()  # пример!!!
    custom_manager = MyManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
