from django.db import models

class Movie_Model(models.Model):
    name  = models.CharField(max_length=50)
    price = models.FloatField()
    genere = models.CharField(max_length=50)
    rating = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
