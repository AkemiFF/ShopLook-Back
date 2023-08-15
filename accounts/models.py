from django.contrib.auth.models import AbstractUser, Group, Permission, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .manager import CustomUserManager
from django.db import models
import uuid


# class Shopper(AbstractUser):
#     pass

# class Shopper(models.Model):
#     name = models.CharField(max_length=45, blank=False, default="")
#     email = models.CharField(max_length=45, null=True, blank=True)
#     phone_number = models.IntegerField(null=True, blank=True)

def generate_custom_uid():
    uid = uuid.uuid4()
    uid_str = str(uid).replace("-", "")
    return uid_str

class Shopper(AbstractBaseUser, PermissionsMixin):
    # username = None
    # email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=200, null=False, blank=True)
    last_name = models.CharField(max_length=250, blank=True, null=False)
    username = models.CharField(max_length=100, blank=True, null=True)
    
    uid = models.CharField(max_length=32, unique=True, default=generate_custom_uid)
    tel = models.CharField(max_length=20, null=True) #Used for API auth
    country = models.CharField(max_length=100, blank=True, null=False)
    date_of_birth = models.DateField(editable=True)
    create_at = models.DateTimeField("User creation", auto_now_add=True)
    
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
