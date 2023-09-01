from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
   age = models.PositiveIntegerField(null=True, blank=True)
   profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

   
def __str__(self):
   return self.firstname
