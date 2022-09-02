"""maps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from mapsapi.views import register_user, login_user
from mapsapi.views.location import LocationView
from mapsapi.views.species import SpeciesView
from mapsapi.views.monster_spotting import MonsterSpottingView
from mapsapi.views.monster_user import MonsterUserView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'locations', LocationView, 'location')
router.register(r'species', SpeciesView, 'species')
router.register(r'spottings', MonsterSpottingView, 'spotting')
router.register(r'users', MonsterUserView, 'user')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
# Register: requests to http://localhost:8000/register will be routed to the register_user function; Login: requests to http://localhosr:8000/login will be routed to the login_user function 