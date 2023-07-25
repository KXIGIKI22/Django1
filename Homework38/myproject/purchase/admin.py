from django.contrib import admin
from .models import CustomUser, Book, Purchase

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'genre', 'published_date']

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'date']

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name']

admin.site.register(Book, BookAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
