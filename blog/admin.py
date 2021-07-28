from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.site_title = 'Свои права доступа в Джанго'
admin.site.site_header = 'Django Permissions'
