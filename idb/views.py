from django.shortcuts import render, get_object_or_404, get_list_or_404

from idb.models import Game, Developer, Platform


def home(request):
    developer_list = get_list_or_404(Developer)
    platform_list = get_list_or_404(Platform)
    game_list = get_list_or_404(Game)
    return render(request, 'home.html', {
    'developer_list': developer_list,
    'platform_list': platform_list,
    'game_list': game_list,
    })

def developers(request):
    developer_list = get_list_or_404(Developer)
    developer_dict = {}
    for developer in developer_list :
        letter = developer.name[0].capitalize()
        if not letter.isalpha() :
            letter = "#"
        if letter in developer_dict :
            developer_dict[letter] += [developer]
        else :
            developer_dict[letter] = [developer]
    return render(request, 'developers.html', {
    'developer_dict': developer_dict,
    })

def developer(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    return render(request, 'developer.html', {
    'developer': developer,
    })

def platforms(request):
    platform_list = get_list_or_404(Platform)
    platform_dict = {}
    for platform in platform_list :
        letter = platform.name[0].capitalize()
        if not letter.isalpha() :
            letter = "#"
        if letter in platform_dict :
            platform_dict[letter] += [platform]
        else :
            platform_dict[letter] = [platform]
    return render(request, 'platforms.html', {
    'platform_dict': platform_dict,
    })

def platform(request, platform_id):
    platform = get_object_or_404(Platform, pk=platform_id)
    return render(request, 'platform.html', {
    'platform': platform,
    })

def games(request):
    game_list = get_list_or_404(Game)
    game_dict = {}
    for game in game_list :
        letter = game.title[0].capitalize()
        if not letter.isalpha() :
            letter = "#"
        if letter in game_dict :
            game_dict[letter] += [game]
        else :
            game_dict[letter] = [game]
    return render(request, 'games.html', {
    'game_dict': game_dict,
    })

def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game.html', {
    'game': game,
    })
