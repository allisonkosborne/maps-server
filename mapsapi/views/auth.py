from urllib import request
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from mapsapi.models import MonsterUser

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
  """Handles the authentication of a monster user
  Method arguments:
  request -- The full HTTP request object"""
  username = request.data['username']
  password = request.data['password']
  
  # USe the built-in authenticate method to verify
  # authenticate returns the user object or None if no user is found
  authenticated_user = authenticate(username=username, password=password)
  
  #If authentication was successful, respond with their token
  if authenticated_user is not None:
    token = Token.objects.get(user=authenticated_user)
    data = {
      'valid': True,
      'token': token.key
    }
    return Response(data)
  else:
    # Bad login details were provided so we cant log the user in.
    data = { 'valid': False }
    return Response(data)
  
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
  '''Handles the creation of a new user for authentication
  Method arguments:
  request --- The full HTTP request object'''
  
  #Create a new user by invoking the 'create_user' helper method
  # On Django's built-in User Model
  new_user = User.objects.create_user(
    username=request.data['username'],
    password=request.data['password'],
    first_name=request.data['first_name'],
    last_name=request.data['last_name']
  )
  
  #Now save the extra info in the mapsapi_monsteruser table
  monsteruser = MonsterUser.objects.create(
    weapon=request.data['weapon'],
    user=new_user
  )
  
  # Use the REST framework's token generator on the new user #account
  
  token = Token.objects.create(user=monsteruser.user)
  # Return the token to the client 
  data = { 'token': token.key }
  return Response(data)
  
  
  