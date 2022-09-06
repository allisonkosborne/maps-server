from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from mapsapi.models import MonsterUser, MonsterSpotting, monster_user
from rest_framework.decorators import action

class MonsterUserView(ViewSet):
  """"User View"""
  # @permission_classes([AllowAny])
  def retrieve(self, request, pk):
    users = MonsterUser.objects.get(pk=pk)
    serializers = MonsterUserSerializer(users)
    return Response(serializers.data)
  
   # @permission_classes([AllowAny])
  def list(self, request):
        users = MonsterUser.objects.all()
        serializer = MonsterUserSerializer(users, many=True)
        return Response(serializer.data)
  
  @action(methods=['get'], detail=True)
  def userSpotting(self, request,pk):
        spottings = MonsterSpotting.objects.all().filter(user_id=pk)
        serializer = UserPostSerializer(spottings, many=True)        
        return Response(serializer.data)
  
#   def update(self, request: Request, pk):
#         """Handles PUT request for a game, returning a 204 with no body on success"""
#         monster_user = MonsterUser.objects.get(pk=pk)
#         serializer = MonsterUserSerializer(monster_user, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(None, status=status.HTTP_204_NO_CONTENT)
    
#   def destroy(self, request, pk):
#         monster_user = MonsterUser.objects.get(pk=pk)
#         monster_user.delete()
#         return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  
class MonsterUserSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    first_name = serializers.CharField(source = 'user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    class Meta:
        model = MonsterUser

        fields = ('first_name', 'last_name', 'weapon')
        # depth = 1
        
# class MonsterSpottingSerializer(serializers.ModelSerializer):
#     """JSON serializer for users
#     """
#     user = MonsterUserSerializer(many=False)
#     class Meta:
#         model = MonsterSpotting
#         fields = ('date', 'time','location')