from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name