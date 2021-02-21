from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
# from .validators import *

# Create your models here.
IMAGE_TYPE = (
        ('Type1','Type1'),
        ('Type2','Type2'), 
        ('Type3','Type3'),
        ('Type4','Type4'),
        ('Type5','Type5'),
        ('Type6','Type6'),
        ('Type7','Type7')
        )

class CustomUserManager(BaseUserManager):
    """custom user manager class"""
    use_in_migration = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    """ Custom user model class"""
    email = models.EmailField(_('email'), unique=True, default='')
    name = models.CharField(_('name'), max_length=50, blank=False)
    mobile=models.CharField(max_length=255)
    password = models.CharField(_('password'), max_length=128)
    enable = models.BooleanField(default=False)
    last_login = models.DateTimeField(_('last login'), blank=True,null=True)
    is_superadmin = models.BooleanField(_('is_superadmin'), default=False)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        """stirng representation"""
        return self.email

class OTP_verification(models.Model):
    email = models.OneToOneField(Users,on_delete = models.CASCADE, primary_key = True)
    otp = models.CharField(max_length=10)
    enable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.email.email

class Images(models.Model):
    # user = models.ForeignKey(TravellerProfile,on_delete = models.CASCADE,related_name='User_Blog')
    image_type = models.CharField(verbose_name="Choose Image Type", max_length=30, choices=IMAGE_TYPE)
    image = models.ImageField(verbose_name="Select Image",upload_to='images/') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_type