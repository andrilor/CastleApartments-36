from django.db import models

# Create your models here.


class Starfsmadur(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)

class StarfsmadurImage(models.Model):
    image = models.CharField(max_length=999)
    starfsmadur = models.ForeignKey(Starfsmadur, on_delete=models.CASCADE)
