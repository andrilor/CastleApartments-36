from datetime import datetime

from django.db import models
from eignir.models import Eign

#Heldur utanum tíma á fyiri opin hús og hvert hús getur haft oftar en einusinni opin hús -Andri
class opinhus(models.Model):
    fra = models.DateTimeField(default=datetime.now, blank=True)
    til = models.DateTimeField(default=datetime.now, blank=True)
    eign = models.ForeignKey(Eign, on_delete=models.CASCADE, related_name='er_opid')

    def __str__(self):
        return str(self.fra)
