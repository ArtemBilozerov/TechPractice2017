from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Item(models.Model):
    Items_Names = (
        ('R', 'Rock'),
        ('S', 'Scissors'),
        ('P', 'Paper'),
    )
    Name = models.CharField(max_length=1 , choices=Items_Names)
    def __str__(self):
        return  self.Name

class Player(User):
    Wins = models.CharField(default=0, max_length=16)
    Loses = models.CharField(default=0, max_length=16)
    def __str__(self):
        return self.username

class Game(models.Model):
    Time = models.DateTimeField
    User1 = models.ForeignKey(User, related_name='firstuser')
    User2 = models.ForeignKey(User, related_name='seconduser', default=1)
    Bet1 = models.ForeignKey(Item, related_name='firstuserbet')
    Bet2 = models.ForeignKey(Item, related_name='seconduserbet', default=1)
    def __str__(self):
        return str(self.id)