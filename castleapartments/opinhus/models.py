from datetime import datetime

from django.db import models
from eignir.models import Eign

class opinhus(models.Model):
    fra = models.DateTimeField(default=datetime.now, blank=True)
    til = models.DateTimeField(default=datetime.now, blank=True)
    eign = models.ForeignKey(Eign, on_delete=models.CASCADE)
    def __int__(self):
        return self.fra and self.til