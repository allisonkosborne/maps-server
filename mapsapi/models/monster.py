from django.db import models
from django.contrib.auth.models import User
from location import Location


class Monster(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    food = models.CharField(max_length=50)