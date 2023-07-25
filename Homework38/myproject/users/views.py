from django.views.generic import ListView, DetailView
from .models import User
from django.views.generic.edit import CreateView
from .forms import UserForm


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

class CreateUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'create_user.html'
    success_url = '/users/'
