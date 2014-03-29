#!/usr/bin/env python3

# from django.test import TestCase
# # from urllib2 import Request, urlopen #python2
# from urllib.request import urlopen, Request #python3
# from json import dumps, loads

from urllib.request import urlopen
from urllib.request import Request
from json import dumps, loads
import json
import unittest


platinum_games = {
	"id": 1,
	"name": "Platinum Games",
	"date_founded": "8-1-2006",
	"num_employees": 120,
	"status": "Active",
	"image_link": "http://upload.wikimedia.org/wikipedia/en/9/9e/PlatinumGames.png",
	"map_link": "https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=1-1-30+Oyodo-naka,+Kita-ku,+Osaka,+531-6108&amp;aq=&amp;sll=34.704426,135.485297&amp;sspn=0.004397,0.008256&amp;ie=UTF8&amp;hq=&amp;hnear=1+Chome-1-30+%C5%8Cyodonaka,+Kita-ku,+%C5%8Csaka-shi,+%C5%8Csaka-fu,+Japan&amp;ll=34.70533,135.489699&amp;spn=0.035033,0.066047&amp;t=m&amp;z=14&amp;output=embed"
 }

the_wonderful_101 = {
	"id": 1,
	"title": "The Wonderful 101",
	"release_date": "09-15-2013",
	"publisher": "Nintendo",
	"ESRB_rating": "T",
	"genre": "Action",
	"image_link": "http://upload.wikimedia.org/wikipedia/en/e/ee/Wonderful_101_box_artwork.jpg",
	"youtube_link": "//www.youtube.com/embed/bNefE89DZds"
}

wii_u = {
	"id": 1,
	"name": "Wii U",
	"manufacturer": "Nintendo",
	"release_date": "11-18-2012",
	"generation": "Physical (disks) and digital",
	"media_format": 8,
	"image_link": "http://timenerdworld.files.wordpress.com/2012/11/top10_gadgets_wiiu.jpg?w=480&h=320&crop=1",
	"youtube_link": "//www.youtube.com/embed/qhlDHeCT-Q8",
	"twitter_link": "https://twitter.com/wiiudaily"
}





class test_API(unittest.TestCase) :

	# ----------
	# Developers
	# ----------
	def test_API_get_developers(self) :
		request = Request("http://vgdb.apiary-mock.com/api/developers")
		response = urlopen(request)
		
		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == [{"id": platinum_games["id"], "name": platinum_games["name"]}])

	def test_API_post_developers(self) :
		values = dumps(platinum_games).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://vgdb.apiary-mock.com/api/developers", data=values, headers=headers)
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 201)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == {"id": platinum_games["id"], "name": platinum_games["name"]})

	def test_API_get_developer(self) :
		request = Request("http://vgdb.apiary-mock.com/api/developers/platinum_games")
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == platinum_games)

	def test_API_put_developer(self) :
		values = dumps(platinum_games).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://vgdb.apiary-mock.com/api/developers/platinum_games", data=values, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 204)

		response_content = response.read().decode("utf-8")
		self.assertTrue(response_content == "")

	def test_API_delete_developer(self) :
		request = Request("http://vgdb.apiary-mock.com/api/developers/platinum_games")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 204)

		response_content = response.read().decode("utf-8")
		self.assertTrue(response_content == "")

	def test_API_get_developer_games(self) :
		request = Request("http://vgdb.apiary-mock.com/api/developers/platinum_games/games")
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == [the_wonderful_101])

	def test_API_get_developer_platforms(self) :
		request = Request("http://vgdb.apiary-mock.com/api/developers/platinum_games/platforms")
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == [wii_u])


	# --------
	# Platform
	# --------
	def test_API_get_platforms(self) :
		request = Request("http://vgdb.apiary-mock.com/api/platforms")
		response = urlopen(request)
		
		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == [{"id": wii_u["id"], "name": wii_u["name"]}])

	def test_API_post_platforms(self) :
		values = dumps(wii_u).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://vgdb.apiary-mock.com/api/platforms", data=values, headers=headers)
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 201)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == {"id": wii_u["id"], "name": wii_u["name"]})

	def test_API_get_platform(self) :
		request = Request("http://vgdb.apiary-mock.com/api/platforms/wii_u")
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == wii_u)

	def test_API_put_platform(self) :
		values = dumps(wii_u).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://vgdb.apiary-mock.com/api/platforms/wii_u", data=values, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 204)

		response_content = response.read().decode("utf-8")
		self.assertTrue(response_content == "")

	def test_API_delete_platform(self) :
		request = Request("http://vgdb.apiary-mock.com/api/platforms/wii_u")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 204)

		response_content = response.read().decode("utf-8")
		self.assertTrue(response_content == "")

	def test_API_get_platform_developers(self) :
		request = Request("http://vgdb.apiary-mock.com/api/platforms/wii_u/developers")
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == [platinum_games])

	def test_API_get_platform_games(self) :
		request = Request("http://vgdb.apiary-mock.com/api/platforms/wii_u/games")
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == [the_wonderful_101])

	
	# ----
	# Game
	# ----
	def test_API_get_games(self) :
		request = Request("http://vgdb.apiary-mock.com/api/games")
		response = urlopen(request)
		
		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == [{"id": the_wonderful_101["id"], "title": the_wonderful_101["title"]}])

	def test_API_post_games(self) :
		values = dumps(the_wonderful_101).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://vgdb.apiary-mock.com/api/games", data=values, headers=headers)
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 201)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == {"id": the_wonderful_101["id"], "title": the_wonderful_101["title"]})

	def test_API_get_game(self) :
		request = Request("http://vgdb.apiary-mock.com/api/games/the_wonderful_101")
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == the_wonderful_101)

	def test_API_put_game(self) :
		values = dumps(the_wonderful_101).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://vgdb.apiary-mock.com/api/games/the_wonderful_101", data=values, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 204)

		response_content = response.read().decode("utf-8")
		self.assertTrue(response_content == "")

	def test_API_delete_game(self) :
		request = Request("http://vgdb.apiary-mock.com/api/games/the_wonderful_101")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 204)

		response_content = response.read().decode("utf-8")
		self.assertTrue(response_content == "")

	def test_API_get_game_developers(self) :
		request = Request("http://vgdb.apiary-mock.com/api/games/the_wonderful_101/developers")
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == [platinum_games])

	def test_API_get_game_platforms(self) :
		request = Request("http://vgdb.apiary-mock.com/api/games/the_wonderful_101/platforms")
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == [wii_u])


	print("Done")

unittest.main()