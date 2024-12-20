from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    phone= models.CharField(max_length = 255,unique=True)
    password = models.CharField(max_length = 255)
    username=None

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
