
from django.shortcuts import render
from  game.models import Games
# Create your views here.

def home(request):
    #return HttpResponse('Hello world')
    return render(request, 'game/login_form.html')

def stats(request):
    #return HttpResponse('Hello world')
    return render(request, 'game/stats.html')

def history(request):
    #return HttpResponse('Hello world')
    playedgames = Games.objects.all()
    return render(request, 'game/history.html')

def games(request):
    #return HttpResponse('Hello world')
    return render(request, 'game/games.html')