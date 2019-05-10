from django.db import models
from django.contrib.auth.models import User
from eignir.models import Eign

class Pantanir(models.Model):
    notandanafn = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE for the time being.
    eignir = models.ForeignKey(Eign, on_delete=models.CASCADE) # CASCADE for the time being.
    kortanumer = models.CharField(max_length=19)
    dagsetning_kort = models.DateField()