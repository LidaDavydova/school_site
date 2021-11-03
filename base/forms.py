from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.views.generic.edit import FormView

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'text',]

class Loginform(forms.Form):
    username= forms.CharField(max_length= 50,label="Enter username")
    password= forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)

class RegisterUserForm(UserCreationForm):
    
    username = forms.CharField(label='Логин', 
                               widget=forms.TextInput(attrs={'class': 'form-input',
                                                             'style': 'width:180px;height:18px'
                                                             }))
    email = forms.EmailField(label='Email', 
                               widget=forms.EmailInput(attrs={'class': 'form-input',
                                                              'style': 'width:180px;height:18px'
                                                              }))
    password1 = forms.CharField(label='Пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                 'style': 'width:180px;height:18px'
                                                                 }))
    password2 = forms.CharField(label='Повтор пароля', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                 'style': 'width:180px;height:18px'
                                                                 }))
    class Meta:
        model = User
        fields = {'email', 'username', 'password2','password1'}
    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)