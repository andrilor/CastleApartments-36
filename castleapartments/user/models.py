from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    netfang = models.EmailField(max_length=50, blank=False)
    fullt_nafn = models.CharField(max_length=255)
    heimilisfang = models.CharField(max_length=255)
    simi = models.IntegerField()