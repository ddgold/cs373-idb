#!/usr/bin/env python3
import datetime
from django.contrib.auth.models import User
from tastypie.test import ResourceTestCase
from idb.models import Image, Platform, Developer, Game
from django.test import TestCase
from django.test.client import Client
from json import dumps, loads

image = {
	"description": "Testing",
	"link": "http://i.walmartimages.com/i/p/00/04/54/96/88/0004549688085_500X500.jpg",
}

platinum_games = {
    "name": "Platinum Games",
    "date_founded": "2006-04-08",
    "num_employees": 120,
    "status": "Active",
    "address": "Umeda Sky Building Tower West 8F,\n1-1-30 Oyodo-naka, Kita-ku, Osaka, 531-6108",
    "map_link": "https://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=1-1-30+Oyodo-naka,+Kita-ku,+Osaka,+531-6108&aq=&sll=34.704426,135.485297&sspn=0.004397,0.008256&ie=UTF8&hq=&hnear=1+Chome-1-30+%C5%8Cyodonaka,+Kita-ku,+%C5%8Csaka-shi,+%C5%8Csaka-fu,+Japan&ll=34.70533,135.489699&spn=0.035033,0.066047&t=m&z=14&output=embed",
    "images": ["/api/v1/image/52/", "/api/v1/image/53/", "/api/v1/image/54/"],
    "platforms": ["/api/v1/platform/1/"],
}

the_wonderful_101 = {
    "title": "The Wonderful 101",
    "release_date": "2013-09-15",
    "genre": "Action",
    "publisher": "Nintendo",
    "ESRB_rating": "T",
    "youtube_link": "www.youtube.com/embed/z9ueBmNNGus",
    "images": ["/api/v1/image/109/", "/api/v1/image/110/", "/api/v1/image/110/"],
    "developer": "/api/v1/developer/1/",
    "platforms":["/api/v1/platform/1/"],
}

wii_u = {
    "name": "Wii U",
    "manufacturer": "Nintendo",
    "release_date": "2012-11-18T00:00:00",
    "media_format": "Physical (disks) and digital",
    "generation": 8,
    "youtube_link": "http://www.youtube.com/embed/qhlDHeCT-Q8",
    "twitter_link": "446085251077373952",
    "images": ["/api/v1/image/1/", "/api/v1/image/2/", "/api/v1/image/3/"],
}


class test_main(TestCase) :
	fixtures = ["data.json"]
	def setUp(self):
		self.client = Client();

	def test_get_main(self) :
		response = self.client.get("/api/v1/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 4)
		self.assertEqual(response_content["platform"]["list_endpoint"], "/api/v1/platform/")
		self.assertEqual(response_content["game"]["list_endpoint"], "/api/v1/game/")
		self.assertEqual(response_content["developer"]["list_endpoint"], "/api/v1/developer/")

	def test_get_404(self) :
		response = self.client.get("/api/v1/bad_address/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

		response_content = response.content.decode("utf-8")
		self.assertEqual(response_content[4:13], "Not Found")

	def test_post_404(self) :
		values = dumps(wii_u).encode("utf-8")
		headers = "application/json"
		response = self.client.post("/api/v1/bad_address/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

		response_content = response.content.decode("utf-8")
		self.assertEqual(response_content[4:13], "Not Found")

	def test_put_404(self) :
		values = dumps(wii_u).encode("utf-8")
		headers = "application/json"
		response = self.client.put("/api/v1/bad_address/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

		response_content = response.content.decode("utf-8")
		self.assertEqual(response_content[4:13], "Not Found")

	def test_delete_404(self) :
		response = self.client.delete("/api/v1/bad_address/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

		response_content = response.content.decode("utf-8")
		self.assertEqual(response_content[4:13], "Not Found")



class test_image(TestCase) :
	fixtures = ["data.json"]
	def setUp(self):
		self.client = Client();

	def test_get_all_image(self) :
		response = self.client.get("/api/v1/image/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(response_content["meta"]["total_count"], 177)
		self.assertEqual(response_content["objects"][0]["link"], "http://images.wikia.com/elderscrolls/images/archive/a/a2/20110812152931!Bethesda_game_studios_logo.jpg")
		self.assertEqual(response_content["objects"][17]["link"], "http://i.imgur.com/orPseLp.jpg")

	def test_post_image(self) :
		values = dumps(image).encode("utf-8")
		headers = "application/json"
		response = self.client.post("/api/v1/image/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 201)

	def test_API_get_single_image(self) :
		response = self.client.get("/api/v1/image/1/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 4)
		self.assertEqual(response_content["id"], 1)
		self.assertEqual(response_content["link"], image["link"])

	def test_API_put_image(self) :
		values = dumps(image).encode("utf-8")
		headers = "application/json"
		response = self.client.put("/api/v1/image/3/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/image/3/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 4)
		self.assertEqual(response_content["id"], 3)
		self.assertEqual(response_content["link"], image["link"])

	def test_API_delete_image(self) :
		response = self.client.delete("/api/v1/image/3/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/image/3/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

	def test_API_delete_image_fail_case(self) :
		response = self.client.delete("/api/v1/iamge/2/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/image/2/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

	def test_API_delete_image_fail_case(self) :
		response = self.client.delete("/api/v1/image/foo/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)



class test_platform(TestCase) :
	fixtures = ["data.json"]
	def setUp(self):
		self.client = Client();

	def test_get_all_platform(self) :
		response = self.client.get("/api/v1/platform/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(response_content["meta"]["total_count"], 17)
		self.assertEqual(response_content["objects"][0]["name"], "Game Boy Advance")
		self.assertEqual(response_content["objects"][4]["name"], "Nintendo 64")

	def test_post_platform(self) :
		values = dumps(wii_u).encode("utf-8")
		headers = "application/json"
		response = self.client.post("/api/v1/platform/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 201)

	def test_API_get_single_platform(self) :
		response = self.client.get("/api/v1/platform/1/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 10)
		self.assertEqual(response_content["id"], 1)
		self.assertEqual(response_content["name"], "Wii U")

	def test_API_put_platform(self) :
		values = dumps(wii_u).encode("utf-8")
		headers = "application/json"
		response = self.client.put("/api/v1/platform/3/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/platform/3/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 10)
		self.assertEqual(response_content["id"], 3)
		self.assertEqual(response_content["name"], "Wii U")

	def test_API_delete_platform(self) :
		response = self.client.delete("/api/v1/platform/3/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/platform/3/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)



class test_developer(TestCase) :
	fixtures = ["data.json"]
	def setUp(self):
		self.client = Client();

	def test_get_all_developer(self) :
		response = self.client.get("/api/v1/developer/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(response_content["meta"]["total_count"], 19)
		self.assertEqual(response_content["objects"][2]["name"], "Capcom")
		self.assertEqual(response_content["objects"][4]["name"], "Dimps")

	def test_post_developer(self) :
		values = dumps(platinum_games).encode("utf-8")
		headers = "application/json"
		response = self.client.post("/api/v1/developer/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 201)

	def test_API_get_single_developer(self) :
		response = self.client.get("/api/v1/developer/2/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 10)
		self.assertEqual(response_content["id"], 2)
		self.assertEqual(response_content["name"], "Infinity Ward")

	def test_API_get_single_developer_fail_case(self):
		response = self.client.get("/api/v1/developer/pie")
		response_code = response.status_code
		self.assertEqual(response.status_code, 301)

	def test_API_put_developer(self) :
		values = dumps(platinum_games).encode("utf-8")
		headers = "application/json"
		response = self.client.put("/api/v1/developer/5/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/developer/5/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 10)
		self.assertEqual(response_content["id"], 5)
		self.assertEqual(response_content["name"], "Platinum Games")

	def test_API_put_developer_fail_case(self):
		values = dumps(platinum_games).encode("utf-8")
		headers = "application/json"
		response = self.client.put("/api/v1/developers/pie/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

	def test_API_delete_developer_fail_case(self) :
		response = self.client.delete("/api/v1/developer/8/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/developer/8/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

	def test_API_delete_developer_fail_case(self) :
		response = self.client.delete("/api/v1/developer/a/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)



class test_game(TestCase) :
	fixtures = ["data.json"]
	def setUp(self):
		self.client = Client();

	def test_get_all_game(self) :
		response = self.client.get("/api/v1/game/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(response_content["meta"]["total_count"], 23)
		self.assertEqual(response_content["objects"][1]["title"], "Call of Duty: Ghosts")
		self.assertEqual(response_content["objects"][8]["title"], "Halo 3")

	def test_post_game(self) :
		values = dumps(the_wonderful_101).encode("utf-8")
		headers = "application/json"
		response = self.client.post("/api/v1/game/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 201)

	def test_post_game_fail_case(self):
		values = dumps(the_wonderful_101).encode("utf-8")
		headers = "application/json"
		response = self.client.post("/api/v1/poop/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

	def test_API_get_single_game(self) :
		response = self.client.get("/api/v1/game/4/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 11)
		self.assertEqual(response_content["id"], 4)	
		self.assertEqual(response_content["title"], "Grand Theft Auto III")

	def test_API_get_single_game_fail_case(self):
		response = self.client.get("/api/v1/game/idontexist")

		response_code = response.status_code
		self.assertEqual(response.status_code, 301)

	def test_API_put_game(self) :
		values = dumps(the_wonderful_101).encode("utf-8")
		headers = "application/json"
		response = self.client.put("/api/v1/game/7/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/game/7/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 11)
		self.assertEqual(response_content["id"], 7)
		self.assertEqual(response_content["title"], "The Wonderful 101")


	def test_API_delete_game(self) :
		response = self.client.delete("/api/v1/game/5/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/game/5/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)



class test_search(TestCase) :
	fixtures = ["data.json"]
	def setUp(self):
		self.client = Client();

	def test_search_1(self) :
		response = self.client.get("http://ivgdb.herokuapp.com/search/?query=super")
		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = response.content.decode("utf-8").split('\n')
		self.assertEqual(response_content.count('                    <li class="list-group-item">'), 3)
		self.assertEqual(response_content[60], '                0 Developers - ')
		self.assertEqual(response_content[61], '                1 Platform - ')
		self.assertEqual(response_content[62], '                2 Games')

	def test_search_2(self) :
		response = self.client.get("http://ivgdb.herokuapp.com/search/?query=nintendo")
		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = response.content.decode("utf-8").split('\n')
		self.assertEqual(response_content.count('                    <li class="list-group-item">'), 17)
		self.assertEqual(response_content[60], '                1 Developer - ')
		self.assertEqual(response_content[61], '                9 Platforms - ')
		self.assertEqual(response_content[62], '                7 Games')

	def test_search_3(self) :
		response = self.client.get("http://ivgdb.herokuapp.com/search/?query=game+cube")
		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = response.content.decode("utf-8").split('\n')
		self.assertEqual(response_content.count('                    <li class="list-group-item">'), 11)
		self.assertEqual(response_content[60], '                5 Developers - ')
		self.assertEqual(response_content[61], '                2 Platforms - ')
		self.assertEqual(response_content[62], '                4 Games')
		self.assertEqual(response_content[100], '                        <a href="/platform/6">GameCube</a>')
		self.assertEqual(response_content[105], '                        <a href="/platform/5">Game Boy Advance</a>')

	def test_search_4(self) :
		response = self.client.get("http://ivgdb.herokuapp.com/search/?query=new+york")
		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = response.content.decode("utf-8").split('\n')
		self.assertEqual(response_content.count('                    <li class="list-group-item">'), 1)
		self.assertEqual(response_content[60], '                1 Developer - ')
		self.assertEqual(response_content[61], '                0 Platforms - ')
		self.assertEqual(response_content[62], '                0 Games')

	def test_search_5(self) :
		response = self.client.get("http://ivgdb.herokuapp.com/search/?query=defunct")
		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = response.content.decode("utf-8").split('\n')
		self.assertEqual(response_content.count('                    <li class="list-group-item">'), 2)
		self.assertEqual(response_content[60], '                2 Developers - ')
		self.assertEqual(response_content[61], '                0 Platforms - ')
		self.assertEqual(response_content[62], '                0 Games')
		
	def test_search_6(self) :
		response = self.client.get("http://ivgdb.herokuapp.com/search/?query=kghrio")
		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = response.content.decode("utf-8").split('\n')
		self.assertEqual(response_content.count('                    <li class="list-group-item">'), 0)
		self.assertEqual(response_content[60], "                Your search didn't match anything!")

	def test_search_7(self) :
		response = self.client.get("http://ivgdb.herokuapp.com/search/?query=cube+game")
		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = response.content.decode("utf-8").split('\n')
		self.assertEqual(response_content.count('                    <li class="list-group-item">'), 11)
		self.assertEqual(response_content[60], '                5 Developers - ')
		self.assertEqual(response_content[61], '                2 Platforms - ')
		self.assertEqual(response_content[62], '                4 Games')
		self.assertEqual(response_content[100], '                        <a href="/platform/6">GameCube</a>')
		self.assertEqual(response_content[105], '                        <a href="/platform/5">Game Boy Advance</a>')

#----------------------------------
# Testing Image through Tastypie
#----------------------------------
class ImageResourceTest(ResourceTestCase) :

	fixtures = ['data.json']

	def setUp(self):
		super(ImageResourceTest, self).setUp()
		
		# Create a user.
		self.username = 'polt'
		self.password = 'masher'
		self.api_key = 'poltergust'
		self.user = User.objects.create_user(self.username, 'poltergust@hotmail.com', self.password)
		
		# chose Game Boy Advance since it is the first alphabetically
		self.image_1 = Image.objects.get(pk=82)
		
		self.detail_url = '/api/v1/image/{0}/'.format(self.image_1.pk)
		
		self.post_data = {
			"id": 178,
			"description": "Tastypie Testing",
			"link": "http://upload.wikimedia.org/wikipedia/en/5/51/Hotel_Dusk.jpg",
			"resource_uri": '/api/v1/image/178/'
		}
		
	def get_credentials(self):
		return self.create_apikey(username=self.username, api_key=self.api_key)
        
	def test_get_list_json(self):
		resp = self.api_client.get('/api/v1/image/', format='json', authentication=self.get_credentials())
		self.assertValidJSONResponse(resp)
    	
		self.assertEqual(len(self.deserialize(resp)['objects']), 177)
		
		# compare with Game Boy Advance
		self.assertEqual(self.deserialize(resp)['objects'][0], {
			"id": self.image_1.pk,
			"description": str(self.image_1.description),
			"link": str(self.image_1.link),
			"resource_uri": '/api/v1/image/{0}/'.format(self.image_1.pk)
		})
		
	def test_get_detail_json(self):
		resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
		self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
		self.assertKeys(self.deserialize(resp), ['description', 'id', 'link', 'resource_uri'])
		self.assertEqual(self.deserialize(resp)['description'], str(self.image_1.description))
		
	def test_post_list(self):
        # Check how many are there first.
		self.assertEqual(Image.objects.count(), 177)
		self.assertHttpCreated(self.api_client.post('/api/v1/image/', format='json', data=self.post_data, authentication=self.get_credentials()))
        # Verify a new one has been added.
		self.assertEqual(Image.objects.count(), 178)
		
	def test_put_detail(self):
		# Grab the current data & modify it slightly.
		original_data = self.deserialize(self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials()))
		new_data = original_data.copy()
		new_data['description'] = 'Updated: Bethesda Game Studios #1'

		self.assertEqual(Image.objects.count(), 177)
		self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data, authentication=self.get_credentials()))
		
		# Make sure the count hasn't changed & we did an update.
		self.assertEqual(Image.objects.count(), 177)
		# Check for updated data.
		self.assertEqual(Image.objects.get(pk=82).description, 'Updated: Bethesda Game Studios #1')
		
	def test_delete_detail(self):
		self.assertEqual(Image.objects.count(), 177)
		self.assertHttpAccepted(self.api_client.delete(self.detail_url, format='json', authentication=self.get_credentials()))
		self.assertEqual(Image.objects.count(), 176)

#----------------------------------
# Testing Platform through Tastypie
#----------------------------------
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
			"id": 18,
			"name": "Genesis",
			"manufacturer": "Sega",
			"release_date": "1991-06-17",
			"media_format": "Physical (cartridge)",
			"generation": 4,
			"youtube_link": "http://www.youtube.com/embed/qhlDHeCT-Q8",
			"twitter_link": "446085251077373952",
			"images": ['/api/v1/image/{0}/'.format(Image.objects.get(pk=1).pk), '/api/v1/image/{0}/'.format(Image.objects.get(pk=2).pk), '/api/v1/image/{0}/'.format(Image.objects.get(pk=3).pk)],
			"resource_uri": '/api/v1/platform/18/'
		}
		
	def get_credentials(self):
		return self.create_apikey(username=self.username, api_key=self.api_key)
        
	def test_get_list_json(self):
		resp = self.api_client.get('/api/v1/platform/', format='json', authentication=self.get_credentials())
		self.assertValidJSONResponse(resp)
    	
		self.assertEqual(len(self.deserialize(resp)['objects']), 17)
		
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
			"images": ['/api/v1/image/{0}/'.format(o.pk) for o in self.platform_1.images.all()],
			"resource_uri": '/api/v1/platform/{0}/'.format(self.platform_1.pk)
		})
		
	def test_get_detail_json(self):
		resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
		self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
		self.assertKeys(self.deserialize(resp), ['generation', 'id', 'images', 'manufacturer', 'media_format', 'name', 'release_date', 'resource_uri', 'twitter_link', 'youtube_link'])
		self.assertEqual(self.deserialize(resp)['name'], str(self.platform_1.name))
		
	def test_post_list(self):
        # Check how many are there first.
		self.assertEqual(Platform.objects.count(), 17)
		self.assertHttpCreated(self.api_client.post('/api/v1/platform/', format='json', data=self.post_data, authentication=self.get_credentials()))
        # Verify a new one has been added.
		self.assertEqual(Platform.objects.count(), 18)
		
	def test_put_detail(self):
		# Grab the current data & modify it slightly.
		original_data = self.deserialize(self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials()))
		new_data = original_data.copy()
		new_data['name'] = 'Updated: Game Boy Advance'

		self.assertEqual(Platform.objects.count(), 17)
		self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data, authentication=self.get_credentials()))
		
		# Make sure the count hasn't changed & we did an update.
		self.assertEqual(Platform.objects.count(), 17)
		# Check for updated data.
		self.assertEqual(Platform.objects.get(pk=5).name, 'Updated: Game Boy Advance')
		self.assertEqual(Platform.objects.get(pk=5).manufacturer, 'Nintendo')
		
	def test_delete_detail(self):
		self.assertEqual(Platform.objects.count(), 17)
		self.assertHttpAccepted(self.api_client.delete(self.detail_url, format='json', authentication=self.get_credentials()))
		self.assertEqual(Platform.objects.count(), 16)

#-----------------------------------
# Testing Developer through Tastypie
#-----------------------------------
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
		self.developer_1 = Developer.objects.get(name='Bethesda Game Studios')
		
		self.detail_url = '/api/v1/developer/{0}/'.format(self.developer_1.pk)
		
		self.post_data = {
			"id": 21,
			"name": "Sega",
			"date_founded": "1987-02-23",
			"num_employees": 324,
			"status": "Active",
			"address": "Tokyo, Japan",
			"map_link": "https://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=1-1-30+Oyodo-naka,+Kita-ku,+Osaka,+531-6108&aq=&sll=34.704426,135.485297&sspn=0.004397,0.008256&ie=UTF8&hq=&hnear=1+Chome-1-30+%C5%8Cyodonaka,+Kita-ku,+%C5%8Csaka-shi,+%C5%8Csaka-fu",
			"images": ['/api/v1/image/{0}/'.format(Image.objects.get(pk=52).pk), '/api/v1/image/{0}/'.format(Image.objects.get(pk=53).pk), '/api/v1/image/{0}/'.format(Image.objects.get(pk=54).pk)],
			"platforms": ['/api/v1/platform/{0}/'.format(Platform.objects.get(pk=1).pk), '/api/v1/platform/{0}/'.format(Platform.objects.get(pk=6).pk)],
			'resource_uri': '/api/v1/developer/21/'
		}
		
	def get_credentials(self):
		return self.create_apikey(username=self.username, api_key=self.api_key)
		
	#def test_get_list_unauthorzied(self):
		#self.assertHttpUnauthorized(self.api_client.get('/api/v1/developer/', format='json'))
        
	def test_get_list_json(self):
		resp = self.api_client.get('/api/v1/developer/', format='json', authentication=self.get_credentials())
		self.assertValidJSONResponse(resp)
    	
		self.assertEqual(len(self.deserialize(resp)['objects']), 19)
		
		# compare with Cing
		self.assertEqual(self.deserialize(resp)['objects'][0], {
			"id": self.developer_1.pk,
			"name": str(self.developer_1.name),
			"date_founded": str(self.developer_1.date_founded),
			"num_employees": self.developer_1.num_employees,
			"status": str(self.developer_1.status),
			"address": str(self.developer_1.address),
			"map_link": str(self.developer_1.map_link),
			"images": ['/api/v1/image/{0}/'.format(o.pk) for o in self.developer_1.images.all()],
			"platforms": ['/api/v1/platform/{0}/'.format(o.pk) for o in self.developer_1.platforms.all()],
			'resource_uri': '/api/v1/developer/{0}/'.format(self.developer_1.pk)
		})
		
	def test_get_detail_json(self):
		resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
		self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
		self.assertKeys(self.deserialize(resp), ['address', 'date_founded', 'id', 'images', 'map_link', 'name', 'num_employees', 'platforms', 'resource_uri', 'status'])
		self.assertEqual(self.deserialize(resp)['name'], str(self.developer_1.name))
		
	def test_post_list(self):
        # Check how many are there first.
		self.assertEqual(Developer.objects.count(), 19)
		self.assertHttpCreated(self.api_client.post('/api/v1/developer/', format='json', data=self.post_data, authentication=self.get_credentials()))
        # Verify a new one has been added.
		self.assertEqual(Developer.objects.count(), 20)
		
	def test_put_detail(self):
		# Grab the current data & modify it slightly.
		original_data = self.deserialize(self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials()))
		new_data = original_data.copy()
		new_data['name'] = 'Updated: Bethesda Game Studios'

		self.assertEqual(Developer.objects.count(), 19)
		self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data, authentication=self.get_credentials()))
		
		# Make sure the count hasn't changed & we did an update.
		self.assertEqual(Developer.objects.count(), 19)
		# Check for updated data.
		self.assertEqual(Developer.objects.get(pk=12).name, 'Updated: Bethesda Game Studios')
		self.assertEqual(Developer.objects.get(pk=12).status, 'Active')
		
	def test_delete_detail(self):
		self.assertEqual(Developer.objects.count(), 19)
		self.assertHttpAccepted(self.api_client.delete(self.detail_url, format='json', authentication=self.get_credentials()))
		self.assertEqual(Developer.objects.count(), 18)

#------------------------------
# Testing Game through Tastypie
#------------------------------
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
			"id": 24,
			"title": "Bayonetta",
			"release_date": "2010-07-12",
			"genre": "Action",
			"publisher": "Sega",
			"esrb_rating": "M",
			"youtube_link": "www.youtube.com/embed/z9ueBmNNGus",
			"images" : ['/api/v1/image/{0}/'.format(Image.objects.get(pk=109).pk), '/api/v1/image/{0}/'.format(Image.objects.get(pk=110).pk), '/api/v1/image/{0}/'.format(Image.objects.get(pk=111).pk)],
			'developer': '/api/v1/developer/{0}/'.format(Developer.objects.get(pk=1).pk),
			'platforms': ['/api/v1/platform/{0}/'.format(Platform.objects.get(pk=2).pk), '/api/v1/platform/{0}/'.format(Platform.objects.get(pk=10).pk)],
			'resource_uri': '/api/v1/game/24/'
		}
		
	def get_credentials(self):
		return self.create_apikey(username=self.username, api_key=self.api_key)
		
	#def test_get_list_unauthorzied(self):
		#self.assertHttpUnauthorized(self.api_client.get('/api/v1/game/', format='json'))
        
	def test_get_list_json(self):
		resp = self.api_client.get('/api/v1/game/', format='json', authentication=self.get_credentials())
		self.assertValidJSONResponse(resp)
    	
		self.assertEqual(len(self.deserialize(resp)['objects']), 23)
		
		# compare with Call of Duty 4: Modern Warfare
		self.assertEqual(self.deserialize(resp)['objects'][0], {
			"id": self.game_1.pk,
			"title": str(self.game_1.title),
			"release_date": str(self.game_1.release_date),
			"genre": str(self.game_1.genre),
			"publisher": str(self.game_1.publisher),
			"esrb_rating": str(self.game_1.esrb_rating),
			"youtube_link": str(self.game_1.youtube_link),
			"images": ['/api/v1/image/{0}/'.format(o.pk) for o in self.game_1.images.all()],
			'developer': '/api/v1/developer/{0}/'.format(self.game_1.developer.pk),
			'platforms': ['/api/v1/platform/{0}/'.format(o.pk) for o in self.game_1.platforms.all()],
			'resource_uri': '/api/v1/game/{0}/'.format(self.game_1.pk)
		})
		
	def test_get_detail_json(self):
		resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
		self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
		self.assertKeys(self.deserialize(resp), ['developer', 'esrb_rating', 'genre', 'id', 'images', 'platforms', 'publisher', 'release_date', 'resource_uri', 'title', 'youtube_link'])
		self.assertEqual(self.deserialize(resp)['title'], str(self.game_1.title))
		
	def test_post_list(self):
        # Check how many are there first.
		self.assertEqual(Game.objects.count(), 23)
		self.assertHttpCreated(self.api_client.post('/api/v1/game/', format='json', data=self.post_data, authentication=self.get_credentials()))
        # Verify a new one has been added.
		self.assertEqual(Game.objects.count(), 24)
		
	def test_put_detail(self):
		# Grab the current data & modify it slightly.
		original_data = self.deserialize(self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials()))
		new_data = original_data.copy()
		new_data['title'] = 'Updated: Call of Duty 4: Modern Warfare'

		self.assertEqual(Game.objects.count(), 23)
		self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data, authentication=self.get_credentials()))
		
		# Make sure the count hasn't changed & we did an update.
		self.assertEqual(Game.objects.count(), 23)
		# Check for updated data.
		self.assertEqual(Game.objects.get(pk=2).title, 'Updated: Call of Duty 4: Modern Warfare')
		self.assertEqual(Game.objects.get(pk=2).genre, 'First-person shooting')
		
	def test_delete_detail(self):
		self.assertEqual(Game.objects.count(), 23)
		self.assertHttpAccepted(self.api_client.delete(self.detail_url, format='json', authentication=self.get_credentials()))
		self.assertEqual(Game.objects.count(), 22)

print("Done")
