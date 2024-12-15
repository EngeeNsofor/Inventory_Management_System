from django.shortcuts import render
from rest_framework import viewsets
from .models import InventoryItem
from .serializers import InventoryItemSerializer, UserSerializer
from django.contrib.auth.models import User

# Create your views here.

class InventoryItemViewSet(viewsets.ModelViewSet):
    """
    viewsets.ModelViewSet provides a set of default actions 
    like create(), list(), retrieve(), update(), and destroy() 
    without needing to write them explicitly.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
