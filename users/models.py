from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = None
    last_name = None
    
    description = models.TextField(null=True, blank=True)
