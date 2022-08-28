from django.db import models
from mapsapi.models.monster_user import MonsterUser



class Species(models.Model):

    monster_user = models.ForeignKey(MonsterUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    food = models.CharField(max_length=50)