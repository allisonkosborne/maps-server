from django.db import models
from django.contrib.auth.models import User
from user import User
from location import Location
from monster import Monster
from datetime import date
from time import time


class MonsterSpotting(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    monster_date = models.DateTimeField(max_length=50)
    monster_time = models.TimeField(max_length=25)
    