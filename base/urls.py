from django.urls import path
from . import views
from .views import *

app_name = 'base'

urlpatterns = [
    path('', views.main, name="main"),
    path('projects/', Projects.as_view(), name="projects"),
]