from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import uuid


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email, username, password):        
        user = self.create_user(            
            email = self.normalize_email(email),            
            username = username,            
            password=password     
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 

class User(AbstractUser):    
    objects = UserManager()
    api_key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)  

    def __str__(self):
        return self.username
