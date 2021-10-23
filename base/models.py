from django.db import models
from django.contrib.auth.models import User


class Progects(models.Model):
    username = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    text = models.TextField()