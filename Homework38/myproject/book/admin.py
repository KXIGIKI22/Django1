from django.contrib import admin
from .models import CustomUser, Book, Purchase

#class User(models.Model):
#    name = models.CharField(max_length=100)
#    email = models.EmailField(unique=True)
#    age = models.IntegerField()

class Bookdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'genre', 'published_date']

admin.site.register(Book, BookAdmin)
