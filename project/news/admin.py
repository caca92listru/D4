from django.contrib import admin

from .models import Post, Category, Author


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)