from django.db import models
import uuid

class Product_Model(models.Model):
    name  = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
