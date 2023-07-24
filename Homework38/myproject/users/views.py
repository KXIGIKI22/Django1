from django.http import JsonResponse
from .models import User

def user_list(request):
    users = User.objects.all()
    data = list(users.values())
    return JsonResponse(data, safe=False)
