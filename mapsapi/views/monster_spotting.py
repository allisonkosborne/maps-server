"""View module for handling requests about monster spotting"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mapsapi.models import MonsterSpotting, MonsterUser, Location, Species, monster_spotting, monster_user

class MonsterSpottingView(ViewSet):
  """MAPS monster spotting view"""
  def retrieve(self, request, pk):
    """Handle GET requests for single monster spotting
    Returns:
      Response -- JSON serialized monster spotting
    """
    monster_spotting = MonsterSpotting.objects.get(pk=pk)
    serializer = MonsterSpottingSerializer(monster_spotting)
    return Response(serializer.data)
    
  def list(self, request):
    """Handle GET requests to get all monster spottings
    Returns:
      Response -- JSON serialized list of monster spottings
    """
    monster_spotting = MonsterSpotting.objects.all()
    serializer = MonsterSpottingSerializer(monster_spotting, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST operations
    Returns
      Response -- JSON serialized monster spotting
    """
    monster_user = MonsterUser.objects.get(user=request.auth.user)
    location = Location.objects.get(pk=request.data["location"])
    species = Species.objects.get(pk=request.data["species"])
    
    monster_spotting = MonsterSpotting.objects.create(
      location=location,
      species=species,
      monster_user=monster_user,
      date=request.data["date"],
      time=request.data["time"]
    )
    serializer = MonsterSpottingSerializer(monster_spotting)
    return Response(serializer.data)
    
class MonsterSpottingSerializer(serializers.ModelSerializer):
  """JSON serializer for monster spottings"""
  class Meta:
    model = MonsterSpotting
    fields = ('monster_user', 'location', 'species', 'date', 'time')
    