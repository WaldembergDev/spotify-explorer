from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, surname, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            first_name = first_name,
            surname = surname,
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, first_name, surname, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(first_name, surname, email, password, **extra_fields)
        

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'surname']

    def __str__(self):
        return self.first_name