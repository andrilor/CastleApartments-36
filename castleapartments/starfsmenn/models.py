from django.db import models

# allar upplisingar fyrir starfsmenn geimdar hér -Andri
class Starfsmenn(models.Model):
    nafn = models.CharField(max_length=255)
    simi = models.IntegerField()
    netfang = models.CharField(max_length=255)
    starfsheiti = models.CharField(max_length=255)
    lysing = models.CharField(max_length=999, blank=True)
    def __str__(self):
        return self.nafn

# myndir fyrir starfsmenn eru geimar hér -Andri
class Starfsmadurmynd(models.Model):
    mynd = models.CharField(max_length=999)
    starfsmenn = models.ForeignKey(Starfsmenn, on_delete=models.CASCADE)
    def __str__(self):
        return self.mynd