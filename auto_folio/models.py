from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    role = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
