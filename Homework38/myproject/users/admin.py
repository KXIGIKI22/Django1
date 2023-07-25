from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age', 'gender', 'phone_number', 'address', 'is_active')

admin.site.register(CustomUser)