from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Items(models.Model):
    Items_Names = (
        ('R', 'Rock'),
        ('S', 'Scissors'),
        ('P', 'Paper'),
    )
    Name = models.CharField(max_length=1 , choices=Items_Names)
    def __str__(self):
        return  self.Name


#class User(models.Model):
#    Name = models.CharField(max_length=20)
#    Surname = models.CharField(max_length=20)
#    Email = models.CharField(max_length=30)
#    Password = models.CharField(max_length=30)
#    RegDate = models.DateField

class Games(models.Model):
    Time = models.DateTimeField
    User1 = models.ForeignKey(User, related_name='firstuser')
    User2 = models.ForeignKey(User, related_name='seconduser', default=1)
    Bet1 = models.ForeignKey(Items, related_name='firstuserbet')
    Bet2 = models.ForeignKey(Items, related_name='seconduserbet', default=1)
    def __str__(self):
        return self.id