from django.contrib import admin
from .models import Post
from django.contrib.auth.models import User
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ['title']
    fields = ('title', 'text', 'author', 'created_date')
    readonly_fields = ('created_date',)
    # exclude = ('created_date',)

admin.site.register(Post, PostAdmin)
# admin.site.register(User)
