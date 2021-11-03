from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    text = models.TextField()

class Profile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    username = models.CharField(max_length = 100)
    scores = models.IntegerField()
    