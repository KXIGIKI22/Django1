from django.urls import path, include
from user.views import users
from book.views import books
from purchase.views import purchases

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', users, name='users'),
    path('books/', books, name='books'),
    path('purchases/', purchases, name='purchases'),
]