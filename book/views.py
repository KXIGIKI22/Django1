from django.http import JsonResponse
from .models import Book

def books(request):
    books = Book.objects.all().values()
    return JsonResponse(list(books), safe=False)