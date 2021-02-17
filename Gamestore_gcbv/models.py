from django.db import models

class Game_store_Model(models.Model):
    game_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    rating = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.game_name
