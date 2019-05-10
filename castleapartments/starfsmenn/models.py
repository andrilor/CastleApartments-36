from django.db import models

class Starfsmadurmynd(models.Model):
    mynd = models.CharField(max_length=999)
    def __str__(self):
        return self.mynd

class Starfsmenn(models.Model):
    nafn = models.CharField(max_length=255)
    simi = models.IntegerField()
    netfang = models.CharField(max_length=255)
    starfsheiti = models.CharField(max_length=255)
    lysing = models.CharField(max_length=999, blank=True)
    starfsmadurmynd = models.ForeignKey(Starfsmadurmynd, on_delete=models.CASCADE)
    def __str__(self):
        return self.nafn