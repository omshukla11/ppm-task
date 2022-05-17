from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.

class UserManager(BaseUserManager):
    def create_superuser(self, email, password=None ,is_active=True, is_staff=True, is_admin=True, **other):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have an password")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        if(is_admin==True):
            user_obj.is_active = True
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_superuser(
            email,
            password=password,
            is_admin=False
        )
        return user
    
    def create_user(self,first_name, last_name, email, password=None):
        user = self.create_superuser(
            email,
            password=password,
            is_admin=False,
            is_staff=False,
            is_active=False
        )
        return user



class User(AbstractBaseUser):

    email     = models.EmailField(max_length=255, unique=True)
    is_staff     = models.BooleanField(default=False)
    is_admin     = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, app_label):
        return True
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
