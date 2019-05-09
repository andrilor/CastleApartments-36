from django.db import models
from eignir.models import Eignir

class opinhus(models.Model):
    Start = models.DateTimeField()
    End = models.DateTimeField()
    eignir = models.ForeignKey(Eignir, on_delete=models.CASCADE)