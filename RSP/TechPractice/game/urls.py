"""TechPractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from urllib import request

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stats', views.stats, name='stats'),
    url(r'^games', views.games, name='games'),
    url(r'^history', views.history, name='history'),

    url(r'^choiced/rock', views.choiced, {'bet': '1'}, name='rock'),
    url(r'^choiced/scissors', views.choiced, {'bet': '2'}, name='scissors'),
    url(r'^choiced/paper', views.choiced, {'bet': '3'}, name='paper'),
    url(r'^choice', views.choice, name='choice'),
    url(r'^start', views.start, name='start'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^login', views.login, name='login'),
    url(r'^', views.home, name='home'),
]