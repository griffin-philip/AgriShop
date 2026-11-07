from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('FARMER', 'Farmer'),
        ('CUSTOMER', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username