from django.db import models
from .manager import UserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = None # Removes username field so u login with email 
    email = models.EmailField(max_length=256, unique=True)
    
    
    
    objects = UserManager() 
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    pass