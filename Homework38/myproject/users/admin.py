from django.contrib import admin
from .models import CustomUser, Book, Purchase

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(Purchase)