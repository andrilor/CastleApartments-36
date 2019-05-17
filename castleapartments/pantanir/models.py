from django.db import models
from django.contrib.auth.models import User
from eignir.models import Eign


class Pantanir(models.Model):
    notandanafn = models.ForeignKey(User, on_delete=models.CASCADE)
    heimilisfang = models.CharField(max_length=255)
    baejarfelag = models.CharField(max_length=255)
    postnumer = models.IntegerField()
    verd = models.IntegerField()
    brunabotamat = models.IntegerField()
    fasteignamat = models.IntegerField()
    tegund = models.CharField(max_length=255)
    staerd = models.IntegerField()
    byggingarar = models.DateField()
    fjoldi_herbergja = models.IntegerField()
    fjoldi_badherberga = models.IntegerField()
    fjoldi_svefnherberga = models.IntegerField()
    sett_a_solu = models.DateField()
    nafn_seljanda = models.CharField(max_length=255)
    simi_seljanda = models.IntegerField()
    netfang_seljanda = models.EmailField(max_length=255)
    starfsmenn = models.CharField(max_length=255)
    nafn_kaupanda = models.CharField(max_length=255)
    simi_kaupanda = models.IntegerField()
    netfang_kaupanda = models.EmailField(max_length=255)
    kennitala_kaupanda = models.IntegerField()
    heimilisfang_kaupanda = models.CharField(max_length=255)
    borg_kaupanda = models.CharField(max_length=255)
    land_kaupanda = models.CharField(max_length=255)
    postnr_kaupanda = models.CharField(max_length=255)

    def __str__(self):
        return self.notandanafn