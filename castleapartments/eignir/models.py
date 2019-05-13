from django.db import models
from starfsmenn.models import Starfsmenn

class Eign(models.Model):
    heimilisfang = models.CharField(max_length=255)
    baejarfelag = models.CharField(max_length=255)
    postnumer = models.IntegerField()
    verd = models.IntegerField()
    brunabotamat = models.IntegerField()
    fasteignamat = models.IntegerField()
    tegund = models.CharField(max_length=255)
    lysing = models.CharField(max_length=999, blank=True)
    staerd = models.IntegerField()
    byggingarar = models.DateField()
    fjoldi_herbergja = models.IntegerField()
    fjoldi_badherberga = models.IntegerField()
    fjoldi_svefnherberga = models.IntegerField()
    sett_a_solu = models.DateField()
    laust_nuna = models.BooleanField()
    teikning = models.BooleanField()
    serinngangur = models.BooleanField()
    sameigninlegur_inngangur = models.BooleanField()
    solpallur = models.BooleanField()
    svalir = models.BooleanField()
    gardur = models.BooleanField()
    thvottahus = models.BooleanField()
    hjolastolaadgengi = models.BooleanField()
    lyfta = models.BooleanField()
    bilskur = models.BooleanField()
    bilastaedi = models.BooleanField()
    nafn_seljanda = models.CharField(max_length=255)
    simi_seljanda = models.IntegerField()
    netfang_seljanda = models.CharField(max_length=255)
    starfsmenn = models.ForeignKey(Starfsmenn, on_delete=models.CASCADE)
    def __str__(self):
        return self.heimilisfang

class GPS_Stadsetning(models.Model):
    heimilisfang = models.CharField(max_length=255)
    lat = models.FloatField(max_length=(10, 6))
    lng = models.FloatField(max_length=(10, 6))
    eign = models.ForeignKey(Eign, on_delete=models.CASCADE)
    def __str__(self):
        return self.lat and self.lat

class Eignmynd(models.Model):
    mynd = models.CharField(max_length=999)
    eign = models.ForeignKey(Eign, on_delete=models.CASCADE)
    def __str__(self):
        return self.mynd

