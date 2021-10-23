from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import *
from django.views.generic import *

def main(request):
    data = {}
    return render(request, 'base.html', data)

class Projects(TemplateView):
    template_name = 'projects.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    '''
    def dispatch(self, request, *args, **kwargs):
        data = {
                }
        return render(request, self.template_name, data)
'''
class RegisterView(CreateView):
    form_class  = RegisterUserForm
    template_name = 'registration/register.html'
    
    def get_success_url(self):
        return reverse('base:login')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
    
class Login(LoginView):
    form_class  = AuthenticationForm
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        return reverse('base:main')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))