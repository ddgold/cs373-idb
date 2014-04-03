from django.shortcuts import render, get_object_or_404, get_list_or_404

from idb.models import Game, Developer, Platform

developer_list = get_list_or_404(Developer)
platform_list = get_list_or_404(Platform)
game_list = get_list_or_404(Game)

def home(request):
    return render(request, 'home.html', {
    'developer_list': developer_list,
    'platform_list': platform_list,
    'game_list': game_list,
    })

def game(request, game_title):
    game = get_object_or_404(Game, title=game_title)
    return render(request, 'game.html', {
    'game': game,
    'developer_list': developer_list,
    'platform_list': platform_list,
    'game_list': game_list,
    })

def platform(request, platform_name):
    platform = get_object_or_404(Platform, name=platform_name)
    return render(request, 'platform.html', {
    'platform': platform,
    'developer_list': developer_list,
    'platform_list': platform_list,
    'game_list': game_list,
    })

def developer(request, developer_name):
    developer = get_object_or_404(Developer, name=developer_name)
    return render(request, 'developer.html', {
    'developer': developer,
    'developer_list': developer_list,
    'platform_list': platform_list,
    'game_list': game_list,
    })
