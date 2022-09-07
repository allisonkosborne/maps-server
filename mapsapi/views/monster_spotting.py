"""View module for handling requests about monster spotting"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
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
    # species = Species.objects.get(user=request.auth.user)
    serializer = CreateMonsterSpottingSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    monster_spotting = serializer.save(monster_user=monster_user)
    # res_serializer = SpeciesSerializer(species)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    # monster_user = MonsterUser.objects.get(user=request.auth.user)
    # location = Location.objects.get(pk=request.data["location"])
    # species = Species.objects.get(pk=request.data["species"])
    
    # monster_spotting = MonsterSpotting.objects.create(
    #   location=location,
    #   species=species,
    #   monster_user=monster_user,
    #   date=request.data["date"],
    #   time=request.data["time"]
    # )
    # serializer = CreateMonsterSpottingSerializer(monster_spotting)
    # return Response(serializer.data)
  
  def update(self, request: Request, pk):
        """Handles PUT request for a game, returning a 204 with no body on success"""
        monster_spotting = MonsterSpotting.objects.get(pk=pk)
        serializer = CreateMonsterSpottingSerializer(monster_spotting, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

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
    fields = ('id', 'monster_user', 'location', 'species', 'date', 'time')
    