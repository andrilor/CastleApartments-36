from django.db import models
from eignir.models import Eign
from django.contrib.auth.models import User
from django.utils import timezone

class Leitarsaga(models.Model):
    notandanafn = models.ForeignKey(User, on_delete=models.CASCADE)  # CASCADE for the time being.
    eign = models.ForeignKey(Eign, on_delete=models.CASCADE, related_name='Leitarsaga_eign')  # CASCADE for the time being.
    time_stamp = models.DateTimeField(default=timezone.now)

    def __int__(self):
        return self.notandanafn