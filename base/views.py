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
    def dispatch(self, request, *args, **kwargs):
        data = {
            'projects': Project.objects.all()[::-1],
                }
        return render(request, self.template_name, data)


class Add_project(TemplateView):
    template_name = 'add_project.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data = {
                'form': ProjectsForm,
                }
            if request.method == 'POST':
                form = ProjectsForm(request.POST, request.FILES)
                if form.is_valid():
                    title = form.cleaned_data.get("title")
                    text = form.cleaned_data.get("text")
                    Project.objects.create(text=text, title=title, author_id=request.user.id)
                    a = Profile.objects.get(user_id=request.user.id)
                    a.scores+=10
                    a.save()
                    return redirect('base:projects')
                else:
                    form = ProjectsForm
                    messages.error(request, f'что-то не так')
            else:
                form = ProjectsForm
            data['form'] = form
            return render(request, self.template_name, data)
        else:
            return redirect('exel:login')

def geo(request):
    data = {
        
        }
    return render(request, 'geo.html', data)

def VR(request):
    data = {
        
        }
    return render(request, 'VR.html', data)    

def chemistry(request):
    data = {
        
        }
    return render(request, 'chemistry.html', data)    

def physics(request):
    data = {
        
        }
    return render(request, 'physics.html', data)    

def math(request):
    data = {
        
        }
    return render(request, 'math.html', data)    

def informatics(request):
    data = {
        
        }
    return render(request, 'informatics.html', data) 

def info(request):
    data = {
        
        }
    return render(request, 'info.html', data) 

def profile(request):
    if request.user.is_authenticated:
        data = {
            'profile': Profile.objects.get(user_id=request.user.id),
            'users': Profile.objects.order_by("-scores"),
            }
        return render(request, 'registration/profile.html', data)
    else:
        return redirect('base:login')    

class RegisterView(CreateView):
    form_class  = RegisterUserForm
    template_name = 'registration/register.html'
    
    def get_success_url(self):
        return reverse('base:login')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
    
class Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        return redirect('base:login')
    
def login_user(request):
    uservalue=''
    passwordvalue=''

    form = Loginform(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            try:
                Profile.objects.get(user_id=user.id)
            except ObjectDoesNotExist:
                Profile.objects.create(scores=0, user_id=user.id, username=uservalue)
            return redirect('base:main')
        else:
            context = {'form': form}
            return render(request, 'registration/login.html', context) 
    else:
        context = {'form': form}
        return render(request, 'registration/login.html', context)    
