#!/usr/bin/env python3
import datetime
from django.contrib.auth.models import User
from tastypie.test import ResourceTestCase
from idb.models import Platform, Developer, Game
from django.shortcuts import get_object_or_404


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

	def setUp(self):
		super(PlatformResourceTest, self).setUp()
		
		# Create a user.
		self.username = 'polt'
		self.password = 'masher'
		self.api_key = 'poltergust'
		self.user = User.objects.create_user(self.username, 'poltergust@hotmail.com', self.password)
		
		# chose Game Boy Advance since it is the first alphabetically
		self.platform_1 = Platform.objects.get(name='Game Boy Advance')
		
		self.detail_url = '/api/v1/platform/{0}/'.format(self.platform_1.pk)
		
		self.post_data = {
			"id": 11,
			"name": "Genesis",
			"manufacturer": "Sega",
			"release_date": "1991-06-17",
			"media_format": "Physical (cartridge)",
			"generation": 4,
			"youtube_link": "http://www.youtube.com/embed/qhlDHeCT-Q8",
			"twitter_link": "446085251077373952",
			"image_link1": "http://g-ecx.images-amazon.com/images/G/01/aplus/detail-page/B009AGXH64hardware.jpg",
			"image_link2": "http://www.dailynintendo.nl/wp-content/uploads/2011/05/wii-u.jpg",
			"image_link3": "http://blogs-images.forbes.com/erikkain/files/2012/11/blackcontroller_big-1.jpg",
			"resource_uri": '/api/v1/platform/11/'
		}
		
	def get_credentials(self):
		return self.create_apikey(username=self.username, api_key=self.api_key)
        
	def test_get_list_json(self):
		resp = self.api_client.get('/api/v1/platform/', format='json', authentication=self.get_credentials())
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
			"resource_uri": '/api/v1/platform/{0}/'.format(self.platform_1.pk)
		})
		
	def test_get_detail_json(self):
		resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
		self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
		self.assertKeys(self.deserialize(resp), ['generation', 'id', 'image_link1', 'image_link2', 'image_link3', 'manufacturer', 'media_format', 'name', 'release_date', 'resource_uri', 'twitter_link', 'youtube_link'])
		self.assertEqual(self.deserialize(resp)['name'], str(self.platform_1.name))
		
	def test_post_list(self):
        # Check how many are there first.
		self.assertEqual(Platform.objects.count(), 10)
		self.assertHttpCreated(self.api_client.post('/api/v1/platform/', format='json', data=self.post_data, authentication=self.get_credentials()))
        # Verify a new one has been added.
		self.assertEqual(Platform.objects.count(), 11)
		
	def test_put_detail(self):
		# Grab the current data & modify it slightly.
		original_data = self.deserialize(self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials()))
		new_data = original_data.copy()
		new_data['name'] = 'Updated: Game Boy Advance'

		self.assertEqual(Platform.objects.count(), 10)
		self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data, authentication=self.get_credentials()))
		
		# Make sure the count hasn't changed & we did an update.
		self.assertEqual(Platform.objects.count(), 10)
		# Check for updated data.
		self.assertEqual(Platform.objects.get(pk=5).name, 'Updated: Game Boy Advance')
		self.assertEqual(Platform.objects.get(pk=5).manufacturer, 'Nintendo')
		
	def test_delete_detail(self):
		self.assertEqual(Platform.objects.count(), 10)
		self.assertHttpAccepted(self.api_client.delete(self.detail_url, format='json', authentication=self.get_credentials()))
		self.assertEqual(Platform.objects.count(), 9)

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
			"id": 11,
			"name": "Sega",
			"date_founded": "1987-02-23",
			"num_employees": 324,
			"status": "Active",
			"address": "Tokyo, Japan",
			"map_link": "https://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=1-1-30+Oyodo-naka,+Kita-ku,+Osaka,+531-6108&aq=&sll=34.704426,135.485297&sspn=0.004397,0.008256&ie=UTF8&hq=&hnear=1+Chome-1-30+%C5%8Cyodonaka,+Kita-ku,+%C5%8Csaka-shi,+%C5%8Csaka-fu",
			"image_link1": "http://nonspecificaction.co.uk/wp-content/uploads/platinum-games-logo.jpg",
			"image_link2": "http://www.gamechup.com/wp-content/uploads/2014/01/platinum-games-project-nagano.jpg",
			"image_link3": "http://3.bp.blogspot.com/_Z50Ik1LwTlQ/TUAHdjb-3oI/AAAAAAAAEYA/pj5C9fp1ctg/s1600/platgamesega.jpg",
			"platforms": ['/api/v1/platform/{0}/'.format(Platform.objects.get(pk=1).pk), '/api/v1/platform/{0}/'.format(Platform.objects.get(pk=6).pk)],
			'resource_uri': '/api/v1/developer/11/'
		}
		
	def get_credentials(self):
		return self.create_apikey(username=self.username, api_key=self.api_key)
		
	#def test_get_list_unauthorzied(self):
		#self.assertHttpUnauthorized(self.api_client.get('/api/v1/developer/', format='json'))
        
	def test_get_list_json(self):
		resp = self.api_client.get('/api/v1/developer/', format='json', authentication=self.get_credentials())
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
		
	def test_get_detail_json(self):
		resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
		self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
		self.assertKeys(self.deserialize(resp), ['address', 'date_founded', 'id', 'image_link1', 'image_link2', 'image_link3', 'map_link', 'name', 'num_employees', 'platforms', 'resource_uri', 'status'])
		self.assertEqual(self.deserialize(resp)['name'], str(self.developer_1.name))
		
	def test_post_list(self):
        # Check how many are there first.
		self.assertEqual(Developer.objects.count(), 10)
		self.assertHttpCreated(self.api_client.post('/api/v1/developer/', format='json', data=self.post_data, authentication=self.get_credentials()))
        # Verify a new one has been added.
		self.assertEqual(Developer.objects.count(), 11)
		
	def test_put_detail(self):
		# Grab the current data & modify it slightly.
		original_data = self.deserialize(self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials()))
		new_data = original_data.copy()
		new_data['name'] = 'Updated: Cing'

		self.assertEqual(Developer.objects.count(), 10)
		self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data, authentication=self.get_credentials()))
		
		# Make sure the count hasn't changed & we did an update.
		self.assertEqual(Developer.objects.count(), 10)
		# Check for updated data.
		self.assertEqual(Developer.objects.get(pk=3).name, 'Updated: Cing')
		self.assertEqual(Developer.objects.get(pk=3).status, 'Defunct')
		
	def test_delete_detail(self):
		self.assertEqual(Developer.objects.count(), 10)
		self.assertHttpAccepted(self.api_client.delete(self.detail_url, format='json', authentication=self.get_credentials()))
		self.assertEqual(Developer.objects.count(), 9)

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
			"id": 11,
			"title": "Bayonetta",
			"release_date": "2010-07-12",
			"genre": "Action",
			"publisher": "Sega",
			"ESRB_rating": "M",
			"youtube_link": "www.youtube.com/embed/z9ueBmNNGus",
			"image_link1": "http://s11.postimg.org/xjy2jtm6b/the_wonderful_101_logo.png",
			"image_link2": "http://venturebeat.files.wordpress.com/2013/05/the-wonderful-101.jpg",
			"image_link3": "http://stickskills.com/wp-content/uploads/2013/01/The-Wonderful-101.jpg",
			'developer': '/api/v1/developer/{0}/'.format(Developer.objects.get(pk=1).pk),
			'platforms': ['/api/v1/platform/{0}/'.format(Platform.objects.get(pk=2).pk), '/api/v1/platform/{0}/'.format(Platform.objects.get(pk=10).pk)],
			'resource_uri': '/api/v1/game/11/'
		}
		
	def get_credentials(self):
		return self.create_apikey(username=self.username, api_key=self.api_key)
		
	#def test_get_list_unauthorzied(self):
		#self.assertHttpUnauthorized(self.api_client.get('/api/v1/game/', format='json'))
        
	def test_get_list_json(self):
		resp = self.api_client.get('/api/v1/game/', format='json', authentication=self.get_credentials())
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
		
	def test_get_detail_json(self):
		resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
		self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
		self.assertKeys(self.deserialize(resp), ['developer', 'ESRB_rating', 'genre', 'id', 'image_link1', 'image_link2', 'image_link3', 'platforms', 'publisher', 'release_date', 'resource_uri', 'title', 'youtube_link'])
		self.assertEqual(self.deserialize(resp)['title'], str(self.game_1.title))
		
	def test_post_list(self):
        # Check how many are there first.
		self.assertEqual(Game.objects.count(), 10)
		self.assertHttpCreated(self.api_client.post('/api/v1/game/', format='json', data=self.post_data, authentication=self.get_credentials()))
        # Verify a new one has been added.
		self.assertEqual(Game.objects.count(), 11)
		
	def test_put_detail(self):
		# Grab the current data & modify it slightly.
		original_data = self.deserialize(self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials()))
		new_data = original_data.copy()
		new_data['title'] = 'Updated: Call of Duty 4: Modern Warfare'

		self.assertEqual(Game.objects.count(), 10)
		self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data, authentication=self.get_credentials()))
		
		# Make sure the count hasn't changed & we did an update.
		self.assertEqual(Game.objects.count(), 10)
		# Check for updated data.
		self.assertEqual(Game.objects.get(pk=2).title, 'Updated: Call of Duty 4: Modern Warfare')
		self.assertEqual(Game.objects.get(pk=2).genre, 'First-person shooting')
		
	def test_delete_detail(self):
		self.assertEqual(Game.objects.count(), 10)
		self.assertHttpAccepted(self.api_client.delete(self.detail_url, format='json', authentication=self.get_credentials()))
		self.assertEqual(Game.objects.count(), 9)


print("Done")
