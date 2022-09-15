"""View module for handling requests about monster spotting"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import serializers, status
from mapsapi.models import MonsterSpotting, MonsterUser, Location, Species, location, monster_spotting, monster_user, species

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
    monster_spotting = MonsterSpotting.objects.create(
      monster_user = MonsterUser.objects.get(user=request.auth.user),
      location= Location.objects.get(id=request.data["location"]),
      species=Species.objects.get(id=request.data["species"]),
      date=request.data["date"],
      time=request.data["time"]
    )
    serializer = CreateMonsterSpottingSerializer(monster_spotting)
    return Response(serializer.data)

  def update(self, request, pk):
    """Handle PUT requests for monster spottings Returns: Response - empty body with 204 status code"""
    monster_spotting = MonsterSpotting.objects.get(pk=pk)
    # monster_user=MonsterUser.objects.get(user=request.data["monster_user"]),
    monster_spotting.species = Species.objects.get(id=request.data["species"])
    monster_spotting.location = Location.objects.get(id=request.data["location"])
    monster_spotting.time = request.data["time"]
    monster_spotting.date = request.data["date"]
    monster_spotting.save()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
      
  def destroy(self, request, pk):
        monster_spotting = MonsterSpotting.objects.get(pk=pk)
        monster_spotting.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class MonsterSpottingSerializer(serializers.ModelSerializer):
  """JSON serializer for monster spottings"""
  class Meta:
    model = MonsterSpotting
    fields = ('id', 'monster_user', 'location', 'species', 'date', 'time')
    depth = 1
    
class CreateMonsterSpottingSerializer(serializers.ModelSerializer):
  """JSON serializer for monster spottings"""
  class Meta:
    model = MonsterSpotting
    fields = ('id', 'monster_user_id', 'location', 'species', 'date', 'time')
    