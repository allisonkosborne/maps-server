from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from mapsapi.models import MonsterUser, MonsterSpotting
from rest_framework.decorators import action

class MonsterUserView(ViewSet):
  """"User View"""
  # @permission_classes([AllowAny])
  def  retrieve(self, request, pk):
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
  
  
class MonsterUserSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    first_name = serializers.CharField(source = 'user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    class Meta:
        model = MonsterUser

        fields = ('user', 'weapon')
        # depth = 1
        
class UserPostSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    user = MonsterUserSerializer(many=False)
    class Meta:
        model = MonsterSpotting
        fields = ('date', 'time','location')