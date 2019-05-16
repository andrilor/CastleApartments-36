from django.contrib.auth.models import User
from django.db import models
from eignir.models import Eign
from django.utils import timezone

class Land(models.Model):
    nafn = models.CharField(max_length=255)
    def __str__(self):
        return self.nafn

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullt_nafn = models.CharField(max_length=255)
    kennitala = models.IntegerField()
    heimilisfang = models.CharField(max_length=255)
    borg = models.CharField(max_length=255)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    postnr = models.IntegerField()
    netfang = models.EmailField(max_length=50)
    simi = models.IntegerField()
    mynd = models.CharField(max_length=9999, blank=True)


class leitarsaga(models.Model):
    notandanafn = models.ForeignKey(User, on_delete=models.CASCADE)
    eign = models.ForeignKey(Eign, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(default=timezone.now)