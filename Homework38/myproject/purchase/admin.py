from django.contrib import admin
from .models import Purchase

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'date']

admin.site.register(Purchase)
