from django.contrib import admin
from django.urls import path, include
from .views import UserListView, UserDetailView, CreateUserView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/create/', CreateUserView.as_view(), name='create_user'),
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('books/', include('book.urls')),
    path('purchases/', include('purchase.urls')),
]
