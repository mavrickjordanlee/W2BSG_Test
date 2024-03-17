from django.db import models

class Game(models.Model):
    game_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    wait_time = models.IntegerField()