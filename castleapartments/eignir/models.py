from django.db import models
from starfsmenn.models import Starfsmenn

class GPS_Stadsetning(models.Model):
    gotuheiti = models.CharField(max_length=255)
    lat = models.FloatField(max_length=(10, 6))
    lng = models.FloatField(max_length=(10, 6))

class Eign(models.Model):
    Address = models.CharField(max_length=255)
    Town_name = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    Price = models.IntegerField()
    Brunabotamat = models.IntegerField()
    Fasteignamat = models.IntegerField()
    Type = models.CharField(max_length=255)
    Description = models.CharField(max_length=999, blank=True)
    Size = models.FloatField()
    Building_year = models.DateField()
    Number_of_rooms = models.IntegerField()
    Number_of_bathrooms = models.IntegerField()
    Number_of_bedrooms = models.IntegerField()
    put_on_sale = models.DateTimeField()
    Available_now = models.BooleanField()
    Housed_drawing = models.BooleanField()
    private_entrance = models.BooleanField()
    public_entrance = models.BooleanField()
    Sundeck = models.BooleanField()
    Balcony = models.BooleanField()
    Garden = models.BooleanField()
    Laundry_room = models.BooleanField()
    wheelchair_Access = models.BooleanField()
    Elevator = models.BooleanField()
    Garage = models.BooleanField()
    Parking_Space = models.BooleanField()

    Seller_Name = models.CharField(max_length=255)
    Seller_Phone = models.IntegerField()
    Seller_Email = models.CharField(max_length=255)
    Starfsmenn = models.ForeignKey(Starfsmenn, on_delete=models.CASCADE)
    GPS_Stadsetning = models.ForeignKey(GPS_Stadsetning, on_delete=models.CASCADE)

class EignImage(models.Model):
    image = models.CharField(max_length=999)
    Eign = models.ForeignKey(Eign, on_delete=models.CASCADE)


