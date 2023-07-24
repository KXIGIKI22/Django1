from django.http import JsonResponse
from .models import Purchase

def purchase_list(request):
    purchases = Purchase.objects.all().order_by('-date')
    data = list(purchases.values())
    return JsonResponse(data, safe=False)