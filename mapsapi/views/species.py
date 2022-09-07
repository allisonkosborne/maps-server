"""View module for handling requests about species"""
from os import stat
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import serializers, status
from mapsapi.models import Species, species
from mapsapi.models import MonsterUser, monster_user

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
  
  
  # def create(self, request):
  #   """Handles create for a new event"""
  #   try: 
  #       monster_user = MonsterUser.objects.get(user=request.auth.user)
  #       species = Species.objects.create(
  #         name=request.data['name'],
  #         food=request.data['food']
  #       )
        
  #       serializer = SpeciesSerializer(
  #         species, many=False, context={"request": request})
  #       return Response(serializer.data, status=status.HTTP_201_CREATED)
  #   except Exception as ex: 
  #     return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
  
  
  
  def create(self, request):
        """Handles POST requests for species"""
        monster_user = MonsterUser.objects.get(user=request.auth.user)
        # species = Species.objects.get(user=request.auth.user)
        serializer = CreateSpeciesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        species = serializer.save(monster_user=monster_user)
        # res_serializer = SpeciesSerializer(species)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
  def update(self, request: Request, pk):
        """Handles PUT request for a game, returning a 204 with no body on success"""
        species = Species.objects.get(pk=pk)
        serializer = SpeciesSerializer(species, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
  def destroy(self, request, pk):
        species = Species.objects.get(pk=pk)
        species.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
  
class SpeciesSerializer(serializers.ModelSerializer):
  """JSON serializer for species"""
  class Meta:
    model = Species
    fields = ('id', 'name', 'food', 'monster_user_id')
    

class CreateSpeciesSerializer(serializers.ModelSerializer):
    """Represents and validates a created species"""
    class Meta:
        model = Species
        fields = (
            'id',
            'name',
            'food',
            'monster_user_id'
        )