#!/usr/bin/env python3
import datetime
from django.contrib.auth.models import User
from tastypie.test import ResourceTestCase
from idb.models import Platform, Developer, Game
from django.shortcuts import get_object_or_404

admin.autodiscover()
v1_api = Api(api_name='v1')
v1_api.register(PlatformResource())
v1_api.register(DeveloperResource())
v1_api.register(GameResource())


platinum_games = {
	"id": 1,
	"name": "Platinum Games",
	"date_founded": "2006-04-08",
	"num_employees": 120,
	"status": "Active",
	"address": "Umeda Sky Building Tower West 8F,\n1-1-30 Oyodo-naka, Kita-ku, Osaka, 531-6108",
	"map_link": "https://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=1-1-30+Oyodo-naka,+Kita-ku,+Osaka,+531-6108&aq=&sll=34.704426,135.485297&sspn=0.004397,0.008256&ie=UTF8&hq=&hnear=1+Chome-1-30+%C5%8Cyodonaka,+Kita-ku,+%C5%8Csaka-shi,+%C5%8Csaka-fu,+Japan&ll=34.70533,135.489699&spn=0.035033,0.066047&t=m&z=14&output=embed",
	"image_link1": "http://nonspecificaction.co.uk/wp-content/uploads/platinum-games-logo.jpg",
	"image_link2": "http://www.gamechup.com/wp-content/uploads/2014/01/platinum-games-project-nagano.jpg",
	"image_link3": "http://3.bp.blogspot.com/_Z50Ik1LwTlQ/TUAHdjb-3oI/AAAAAAAAEYA/pj5C9fp1ctg/s1600/platgamesega.jpg",
	"platforms": [1]
}

the_wonderful_101 = {
	"id": 1,
	"title": "The Wonderful 101",
	"release_date": "2013-09-15",
	"genre": "Action",
	"publisher": "Nintendo",
	"ESRB_rating": "T",
	"youtube_link": "www.youtube.com/embed/z9ueBmNNGus",
	"image_link1": "http://s11.postimg.org/xjy2jtm6b/the_wonderful_101_logo.png",
	"image_link2": "http://venturebeat.files.wordpress.com/2013/05/the-wonderful-101.jpg",
	"image_link3": "http://stickskills.com/wp-content/uploads/2013/01/The-Wonderful-101.jpg",
	"developer": 1, 
	"platforms":[1]
	}

wii_u = {
	"id": 1,
	"name": "Wii U",
	"manufacturer": "Nintendo",
	"release_date": "2012-11-18",
	"media_format": "Physical (disks) and digital",
	"generation": 8,
	"youtube_link": "http://www.youtube.com/embed/qhlDHeCT-Q8",
	"twitter_link": "446085251077373952",
	"image_link1": "http://g-ecx.images-amazon.com/images/G/01/aplus/detail-page/B009AGXH64hardware.jpg",
	"image_link2": "http://www.dailynintendo.nl/wp-content/uploads/2011/05/wii-u.jpg",
	"image_link3": "http://blogs-images.forbes.com/erikkain/files/2012/11/blackcontroller_big-1.jpg"
}

#----------
# Platforms
#----------
class PlatformResourceTest(ResourceTestCase) :

	fixtures = ['data.json']

<<<<<<< HEAD:tests.py

class test_API(TestCase) :

	# ----------
	# Developers
	# ----------
	def test_API_get_developers(self) :
		request = Request(patterns(r'^api/', include(v1_api.urls)))
=======
	def setUp(self):
		super(PlatformResourceTest, self).setUp()
		
		# Create a user.
		self.username = 'polt'
		self.password = 'masher'
		self.api_key = 'poltergust'
		self.user = User.objects.create_user(self.username, 'poltergust@hotmail.com', self.password)
		
		# chose Game Boy Advance since it is the first alphabetically
		self.platform_1 = Platform.objects.get(name='Game Boy Advance')
		
		self.detail_url = '/api/v1/developer/{0}/'.format(self.platform_1.pk)
		
		self.post_data = {
			'user': '/api/v1/user/{0}/'.format(self.user.pk),
			'title': 'Second Post!',
			'slug': 'second-post',
			'created': '2014-04-03T19:13:42',
		}
		
	def get_api_credentials(self):
		return self.create_apikey(username=self.username, api_key=self.api_key)
        
	def test_get_list_json(self):
		resp = self.api_client.get('/api/v1/platform/', format='json', authentication=self.get_api_credentials())
		self.assertValidJSONResponse(resp)
    	
		self.assertEqual(len(self.deserialize(resp)['objects']), 10)
		
		# compare with Game Boy Advance
		self.assertEqual(self.deserialize(resp)['objects'][0], {
			"id": self.platform_1.pk,
			"name": str(self.platform_1.name),
			"manufacturer": str(self.platform_1.manufacturer),
			"release_date": str(self.platform_1.release_date),
			"media_format": str(self.platform_1.media_format),
			"generation": self.platform_1.generation,
			"youtube_link": str(self.platform_1.youtube_link),
			"twitter_link": str(self.platform_1.twitter_link),
			"image_link1": str(self.platform_1.image_link1),
			"image_link2": str(self.platform_1.image_link2),
			"image_link3": str(self.platform_1.image_link3),
			'resource_uri': '/api/v1/platform/{0}/'.format(self.platform_1.pk)
		})

# ----------
# Developers
# ----------
class DeveloperResourceTest(ResourceTestCase) :

	fixtures = ['data.json']

	def setUp(self):
		super(DeveloperResourceTest, self).setUp()
		
		# Create a user.
		self.username = 'polt'
		self.password = 'masher'
		self.api_key = 'poltergust'
		self.user = User.objects.create_user(self.username, 'poltergust@hotmail.com', self.password)
		
		# chose Cing since it is the first alphabetically
		self.developer_1 = Developer.objects.get(name='Cing')
		
		self.detail_url = '/api/v1/developer/{0}/'.format(self.developer_1.pk)
		
		self.post_data = {
			'user': '/api/v1/user/{0}/'.format(self.user.pk),
			'title': 'Second Post!',
			'slug': 'second-post',
			'created': '2014-04-03T19:13:42',
		}
		
	def get_api_credentials(self):
		return self.create_apikey(username=self.username, api_key=self.api_key)
		
	#def test_get_list_unauthorzied(self):
		#self.assertHttpUnauthorized(self.api_client.get('/api/v1/developer/', format='json'))
        
	def test_get_list_json(self):
		resp = self.api_client.get('/api/v1/developer/', format='json', authentication=self.get_api_credentials())
		self.assertValidJSONResponse(resp)
    	
		self.assertEqual(len(self.deserialize(resp)['objects']), 10)
		
		# compare with Cing
		self.assertEqual(self.deserialize(resp)['objects'][0], {
			"id": self.developer_1.pk,
			"name": str(self.developer_1.name),
			"date_founded": str(self.developer_1.date_founded),
			"num_employees": self.developer_1.num_employees,
			"status": str(self.developer_1.status),
			"address": str(self.developer_1.address),
			"map_link": str(self.developer_1.map_link),
			"image_link1": str(self.developer_1.image_link1),
			"image_link2": str(self.developer_1.image_link2),
			"image_link3": str(self.developer_1.image_link3),
			"platforms": ['/api/v1/platform/{0}/'.format(o.pk) for o in self.developer_1.platforms.all()],
			'resource_uri': '/api/v1/developer/{0}/'.format(self.developer_1.pk)
		})

#------
# Games
#------
class GameResourceTest(ResourceTestCase) :

	fixtures = ['data.json']

	def setUp(self):
		super(GameResourceTest, self).setUp()
		
		# Create a user.
		self.username = 'polt'
		self.password = 'masher'
		self.api_key = 'poltergust'
		self.user = User.objects.create_user(self.username, 'poltergust@hotmail.com', self.password)
		
		# chose Call of Duty 4: Modern Warfare since it is the first alphabetically
		self.game_1 = Game.objects.get(title='Call of Duty 4: Modern Warfare')
		
		self.detail_url = '/api/v1/game/{0}/'.format(self.game_1.pk)
		
		self.post_data = {
			'user': '/api/v1/user/{0}/'.format(self.user.pk),
			'title': 'Second Post!',
			'slug': 'second-post',
			'created': '2014-04-03T19:13:42',
		}
		
	def get_api_credentials(self):
		return self.create_apikey(username=self.username, api_key=self.api_key)
		
	#def test_get_list_unauthorzied(self):
		#self.assertHttpUnauthorized(self.api_client.get('/api/v1/game/', format='json'))
        
	def test_get_list_json(self):
		resp = self.api_client.get('/api/v1/game/', format='json', authentication=self.get_api_credentials())
		self.assertValidJSONResponse(resp)
    	
		self.assertEqual(len(self.deserialize(resp)['objects']), 10)
		
		# compare with Call of Duty 4: Modern Warfare
		self.assertEqual(self.deserialize(resp)['objects'][0], {
			"id": self.game_1.pk,
			"title": str(self.game_1.title),
			"release_date": str(self.game_1.release_date),
			"genre": str(self.game_1.genre),
			"publisher": str(self.game_1.publisher),
			"ESRB_rating": str(self.game_1.ESRB_rating),
			"youtube_link": str(self.game_1.youtube_link),
			"image_link1": str(self.game_1.image_link1),
			"image_link2": str(self.game_1.image_link2),
			"image_link3": str(self.game_1.image_link3),
			'developer': '/api/v1/developer/{0}/'.format(self.game_1.developer.pk),
			'platforms': ['/api/v1/platform/{0}/'.format(o.pk) for o in self.game_1.platforms.all()],
			'resource_uri': '/api/v1/game/{0}/'.format(self.game_1.pk)
		})

	"""def test_API_get_developers(self) :
		request = Request("api/v1/developer")
>>>>>>> 4d57705368158afa39a9397d1d3947c502467771:polt-tests.py
		response = urlopen(request)
		
		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		print(response_content + "\n\n\n\n")
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
		self.assertTrue(response_content == platinum_games)

	def test_API_get_game_platforms(self) :
		request = Request("http://vgdb.apiary-mock.com/api/games/the_wonderful_101/platforms")
		response = urlopen(request)

		response_code = response.getcode()
		self.assertTrue(response_code == 200)

		response_content = loads(response.read().decode("utf-8"))
		self.assertTrue(response_content == [wii_u]) """


	print("Done")
