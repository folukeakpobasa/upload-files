from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid
# Create your models here.
class User(AbstractBaseUser):
    '''create a custom user model'''
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=8, )
    fullname = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.fullname

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    files = models.ImageField(upload_to="fiels_bank")
    dog = models.DateTimeField()
    
    
    def __str__(self):
        return self.fullname   