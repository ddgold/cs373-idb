from django.test import TestCase
from urllib2 import Request, urlopen
from json import dumps

class test_API(TestCase) :

	# ---
	# get
	# ---
	def test_API_get_game_response(self) :
		request = Request("http://vgdb.apiary.io/developers")
		response = urlopen(request)
		self.assertTrue(True)
