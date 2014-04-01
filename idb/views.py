from django.shortcuts import render, get_object_or_404

from idb.models import Game, Developer, Platform


def home(request):
    return render(request, 'home.html')

def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game.html', {
	'game': game,
    })

def platform(request, platform_id):
    platform = get_object_or_404(Platform, pk=platform_id)
    return render(request, 'platform.html', {
    'platform': platform,
    })

def developer(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    return render(request, 'developer.html', {
    'developer': developer,
    })
