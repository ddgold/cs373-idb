from django.shortcuts import render, get_object_or_404

from idb.models import Game, Developer, Platform


def home(request):
    return render(request, 'home.html')

def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game.html', {
	'game': game,
    })
