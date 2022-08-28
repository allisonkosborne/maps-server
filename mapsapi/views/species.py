"""View module for handling requests about species"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mapsapi.models import Species

class SpeciesView(ViewSet):
  """MAPS species view"""
  def retrieve(self, request, pk):
    """Handle GET requests for single species
    Returns:
      Response -- JSON serialized species
    """
    species = Species.objects.get(pk=pk)
    serializer = SpeciesSerializer(species)
    return Response(serializer.data)
    
  def list(self, request):
    """Handle GET requests to get all species
    Returns:
      Response -- JSON serialized list of species
    """
    species = Species.objects.all()
    serializer = SpeciesSerializer(species, many = True)
    return Response(serializer.data)
  
class SpeciesSerializer(serializers.ModelSerializer):
  """JSON serializer for species"""
  class Meta:
    model = Species
    fields = ('id', 'name', 'food', 'monster_user_id')