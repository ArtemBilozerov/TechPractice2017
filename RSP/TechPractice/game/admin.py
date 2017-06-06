from django.contrib import admin

# Register your models here.
from game.models import Items, Games, Players

admin.site.register(Items)
admin.site.register(Games)
admin.site.register(Players)