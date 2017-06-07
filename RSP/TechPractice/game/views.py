
from django.shortcuts import render
from game.models import Game
from datetime import datetime
# Create your views here.

def home(request):
    #return HttpResponse('Hello world')
    return render(request, 'game/login_form.html')

def stats(request):
    #return HttpResponse('Hello world')
    return render(request, 'game/stats.html')

def history(request):
    #return HttpResponse('Hello world')
    playedgames = Game.objects.all()[:10]
    context = {
        'games': playedgames
    }
    return render(request, 'game/history.html', context)

def games(request):
    #return HttpResponse('Hello world')
    return render(request, 'game/games.html')

def choise(request):

    return render(request, 'game/choise.html')


def choise(request, str):
    if str == "rock":
        return render(request, 'game/choise.html')