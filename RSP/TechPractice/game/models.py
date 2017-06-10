
from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    Items_Names = (
        ('1', 'Rock'),
        ('2', 'Scissors'),
        ('3', 'Paper'),
    )
    name = models.CharField(max_length=1 , choices=Items_Names)
    def __str__(self):
        return  self.name


class Game(models.Model):
    time = models.DateTimeField(default=datetime.now())
    user1login = models.CharField(default='bot',max_length=16)
    user2login = models.CharField(default='bot',max_length=16)
    bet1 = models.CharField(default='1',max_length=1)
    bet2 = models.CharField(default='1',max_length=1)
    result = models.CharField(default='drow',max_length=4) #drow win lose