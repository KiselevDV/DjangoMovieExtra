from django.contrib.auth.models import User
from django.db import models


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
