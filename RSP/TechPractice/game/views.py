from collections import Iterator
from django.shortcuts import render
from django.contrib import auth
from  django.template.context_processors import csrf
from game.models import Game, Item
import random
from  datetime import datetime
from  django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import contenttypes
# Create your views here.

def home(request):
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

def reg(request):
    args = {}
    args.update(csrf(request))

    if request.POST:
        newuser = UserCreationForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            newuser = auth.authenticate(username=newuser.cleaned_data['username'], password=newuser.cleaned_data['password2'])
            return render(request, 'game/start.html')
        else:
            args['form'] = newuser
    return render(request, 'game/register_form.html', args)


class Plgame():
    win = 0
    lose = 0
    drow = 0
    username = ''
    time = datetime.now()
    def __init__(self,w,l,d,u,t):
        self.win = w
        self.lose = l
        self.drow = d
        self.username = u
        self.time = t

def stats(request):
    #return HttpResponse('Hello world')}

    glist = []
    users = User.objects.all()[:20]
    print(users)
    for user in users:
        glist.append(Plgame(
            Game.objects.all().filter(user1login=user.username, result='win').count(),
            Game.objects.all().filter(user1login=user.username, result='lose').count(),
            Game.objects.all().filter(user1login=user.username, result='drow').count(),
            user.username,
            user.date_joined,

        ))
    context = iter(glist)
    pgame = {'games': context}
    print(context)
    return render(request, 'game/stats.html', pgame)

def history(request):
    items = {'1': 'rock', '2': 'scissors', '3': 'paper'}
    pgame = Game.objects.order_by('-time').filter(user1login=auth.get_user(request).username)[:20]
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
    elif (bet[0] == '1' and botchoise == 2) \
            or (bet[0] == '2' and botchoise == 3) or (bet[0] == '3' and botchoise == 1):
        result = 'win'
    else:
        result = 'lose'
    playedgame = Game(user1login=auth.get_user(request).username, user2login='bot', bet1=bet[0], bet2=botchoise, result=result, time=datetime.now())
    playedgame.save()
    return render(request, 'game/result.html', {'bet1': bet[0], 'bet2': botchoise,'result': result})


def start(request):
    return render(request, 'game/start.html', {'username':auth.get_user(request).username})