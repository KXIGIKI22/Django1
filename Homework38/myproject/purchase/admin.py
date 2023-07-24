from django.contrib import admin
from .models import CustomUser, Book, Purchase
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'purchase_date', 'price']

admin.site.register(Purchase, PurchaseAdmin)
