from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
    name         = models.CharField(max_length=120)
    location     = models.CharField(max_length=120, null=True, blank=True)