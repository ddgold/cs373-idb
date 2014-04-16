from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from collections import OrderedDict

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
    developer_dict = OrderedDict(sorted(developer_dict.items()))
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
    platform_dict = OrderedDict(sorted(platform_dict.items()))
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
    game_dict = OrderedDict(sorted(game_dict.items()))
    return render(request, 'games.html', {
    'game_dict': game_dict,
    })

def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game.html', {
    'game': game,
    })

def search(request):
    query = ""

    if request.method == 'GET':
        query = request.GET.get('query', '')
    if not query:
        return HttpResponseRedirect('/')

    original_query = query
    query = query.lower()
    query_words = query.split()

    developer_list = get_list_or_404(Developer)
    platform_list = get_list_or_404(Platform)
    game_list = get_list_or_404(Game)

    developer_results = []
    partial_matches = []
    for d in developer_list:
        name = d.name.lower()
        if query in name or all(w in name for w in query_words):
            developer_results.append(d)
        else:
            for word in query_words:
                if word in name:
                    partial_matches.append(d)
                    break
    developer_results += partial_matches

    platform_results = []
    partial_matches = []
    for p in platform_list:
        name = p.name.lower()
        if query in name or all(w in name for w in query_words):
            platform_results.append(p)
        else:
            for word in query_words:
                if word in name:
                    partial_matches.append(p)
                    break
    platform_results += partial_matches

    game_results = []
    partial_matches = []
    for g in game_list:
        name = g.title.lower()
        if query in name or all(w in name for w in query_words):
            game_results.append(g)
        else:
            for word in query_words:
                if word in name:
                    partial_matches.append(g)
                    break
    game_results += partial_matches

    return render(request, 'search.html', {
        'query': original_query,
        'developer_results': developer_results,
        'platform_results': platform_results,
        'game_results': game_results,
    })
