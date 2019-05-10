from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    netfang = models.EmailField(max_length=50, blank=False)
    nafn = models.CharField(max_length=255)
    eftirnafn = models.CharField(max_length=255)
    simi = models.IntegerField()
    profile_mynd = models.CharField(max_length=9999)
