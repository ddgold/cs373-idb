from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.db import connection
from collections import OrderedDict
from random import sample
from operator import attrgetter

from idb.models import Game, Developer, Platform


def home(request):
    developer_list = get_list_or_404(Developer)
    if (len(developer_list) > 5):
        developer_list = sorted(sample(developer_list, 10), key=attrgetter('name'))
    platform_list = get_list_or_404(Platform)
    if (len(platform_list) > 5):
        platform_list = sorted(sample(platform_list, 10), key=attrgetter('name'))
    game_list = get_list_or_404(Game)
    if (len(game_list) > 5):
        game_list = sorted(sample(game_list, 10), key=attrgetter('title'))
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
        data = ' '.join([d.name.lower(), d.status.lower(), d.address.lower()])
        if query in data or all(w in data for w in query_words):
            developer_results.append(d)
        else:
            for word in query_words:
                if word in data:
                    partial_matches.append(d)
                    break
    developer_results += partial_matches

    platform_results = []
    partial_matches = []
    for p in platform_list:
        data = ' '.join([p.name.lower(), p.manufacturer.lower()])
        if query in data or all(w in data for w in query_words):
            platform_results.append(p)
        else:
            for word in query_words:
                if word in data:
                    partial_matches.append(p)
                    break
    platform_results += partial_matches

    game_results = []
    partial_matches = []
    for g in game_list:
        data = ' '.join([g.title.lower(), g.genre.lower(), g.publisher.lower()])
        if query in data or all(w in data for w in query_words):
            game_results.append(g)
        else:
            for word in query_words:
                if word in data:
                    partial_matches.append(g)
                    break
    game_results += partial_matches

    return render(request, 'search.html', {
        'query': original_query,
        'developer_results': developer_results,
        'platform_results': platform_results,
        'game_results': game_results,
    })

def queries(request):
    queries = [
        {
            "description": "Get the video games that do not have an ESRB rating of M, but have an another valid ESRB rating.",
            "sql": "select title, esrb_rating\n\tfrom idb_game\n\twhere esrb_rating != 'M' and ESRB_rating != 'N/A';",
        },
        {
            "description": "Get the video games that appear on more than one platform.",
            "sql": "select title, count(*)\n\tfrom idb_game inner join idb_game_platforms\n\ton idb_game.id = idb_game_platforms.game_id\n\tgroup by idb_game.id\n\thaving count(*) > 1;",
        },
        {
            "description": "Get the video games that were created by now defunct developers.",
            "sql": "select title, genre, publisher\n\tfrom idb_game\n\twhere developer_id in\n\t\t(select idb_developer.id\n\t\t\tfrom idb_developer\n\t\t\twhere status = 'Defunct');",
        },
        {
            "description": "Get the platforms in which only one developer in the database has worked on.",
            "sql": "select name, manufacturer\n\tfrom idb_platform\n\twhere id in\n\t\t(select platform_id\n\t\t\tfrom idb_developer_platforms\n\t\t\tgroup by platform_id\n\t\t\thaving count(platform_id) = 1);",
        },
        {
            "description": "Get the developers that created a game during the 6th generation of consoles.",
            "sql": "select name, status\n\tfrom idb_developer\n\twhere id in\n\t\t(select developer_id\n\t\t\tfrom idb_developer_platforms\n\t\t\twhere platform_id in\n\t\t\t\t(select id\n\t\t\t\t\tfrom idb_platform\n\t\t\t\t\twhere generation = 6));",
        },
    ]

    for q in queries:
        cursor = connection.cursor()
        cursor.execute(q['sql'])
        q['results'] = cursor.fetchall()

    return render(request, 'queries.html', {
    'queries': queries,
    })

