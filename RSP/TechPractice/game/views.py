
from django.shortcuts import render
from django.contrib import auth
from  django.template.context_processors import csrf
from game.models import Game, Item
import random
from  datetime import datetime
from  django.contrib.auth.models import User
from django.contrib import contenttypes
# Create your views here.

def home(request):
    users = User.objects.all()[:20]
    for user in users:
        Game.objects.get(user1login=user.username)
    if auth.get_user(request).is_authenticated:
        print(auth.get_user(request).username)
        return render(request,'game/start.html')
    else:
        return render(request, 'game/login_form.html')
def login(request):
    print('hello')
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print(1)
            return render(request,'game/start.html')
        else:
            print(2)
            return render(request, 'game/login_form.html',{'error':'invalid_user'})
    else:
        print(3)
        return render(request, 'game/login_form.html', {'error': 'wrong_request'})

def logout(request):
    print('2223')
    auth.logout(request)
    return render(request,'game/login_form.html')

def stats(request):
    #return HttpResponse('Hello world')}
    context = {

    }
    return render(request, 'game/stats.html', context)

def history(request):
    items = {'1': 'rock', '2': 'scissors', '3': 'paper'}
    pgame = Game.objects.order_by('-time')[:20]
    for gg in pgame:
        gg.bet1 = items[gg.bet1]
        gg.bet2 = items[gg.bet2]
    context = {'games': pgame}
    return render(request, 'game/history.html',context)

def games(request):
    #return HttpResponse('Hello world')
    return render(request, 'game/games.html')

def choice(request):
    print('choice')
    return render(request, 'game/choice.html')

def choiced(request, bet):
    print('r4r4r4r4r')
    botchoise = random.randint(1,3)
    result = ''
    print(bet[0])
    if bet[0] == str(botchoise):
        result = 'drow'
    elif (bet[0] == '1' and botchoise == 2)\
            or (bet[0] == '2' and botchoise == 3) or (bet[0] == '3' and botchoise == 1):
        result = 'win'
    else:
        result = 'lose'
    playedgame = Game(user1login=auth.get_user(request).username, user2login='bot', bet1=bet[0], bet2=botchoise, result=result, time=datetime.now())
    playedgame.save()
    return render(request, 'game/result.html', {'bet1': bet[0], 'bet2': botchoise,'result': result})


def start(request):
    return render(request, 'game/start.html', {'username':auth.get_user(request).username})