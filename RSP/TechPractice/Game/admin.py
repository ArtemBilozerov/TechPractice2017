from django.contrib import admin

# Register your models here.
from Game.models import Items, Games

admin.site.register(Items)
admin.site.register(Games)