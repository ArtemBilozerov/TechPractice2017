from django.contrib import admin

# Register your models here.
from game.models import Item, Game, Player

admin.site.register(Item)
admin.site.register(Game)
admin.site.register(Player)