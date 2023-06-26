from django.contrib import admin
from apps.blog.models import Author, Category

# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
