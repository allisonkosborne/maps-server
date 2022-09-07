"""View modules for handling requests about locations"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mapsapi.models import Location
from mapsapi.models import MonsterUser

class LocationView(ViewSet):
  """MAPS location view"""
  
  def retrieve(self, request, pk):
    """Handle GET requests for single location
    Returns:
      Response -- JSON serialized location
    """
    location = Location.objects.get(pk=pk)
    serializer = LocationSerializer(location)
    return Response(serializer.data)
    
    
  def list(self, request):
    """Handle GET requests to get all locations
    Returns:
      Response -- JSON serialized list of locations
    """
    location = Location.objects.all()
    serializer = LocationSerializer(location, many=True)
    return Response(serializer.data)
  
  def create(self, request):
        """Handles POST requests for species"""
        monster_user = MonsterUser.objects.get(user=request.auth.user)
        # species = Species.objects.get(user=request.auth.user)
        serializer = CreateLocationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        locations = serializer.save(monster_user=monster_user)
        # res_serializer = SpeciesSerializer(species)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
  
class LocationSerializer(serializers.ModelSerializer):
  """JSON serializer for locations"""
  class Meta:
    model = Location
    fields = ('id', 'name')
    
class CreateLocationSerializer(serializers.ModelSerializer):
  """JSON serializer for locations"""
  class Meta:
    model = Location
    fields = ('id', 'name')