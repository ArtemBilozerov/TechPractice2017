from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(self):
    #return HttpResponse('Hello world')
    return render(self, 'game/index.html')