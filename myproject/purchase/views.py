from django.http import JsonResponse
from .models import Purchase

def purchases(request):
    purchases = Purchase.objects.all().values()
    return JsonResponse(list(purchases), safe=False)
