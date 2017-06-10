from django.contrib import admin

# Register your models here.
from game.models import Item, Game

admin.site.register(Item)
admin.site.register(Game)