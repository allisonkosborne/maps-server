# from logging.config import _LoggerConfiguration
from django.db import models
from django.contrib.auth.models import User
from mapsapi.models.location import Location

class MonsterUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    weapon = models.CharField(max_length=50)