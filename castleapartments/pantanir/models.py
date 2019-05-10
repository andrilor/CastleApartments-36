from django.db import models
from django.contrib.auth.models import User
from eignir.models import Eign

class Pantanir(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE for the time being.
    properties = models.ForeignKey(Eign, on_delete=models.CASCADE) # CASCADE for the time being.
    card_number = models.CharField(max_length=19)
    card_expiration_date = models.DateField()