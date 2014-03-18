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

	def test_API_get_platforms_response(self) :
		request = Request("http://vgdb.apiary.io/platforms")
		response = urlopen(request)
		self.assertTrue(response.getcode() == 200)