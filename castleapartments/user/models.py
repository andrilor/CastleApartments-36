from django.contrib.auth.models import User
from django.db import models
from eignir.models import Eign

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    netfang = models.EmailField(max_length=50, blank=False)
    fullt_nafn = models.CharField(max_length=255)
    heimilisfang = models.CharField(max_length=255)
    simi = models.IntegerField()
    mynd = models.CharField(max_length=9999, blank=True)


class leitarsaga(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    eign = models.ForeignKey(Eign, on_delete=models.CASCADE)
