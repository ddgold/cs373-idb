from django.test import TestCase
from urllib2 import Request, urlopen
from json import dumps, loads

class test_API(TestCase) :

	# ---
	# get
	# ---
	def test_API_get_developers_response(self) :
		request = Request("http://vgdb.apiary.io/developers")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_developers_object_response(self) :
		request = Request("http://vgdb.apiary.io/developers/platinum_games")
		response_body = urlopen(request).read().decode("utf-8")
		response = loads(response_body)
		print(response_body)
		#self.assertTrue(response.getcode() == 200)

	def test_API_get_developers_object_games_response(self) :
		request = Request("http://vgdb.apiary.io/developers/platinum_games/games")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_developers_object_platforms_response(self) :
		request = Request("http://vgdb.apiary.io/developers/platinum_games/platforms")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_games_response(self) :
		request = Request("http://vgdb.apiary.io/games")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_games_object_response(self) :
		request = Request("http://vgdb.apiary.io/games/the_wonderful_101")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_games_object_developers_response(self) :
		request = Request("http://vgdb.apiary.io/games/the_wonderful_101/developers")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_games_object_platforms_response(self) :
		request = Request("http://vgdb.apiary.io/games/the_wonderful_101/platforms")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_platforms_response(self) :
		request = Request("http://vgdb.apiary.io/platforms")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_platforms_object_response(self) :
		request = Request("http://vgdb.apiary.io/platforms/wii_u")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_platforms_object_developers_response(self) :
		request = Request("http://vgdb.apiary.io/platforms/wii_u/developers")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)

	def test_API_get_platforms_object_games_response(self) :
		request = Request("http://vgdb.apiary.io/platforms/wii_u/games")
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

	# ---
	# delete
	# ---

	def test_API_delete_platform(self):
		request = Request("http://vgdb.apiary.io/platforms/wii_u")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)
		self.assertTrue(response.getcode() == 204)
		
	def test_API_delete_game(self):
		request = Request("http://vgdb.apiary.io/platforms/wonderful_101")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)
		self.assertTrue(response.getcode() == 204)
		
	def test_API_delete_developer(self):
		request = Request("http://vgdb.apiary.io/platforms/platinum_games")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)
		self.assertTrue(response.getcode() == 204)
