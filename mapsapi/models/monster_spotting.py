from django.db import models
from django.contrib.auth.models import User
from mapsapi.models.monster_user import MonsterUser
from mapsapi.models.location import Location# 
from mapsapi.models.species import Species
from datetime import date
from time import time


class MonsterSpotting(models.Model):

    monster_user = models.ForeignKey(MonsterUser, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    date = models.DateTimeField(max_length=50)
    time = models.TimeField(max_length=25)
    