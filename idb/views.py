from django.shortcuts import render

from idb.models import Game, Developer, Platform


def home(request):
    return render(request, 'home.html')
