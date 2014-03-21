#!/usr/bin/env python

from urllib2 import Request, urlopen
from json import dumps, loads
import unittest

def verify_console(response_body):
	return response_body["name"] == "Xbox 360" and \
		response_body["id"] == 1 and \
		response_body["description"] == "A video game console developed by Microsoft, and is the successor to the original Xbox, and it is the second console in the Xbox series." and \
		response_body["release_date"] == "2005-11-22" and \
		"Microsoft" in response_body["developers"] and \
		response_body["cpu"] == "3.2 GHz PowerPC Tri-Core Xenon" and \
		response_body["memory"] == "512 MB of GDDR3 RAM clocked at 700 MHz" and \
		response_body["storage"] == "HDD" and \
		response_body["graphics"] == "500 MHz ATI Xenos" and \
		response_body["image_url"] == "http://upload.wikimedia.org/wikipedia/commons/0/03/Xbox-360-Consoles-Infobox.png" and \
		"https://www.youtube.com/embed/AZYhri2tsM4" in response_body["videos"] and \
		1 in response_body["games"] and \
		1 in response_body["studios"] and \
		1 in response_body["articles"] and \
		"http://en.wikipedia.org/wiki/Xbox_360" in response_body["citations"] and \
		"http://www.xbox.com/en-US/" in response_body["external_link"] 

def verify_studio(response_body):
	return response_body["name"] == "Rockstar North" and \
		response_body["id"] == 1 and \
		response_body["date_of_birth"] == "2002-MM-DD" and \
		response_body["location"] == "Edinburgh, Scotland, UK" and \
		response_body["description"] == "Best known for creating the Grand Theft Auto franchises" and \
		response_body["image_url"] == "http://upload.wikimedia.org/wikipedia/en/2/24/Rockstar_North_logo.svg" and \
		"https://www.youtube.com/embed/67nY8w5sCkk" in response_body["videos"] and \
		"http://goo.gl/maps/7g8kX" in response_body["maps"] and \
		response_body["handle"] == "RockstarGames" and \
		response_body["widget_id"] == "000000000000000000" and \
		1 in response_body["games"] and \
		1 in response_body["consoles"] and \
		"http://www.rockstarnorth.com/" in response_body["external_link"] and \
		"http://en.wikipedia.org/wiki/Rockstar_North" in response_body["citations"] and \
		1 in response_body["articles"]

def verify_game(response_body):
	return response_body["name"] == "Grand Theft Auto V" and \
		response_body["id"] == 1 and \
		response_body["genre"] == 1 and \
		response_body["publish_date"] == "2013-09-17" and \
		response_body["description"] == "Free roam sandbox mayhem creation game" and \
		response_body["image_url"] == "http://images.eurogamer.net/2013/usgamer/GTA-V-big.jpg" and \
		"http://www.youtube.com/embed/N-xHcvug3WI" in response_body["videos"] and \
		response_body["handle"] == "RockstarGTAV" and \
		response_body["widget_id"] == "445748828545630209" and \
		1 in response_body["consoles"] and \
		1 in response_body["studios"] and \
		"http://www.rockstargames.com/V/" in response_body["external_link"] and \
		"http://en.wikipedia.org/wiki/Grand_Theft_Auto_V" in response_body["citation"] and \
		1 in response_body["articles"]
class TestAPI(unittest.TestCase):
	# Game endpoint tests
	def test_get_all_games(self):
		request = Request("http://expansionpakmen.apiary.io/api/games")
		response_body = loads(urlopen(request).read())[0]
		self.assertTrue(response_body["name"] == "Grand Theft Auto V")
		self.assertTrue(response_body["id"] == 1)
	
	def test_get_single_game(self):
		request = Request("http://expansionpakmen.apiary.io/api/games/{id}")
		response_body = loads(urlopen(request).read())
		self.assertTrue(verify_game(response_body))
		
	def test_get_studios_for_single_game(self):
		request = Request("http://expansionpakmen.apiary.io/api/games/{id}/studios")
		response_body = loads(urlopen(request).read())[0]
		self.assertTrue(verify_studio(response_body))
		
	def test_get_consoles_for_single_game(self):
		request = Request("http://expansionpakmen.apiary.io/api/games/{id}/consoles")
		response_body = loads(urlopen(request).read())[0]
		self.assertTrue(verify_console(response_body))	

	def test_post_single_game(self):
		values = dumps({
		    "name": "Grand Theft Auto V",
		    "id": 1,
		    "genre": 1,
		    "publish_date": "2013-09-17",
		    "description": "Free roam sandbox mayhem creation game",
		    "image_url": "http://images.eurogamer.net/2013/usgamer/GTA-V-big.jpg",
		    "videos": ["http://www.youtube.com/embed/N-xHcvug3WI"],
		    "handle": "RockstarGTAV", 
		    "widget_id": "445748828545630209",
		    "consoles": [1],
		    "studios": [1],
		    "external_link": ["http://www.rockstargames.com/V/"],
		    "citation": ["http://en.wikipedia.org/wiki/Grand_Theft_Auto_V"],
		    "articles": [1]
		})
		headers = {"Content-Type": "application/json"}
		request = Request("http://expansionpakmen.apiary.io/api/games", data=values, headers=headers)
		response_body = urlopen(request).read()
		self.assertTrue(response_body == '{ id: 1 }')

	def test_put_single_game(self):
		values = dumps({
		    "name": "Grand Theft Auto V",
		    "id": 1,
		    "genre": 1,
		    "publish_date": "2013-09-17",
		    "description": "Free roam sandbox mayhem creation game",
		    "image_url": "http://images.eurogamer.net/2013/usgamer/GTA-V-big.jpg",
		    "videos": ["http://www.youtube.com/embed/N-xHcvug3WI"],
		    "handle": "RockstarGTAV", 
		    "widget_id": "445748828545630209",
		    "consoles": [1],
		    "studios": [1],
		    "external_link": ["http://www.rockstargames.com/V/"],
		    "citation": ["http://en.wikipedia.org/wiki/Grand_Theft_Auto_V"],
		    "articles": [1]
		})
		headers = {"Content-Type": "application/json"}
		request = Request("http://expansionpakmen.apiary.io/api/games/{id}", data=values, headers=headers)
		request.get_method = lambda: 'PUT'
		response_body = urlopen(request).read()
		self.assertTrue(response_body == '')

	def test_delete_single_game(self):
		request = Request("http://expansionpakmen.apiary.io/api/games/{id}")
		request.get_method = lambda: 'DELETE'
		response_body = urlopen(request).read()
		self.assertTrue(response_body == '')


	# Studio endpoint tests
	def test_get_all_studios(self):
		request = Request("http://expansionpakmen.apiary.io/api/studios")
		response_body = loads(urlopen(request).read())[0]
		self.assertTrue(response_body["name"] == "Rockstar North")
		self.assertTrue(response_body["id"] == 1)
	
	def test_get_single_studio(self):
		request = Request("http://expansionpakmen.apiary.io/api/studios/{id}")
		response_body = loads(urlopen(request).read())
		self.assertTrue(verify_studio(response_body))

	def test_get_games_for_single_studio(self):
		request = Request("http://expansionpakmen.apiary.io/api/studios/{id}/games")
		response_body = loads(urlopen(request).read())[0]
		self.assertTrue(verify_game(response_body))

	def test_get_consoles_for_single_studio(self):
		request = Request("http://expansionpakmen.apiary.io/api/studios/{id}/consoles")
		response_body = loads(urlopen(request).read())[0]
		self.assertTrue(verify_console(response_body))
	
	def test_post_single_studio(self):
		values = dumps({
		    "name": "Rockstar North",
		    "id": 1,
		    "date_of_birth": "2002-MM-DD",
		    "location": "Edinburgh, Scotland, UK",
		    "description": "Best known for creating the Grand Theft Auto franchises",
		    "image_url": "http://upload.wikimedia.org/wikipedia/en/2/24/Rockstar_North_logo.svg",
		    "videos": ["https://www.youtube.com/embed/67nY8w5sCkk"],
		    "maps": ["http://goo.gl/maps/7g8kX"],
		    "handle": "RockstarGames",
		    "widget_id": "000000000000000000",
		    "games": [1],
		    "consoles": [1],
		    "external_link": ["http://www.rockstarnorth.com/"],
		    "citations": ["http://en.wikipedia.org/wiki/Rockstar_North"],
		    "articles": [1]
		})
		headers = {"Content-Type": "application/json"}
		request = Request("http://expansionpakmen.apiary.io/api/studios", data=values, headers=headers)
		response_body = urlopen(request).read()
		self.assertTrue(response_body == '{ id: 1 }')
	
	def test_put_single_studio(self):
		values = dumps({
	        "name": "Rockstar North",
		    "id": 1,
		    "date_of_birth": "2002-MM-DD",
		    "location": "Edinburgh, Scotland, UK",
		    "description": "Best known for creating the Grand Theft Auto franchises",
		    "image_url": "http://upload.wikimedia.org/wikipedia/en/2/24/Rockstar_North_logo.svg",
		    "videos": ["https://www.youtube.com/embed/67nY8w5sCkk"],
		    "maps": ["http://goo.gl/maps/7g8kX"],
		    "handle": "RockstarGames",
		    "widget_id": "000000000000000000",
		    "games": [1],
		    "consoles": [1],
		    "external_link": ["http://www.rockstarnorth.com/"],
		    "citations": ["http://en.wikipedia.org/wiki/Rockstar_North"],
		    "articles": [1]
		})
		headers = {"Content-Type": "application/json"}
		request = Request("http://expansionpakmen.apiary.io/api/studios/{id}", data=values, headers=headers)
		request.get_method = lambda: 'PUT'
		response_body = urlopen(request).read()
		self.assertTrue(response_body == '')
	
	def test_delete_single_studio(self):
		request = Request("http://expansionpakmen.apiary.io/api/games/{id}")
		request.get_method = lambda: 'DELETE'
		response_body = urlopen(request).read()
		self.assertTrue(response_body == '')

	# Console endpoint tests
	def test_get_all_consoles(self):
		request = Request("http://expansionpakmen.apiary.io/api/consoles")
		response_body = loads(urlopen(request).read())[0]
		self.assertTrue(response_body["name"] == "Xbox 360")
		self.assertTrue(response_body["id"] == 1)
	
	def test_get_single_console(self):
		request = Request("http://expansionpakmen.apiary.io/api/consoles/{id}")
		response_body = loads(urlopen(request).read())
		self.assertTrue(verify_console(response_body))

	def test_get_games_for_single_console(self):
		request = Request("http://expansionpakmen.apiary.io/api/consoles/{id}/games")
		response_body = loads(urlopen(request).read())[0]
		self.assertTrue(verify_game(response_body))

	def test_get_studios_for_single_console(self):
		request = Request("http://expansionpakmen.apiary.io/api/consoles/{id}/studios")
		response_body = loads(urlopen(request).read())[0]
		self.assertTrue(verify_studio(response_body))
	
	def test_post_single_console(self):
		values = dumps({
		    "name": "Xbox 360",
		    "id": 1,
		    "description": "A video game console developed by Microsoft, and is the successor to the original Xbox, and it is the second console in the Xbox series.",
		    "release_date": "2005-11-22",
		    "developers": ["Microsoft"],
		    "cpu": 	"3.2 GHz PowerPC Tri-Core Xenon",
		    "memory": "512 MB of GDDR3 RAM clocked at 700 MHz",
		    "storage": "HDD",
		    "graphics": "500 MHz ATI Xenos",
		    "image_url": "http://upload.wikimedia.org/wikipedia/commons/0/03/Xbox-360-Consoles-Infobox.png",
		    "videos": ["https://www.youtube.com/embed/AZYhri2tsM4"],
		    "games": [1],
		    "studios": [1],
		    "citations": ["http://en.wikipedia.org/wiki/Xbox_360"],
		    "external_link": ["http://www.xbox.com/en-US/"],
		    "articles": [1]
		})
		headers = {"Content-Type": "application/json"}
		request = Request("http://expansionpakmen.apiary.io/api/consoles", data=values, headers=headers)
		response_body = urlopen(request).read()
		self.assertTrue(response_body == '{ id: 1 }')
	
	def test_put_single_console(self):
		values = dumps({
		    "name": "Xbox 360",
		    "id": 1,
		    "description": "A video game console developed by Microsoft, and is the successor to the original Xbox, and it is the second console in the Xbox series.",
		    "release_date": "2005-11-22",
		    "developers": ["Microsoft"],
		    "cpu": 	"3.2 GHz PowerPC Tri-Core Xenon",
		    "memory": "512 MB of GDDR3 RAM clocked at 700 MHz",
		    "storage": "HDD",
		    "graphics": "500 MHz ATI Xenos",
		    "image_url": "http://upload.wikimedia.org/wikipedia/commons/0/03/Xbox-360-Consoles-Infobox.png",
		    "videos": ["https://www.youtube.com/embed/AZYhri2tsM4"],
		    "games": [1],
		    "studios": [1],
		    "citations": ["http://en.wikipedia.org/wiki/Xbox_360"],
		    "external_link": ["http://www.xbox.com/en-US/"],
		    "articles": [1]
		})
		headers = {"Content-Type": "application/json"}
		request = Request("http://expansionpakmen.apiary.io/api/consoles/{id}", data=values, headers=headers)
		request.get_method = lambda: 'PUT'
		response_body = urlopen(request).read()
		self.assertTrue(response_body == '')

	def test_delete_single_console(self):
		request = Request("http://expansionpakmen.apiary.io/api/consoles/{id}")
		request.get_method = lambda: 'DELETE'
		response_body = urlopen(request).read()
		self.assertTrue(response_body == '')

print ("ExpansionPakmen-tests.py")
unittest.main()
print("Done.")
