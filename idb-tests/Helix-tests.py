#! usr/bin/env python3

from urllib.request import Request, urlopen
import json, urllib
import unittest

class TestApiary (unittest.TestCase) :
  def test_GET_POKEMON(self):
    request = Request("http://helixapi.apiary.io/api/pokemon")
    response = urlopen(request)
    assert( response.msg == 'OK' )
    assert( response.reason == 'OK' )
    assert( response.status == 200 )

    matt = json.loads(response.read().decode('utf-8'))
    compare = {'pokemon': [{'trainer': 'Red', 'type': ['Grass', 'Poison'], 'name': 'Bulbasaur', 'p_id': 1}]}
    assert(compare == matt)

  def test_GET_POKEMON_ID(self):
    request = Request("http://helixapi.apiary.io/api/pokemon/1")
    response = urlopen(request)

    assert( response.msg == 'OK' )
    assert( response.reason == 'OK' )
    assert( response.status == 200 )

    matt = json.loads(response.read().decode('utf-8'))
    compare = {'type': ['Grass', 'Poison'], 'name': 'Bulbasaur', 'p_id': 1, 'height': 0.7, 'weight': 6.9, 'location': 'Kanto', 'kind': 'Seed', "description": "Bulbasaur is a small, quadruped Pokémon with green or bluish green skin and dark patches.", "images": ["http://bulbapedia.bulbagarden.net/wiki/File:001Bulbasaur.png"]}
    assert(compare == matt)

  def test_GET_TRAINER(self):
    request = Request("http://helixapi.apiary.io/api/trainer")
    response = urlopen(request)
    assert( response.msg == 'OK' )
    assert( response.reason == 'OK' )
    assert( response.status == 200 )

    matt = json.loads(response.read().decode('utf-8'))
    compare = {'trainer': [{'name': 'Red', 'kind': "Master", 'tr_id': 'tra_red'}]}
    assert(compare == matt)

  def test_GET_TRAINER_ID(self):
    request = Request("http://helixapi.apiary.io/api/trainer/tra_red")
    response = urlopen(request)
    assert( response.msg == 'OK' )
    assert( response.reason == 'OK' )
    assert( response.status == 200 )

    matt = json.loads(response.read().decode('utf-8'))
    compare = {
      "name": "Red",
      "tr_id": "tra_red",
      "badge": "",
      "location": "Pallet Town",
      "kind": "Master",
      "description": "Main Character of Pokemon Adventures",
      "images": ["http://bulbapedia.bulbagarden.net/wiki/File:Red_Adventures.png"],
      "citations": ["http://bulbapedia.bulbagarden.net/wiki/Red_%28Adventures%29"]  }
    assert(compare == matt)

  def test_GET_TYPE(self):
    request = Request("http://helixapi.apiary.io/api/types")
    response = urlopen(request)
    assert( response.msg == 'OK' )
    assert( response.reason == 'OK' )
    assert( response.status == 200 )

    matt = json.loads(response.read().decode('utf-8'))
    compare = {
      "types": [
          {
              "name": "Fire",
              "ty_id": "type_fire",
              "effect": [
                {
                    "att_strong": ["Bug", "Grass", "Ice", "Steel"],
                    "att_weak": ["Dragon", "Fire", "Rock", "Water"],
                    "def_strong": ["Bug", "Fairy", "Fire", "Grass", "Ice", "Steel"],
                    "def_weak": ["Ground", "Rock", "Water"]
                }
            ],
            "description": "Notable Trainers who specialize in Fire-type Pokémon include Blaine of Cinnabar Island, Flannery of Lavaridge Town, Flint of the Sinnoh Elite Four, Chili of Striaton City, and Malva of the Kalos Elite Four."
          }
        ]
      }
    assert(compare == matt)

  def test_GET_TYPE_ID(self):
    request = Request("http://helixapi.apiary.io/api/types/type_fire")
    response = urlopen(request)
    assert( response.msg == 'OK' )
    assert( response.reason == 'OK' )
    assert( response.status == 200 )

    matt = json.loads(response.read().decode('utf-8'))
    compare = {
      "name": "Fire",
      "effect": [
        {
              "att_strong": ["Bug", "Grass", "Ice", "Steel"],
              "att_weak": ["Dragon", "Fire", "Rock", "Water"],
              "def_strong": ["Bug", "Fairy", "Fire", "Grass", "Ice", "Steel"],
              "def_weak": ["Ground", "Rock", "Water"]
          }
      ],
      "description": "Notable Trainers who specialize in Fire-type Pokémon include Blaine of Cinnabar Island, Flannery of Lavaridge Town, Flint of the Sinnoh Elite Four, Chili of Striaton City, and Malva of the Kalos Elite Four."  }
    assert(compare == matt)

  def test_POST_POKEMON(self):
    data = {'type': ['Grass', 'Poison'], 'name': 'Bulbasaur', 'p_id': 1, 'height': 0.7, 'weight': 6.9, 'location': 'Kanto', 'kind': 'Seed', "description": "Bulbasaur is a small, quadruped Pokémon with green or bluish green skin and dark patches.", "images": ["http://bulbapedia.bulbagarden.net/wiki/File:001Bulbasaur.png"]}
    d = urllib.parse.urlencode(data)
    request = Request("http://helixapi.apiary.io/api/pokemon", d.encode('utf-8'))
    response = urlopen(request)

    assert( response.msg == "Created")
    assert( response.reason == "Created")
    assert( response.status == 201)

  def test_POST_TRAINER(self):
    data = {
      "name": "Red",
      "tr_id": "tra_red",
      "badge": "",
      "location": "Pallet Town",
      "kind": "Master",
      "description": "Main Character of Pokemon Adventures",
      "images": ["http://bulbapedia.bulbagarden.net/wiki/File:Red_Adventures.png"],
      "citations": ["http://bulbapedia.bulbagarden.net/wiki/Red_%28Adventures%29"]  }
    d = urllib.parse.urlencode(data)
    request = Request("http://helixapi.apiary.io/api/trainer", d.encode('utf-8'))
    response = urlopen(request)

    assert( response.msg == "Created")
    assert( response.reason == "Created")
    assert( response.status == 201)

  def test_POST_TYPES(self):
    data = {
      "name": "Fire",
      "effect": [
        {
              "att_strong": ["Bug", "Grass", "Ice", "Steel"],
              "att_weak": ["Dragon", "Fire", "Rock", "Water"],
              "def_strong": ["Bug", "Fairy", "Fire", "Grass", "Ice", "Steel"],
              "def_weak": ["Ground", "Rock", "Water"]
          }
      ],
      "description": "Notable Trainers who specialize in Fire-type Pokémon include Blaine of Cinnabar Island, Flannery of Lavaridge Town, Flint of the Sinnoh Elite Four, Chili of Striaton City, and Malva of the Kalos Elite Four."  }
    d = urllib.parse.urlencode(data)
    request = Request("http://helixapi.apiary.io/api/types", d.encode('utf-8'))
    response = urlopen(request)

    assert( response.msg == "Created")
    assert( response.reason == "Created")
    assert( response.status == 201)

  """
    Converting to Python3 for PUTS
    http://stackoverflow.com/questions/7081488/python-3-x-urllib-request-error
  """
  def test_PUT_POKEMON(self):
    values = {
    "name": "Bulbasaur",
    "height": 0.7,
    "weight": 6.9,
    "location": "Kanto",
    "kind": "Seed",
    "description": "Bulbasaur is a small, quadruped Pokémon with green or bluish green skin and dark patches.",
    "images": ["http://bulbapedia.bulbagarden.net/wiki/File:001Bulbasaur.png"]
}
#    headers = {"Content-Type": "application/json"}
    params = urllib.parse.urlencode(values)
    params = params.encode('utf-8')
    request = Request("http://helixapi.apiary.io/api/pokemon/1", params)
    request.get_method = lambda: 'PUT'
    response = urlopen(request)
    assert( response.msg == "No Content")
    assert( response.reason == "No Content")
    assert( response.status == 204)
    assert( response.read().decode('utf-8') == "" )

  def test_PUT_TRAINER(self):
    values = {
        "name": "Red",
        "tr_id": "tra_red",
        "badge": "",
        "location": "Pallet Town",
        "kind": "Master",
        "description": "Main Character of Pokemon Adventures",
        "images": ["http://bulbapedia.bulbagarden.net/wiki/File:Red_Adventures.png"],
        "citations": ["http://bulbapedia.bulbagarden.net/wiki/Red_%28Adventures%29"]
    }
#    headers = {"Content-Type": "application/json"}
    params = urllib.parse.urlencode(values)
    params = params.encode('utf-8')
    request = Request("http://helixapi.apiary.io/api/trainer/1", params)
    request.get_method = lambda: 'PUT'
    response = urlopen(request)
    assert( response.msg == "No Content")
    assert( response.reason == "No Content")
    assert( response.status == 204)
    assert( response.read().decode('utf-8') == "" )

  def test_PUT_TYPE(self):
    values = {
        "name": "Fire",
        "effect": [
           {
                "att_strong": ["Bug", "Grass", "Ice", "Steel"],
                "att_weak": ["Dragon", "Fire", "Rock", "Water"],
                "def_strong": ["Bug", "Fairy", "Fire", "Grass", "Ice", "Steel"],
                "def_weak": ["Ground", "Rock", "Water"]
            }
        ],
        "description": "Notable Trainers who specialize in Fire-type Pokémon include Blaine of Cinnabar Island, Flannery of Lavaridge Town, Flint of the Sinnoh Elite Four, Chili of Striaton City, and Malva of the Kalos Elite Four."
    }
#    headers = {"Content-Type": "application/json"}
    params = urllib.parse.urlencode(values)
    params = params.encode('utf-8')
    request = Request("http://helixapi.apiary.io/api/types/1", params)
    request.get_method = lambda: 'PUT'
    response = urlopen(request)
    assert( response.msg == "No Content")
    assert( response.reason == "No Content")
    assert( response.status == 204)
    assert( response.read().decode('utf-8') == "" )

  def test_DELETE_POKEMON(self):
    request = Request("http://helixapi.apiary.io/api/pokemon/1")
    request.get_method = lambda: 'DELETE'
    response = urlopen(request)
    response_body = response.read().decode('utf-8')

    assert( response.msg == "No Content" )
    assert( response.reason == "No Content" )
    assert( response.status == 204 )
    assert( response_body == "" )

  def test_DELETE_TRAINER(self):
    request = Request("http://helixapi.apiary.io/api/trainer/1")
    request.get_method = lambda: 'DELETE'
    response = urlopen(request)
    response_body = response.read().decode('utf-8')

    assert( response.msg == "No Content" )
    assert( response.reason == "No Content" )
    assert( response.status == 204 )
    assert( response_body == "" )

  def test_DELETE_TYPE(self):
    request = Request("http://helixapi.apiary.io/api/types/1")
    request.get_method = lambda: 'DELETE'
    response = urlopen(request)
    response_body = response.read().decode('utf-8')

    assert( response.msg == "No Content" )
    assert( response.reason == "No Content" )
    assert( response.status == 204 )
    assert( response_body == "" )

print("TestApiary.py")
unittest.main()
print("Done.")
