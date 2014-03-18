from django.test import TestCase
from urllib2 import Request, urlopen
from json import dumps

class test_API(TestCase) :

	# ---
	# get
	# ---
	def test_API_get_developers_response(self) :
		request = Request("http://vgdb.apiary.io/developers")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_games_response(self) :
		request = Request("http://vgdb.apiary.io/games")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_games_title_response(self) :
		request = Request("http://vgdb.apiary.io/game/the_wonderful_101")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)


	def test_API_get_platforms_response(self) :
		request = Request("http://vgdb.apiary.io/platforms")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)


	# ---
	# post
	# ---

	def test_API_post_developers_response(self):

		values = dumps([{
		    'name': 'Platinum Games',
		    'date_founded': 2006,
		    'num_employees': 120,
		    'status': 'Active'
		}])

		headers = {"Content-Type": "application/json"}
		request = Request("http://vgdb.apiary.io/developers", data=values, headers=headers)
		response = urlopen(request)
		self.assertTrue(response.getcode() == 201)

	def test_API_post_platforms_response(self):
		values = dumps([{
		    'name': 'Wii U',
		    'manufacturer': 'Nintendo',
		    'release_date': 11-18-2012,
		    'generation': 'Physical (disks) and digital',
		    'media_format': 8
		}])
		headers = {"Content-Type": "application/json"}
		request = Request("http://vgdb.apiary.io/platforms", data=values, headers=headers)
		response = urlopen(request)
		self.assertTrue(response.getcode() == 201)

	def test_API_post_games_response(self):
		values = dumps([{
		    'title': 'The Wonderful 101',
		    'release_date': 9-15-2013,
		    'publisher': 'Nintendo',
		    'ESRB_rating': 'T',
		    'genre': 'Action'
		}])
		headers = {"Content-Type": "application/json"}
		request = Request("http://vgdb.apiary.io/games", data=values, headers=headers)
		response = urlopen(request)
		self.assertTrue(response.getcode() == 201)

	# ---
	# put
	# ---
	def test_API_put_platforms(self):
		request = Request("http://vgdb.apiary.io/platforms/wii_u")
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		self.assertTrue(response.getcode() == 204)

	def test_API_put_game(self):
		request = Request("http://vgdb.apiary.io/game/the_wonderful_101")
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		self.assertTrue(response.getcode() == 204)

	def test_API_put_developer(self):
		request = Request("http://vgdb.apiary.io/developers/platinum_games")
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		self.assertTrue(response.getcode() == 204)