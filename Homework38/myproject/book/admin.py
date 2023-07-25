from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'genre', 'published_date']

admin.site.register(Book)