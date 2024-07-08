from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_display_links = ('title',)


admin.site.register(News, NewsAdmin)