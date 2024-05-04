from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
    )


# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('User must have email !')
        email=self.normalize_email(email)
        user=self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password):
        user=self.create_user(email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)

    objects=UserProfileManager()

    USERNAME_FIELD="email"

    def __str__(self):
        return self.email


class Contact(models.Model):
    name=models.CharField(max_length=255)
    phoneNumber=models.CharField(max_length=255)
    image=models.CharField(max_length=255)
    image=models.ImageField(upload_to = 'contact_picture',blank=True)
    division=models.CharField(max_length=255)
    added_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
