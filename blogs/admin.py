# blogs/admin.py
from django.contrib import admin
from .models import BlogPost, Category, Like

admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Like)
