from logging.config import _LoggerConfiguration
from django.db import models
from django.contrib.auth.models import User
from location import Location


class User(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    species = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    weapon = models.CharField(max_length=50)
    
    