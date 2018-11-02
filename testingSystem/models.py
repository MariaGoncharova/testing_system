# Create your models here.
from django.db import models
from django.utils import timezone


class User(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)