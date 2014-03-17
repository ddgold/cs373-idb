from django.shortcuts import render

from models import Game, Developer, Platform


def home(request):
    return render(request, 'home.html')
