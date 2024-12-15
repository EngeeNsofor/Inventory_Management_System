from rest_framework import serializers
from .models import InventoryItem
from django.contrib.auth.models import User

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'description', 'price', 'quantity_in_stock']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']