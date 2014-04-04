#!/usr/bin/env python3

from django.test import TestCase
from django.test.client import Client
from json import dumps, loads



platinum_games = {
	"name": "Platinum Games",
	"date_founded": "2006-04-08",
	"num_employees": 120,
	"status": "Active",
	"address": "Umeda Sky Building Tower West 8F,\n1-1-30 Oyodo-naka, Kita-ku, Osaka, 531-6108",
	"map_link": "https://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=1-1-30+Oyodo-naka,+Kita-ku,+Osaka,+531-6108&aq=&sll=34.704426,135.485297&sspn=0.004397,0.008256&ie=UTF8&hq=&hnear=1+Chome-1-30+%C5%8Cyodonaka,+Kita-ku,+%C5%8Csaka-shi,+%C5%8Csaka-fu,+Japan&ll=34.70533,135.489699&spn=0.035033,0.066047&t=m&z=14&output=embed",
	"image_link1": "http://nonspecificaction.co.uk/wp-content/uploads/platinum-games-logo.jpg",
	"image_link2": "http://www.gamechup.com/wp-content/uploads/2014/01/platinum-games-project-nagano.jpg",
	"image_link3": "http://3.bp.blogspot.com/_Z50Ik1LwTlQ/TUAHdjb-3oI/AAAAAAAAEYA/pj5C9fp1ctg/s1600/platgamesega.jpg",
	"platforms": ["/api/v1/platform/1/"]
}

the_wonderful_101 = {
	"title": "The Wonderful 101",
	"release_date": "2013-09-15",
	"genre": "Action",
	"publisher": "Nintendo",
	"ESRB_rating": "T",
	"youtube_link": "www.youtube.com/embed/z9ueBmNNGus",
	"image_link1": "http://s11.postimg.org/xjy2jtm6b/the_wonderful_101_logo.png",
	"image_link2": "http://venturebeat.files.wordpress.com/2013/05/the-wonderful-101.jpg",
	"image_link3": "http://stickskills.com/wp-content/uploads/2013/01/The-Wonderful-101.jpg",
	"developer": "/api/v1/developer/1/", 
	"platforms":["/api/v1/platform/1/"]
}

wii_u = {
	"name": "Wii U",
	"manufacturer": "Nintendo",
	"release_date": "2012-11-18T00:00:00",
	"media_format": "Physical (disks) and digital",
	"generation": 8,
	"youtube_link": "http://www.youtube.com/embed/qhlDHeCT-Q8",
	"twitter_link": "446085251077373952",
	"image_link1": "http://g-ecx.images-amazon.com/images/G/01/aplus/detail-page/B009AGXH64hardware.jpg",
	"image_link2": "http://www.dailynintendo.nl/wp-content/uploads/2011/05/wii-u.jpg",
	"image_link3": "http://blogs-images.forbes.com/erikkain/files/2012/11/blackcontroller_big-1.jpg"
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
		self.assertEqual(len(response_content), 3)
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


class test_platform(TestCase) :
	fixtures = ["data.json"]
	def setUp(self):
		self.client = Client();

	def test_get_all_platform(self) :
		response = self.client.get("/api/v1/platform/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(response_content["meta"]["total_count"], 10)
		self.assertEqual(response_content["objects"][0]["name"], "Game Boy Advance")
		self.assertEqual(response_content["objects"][4]["name"], "Nintendo DS")

	def test_post_platform(self) :
		values = dumps(wii_u).encode("utf-8")
		headers = "application/json"
		response = self.client.post("/api/v1/platform/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 201)

		# response_content = loads(response.content.decode("utf-8"))
		# results = wii_u.copy().update({"id": 11, 'resource_uri': '/api/v1/platform/11/'})
		# self.assertTrue(response_content, results)

	def test_API_get_single_platform(self) :
		response = self.client.get("/api/v1/platform/1/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 12)
		self.assertEqual(response_content["id"], 1)
		self.assertEqual(response_content["name"], "Wii U")

	def test_API_put_platform(self) :
		values = dumps(wii_u).encode("utf-8")
		headers = "application/json"
		response = self.client.put("/api/v1/platform/3/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		# response_content = loads(response.content.decode("utf-8"))
		# results = wii_u.copy().update({"id": 3, 'resource_uri': '/api/v1/platform/3/'})
		# self.assertTrue(response_content, results)

		response = self.client.get("/api/v1/platform/3/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 12)
		self.assertEqual(response_content["id"], 3)
		self.assertEqual(response_content["name"], "Wii U")

	def test_API_delete_platform(self) :
		response = self.client.delete("/api/v1/platform/3/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/platform/3/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)


"""
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
"""



class test_game(TestCase) :
	fixtures = ["data.json"]
	def setUp(self):
		self.client = Client();

	def test_get_all_game(self) :
		response = self.client.get("/api/v1/game/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(response_content["meta"]["total_count"], 10)
		self.assertEqual(response_content["objects"][1]["title"], "Doom 64")
		self.assertEqual(response_content["objects"][8]["title"], "The Wonderful 101")

	def test_post_game(self) :
		values = dumps(the_wonderful_101).encode("utf-8")
		headers = "application/json"
		response = self.client.post("/api/v1/game/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 201)

		# response_content = loads(response.content.decode("utf-8"))
		# results = the_wonderful_101.copy().update({"id": 11, 'resource_uri': '/api/v1/game/11/'})
		# self.assertTrue(response_content, results)

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
		self.assertEqual(len(response_content), 13)
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

		# response_content = loads(response.content.decode("utf-8"))
		# results = the_wonderful_101.copy().update({"id": 7, 'resource_uri': '/api/v1/game/7/'})
		# self.assertTrue(response_content, results)

		response = self.client.get("/api/v1/game/7/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 13)
		self.assertEqual(response_content["id"], 7)
		self.assertEqual(response_content["title"], "The Wonderful 101")


	def test_API_delete_game(self) :
		response = self.client.delete("/api/v1/game/5/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/game/5/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

"""
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
		self.assertTrue(response_content == [wii_u])
"""



class test_developer(TestCase) :
	fixtures = ["data.json"]
	def setUp(self):
		self.client = Client();

	def test_get_all_developer(self) :
		response = self.client.get("/api/v1/developer/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(response_content["meta"]["total_count"], 10)
		self.assertEqual(response_content["objects"][2]["name"], "HAL Laboratories")
		self.assertEqual(response_content["objects"][4]["name"], "Konami")

	def test_post_developer(self) :
		values = dumps(platinum_games).encode("utf-8")
		headers = "application/json"
		response = self.client.post("/api/v1/developer/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 201)

		# response_content = loads(response.content.decode("utf-8"))
		# results = platinum_games.copy().update({"id": 11, 'resource_uri': '/api/v1/developer/11/'})
		# self.assertTrue(response_content, results)

	def test_API_get_single_developer(self) :
		response = self.client.get("/api/v1/developer/2/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 12)
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

		# response_content = loads(response.content.decode("utf-8"))
		# results = platinum_games.copy().update({"id": 5, 'resource_uri': '/api/v1/developer/5/'})
		# self.assertTrue(response_content, results)

		response = self.client.get("/api/v1/developer/5/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 12)
		self.assertEqual(response_content["id"], 5)
		self.assertEqual(response_content["name"], "Platinum Games")

	def test_API_put_developer_fail_case(self):
		values = dumps(platinum_games).encode("utf-8")
		headers = "application/json"
		response = self.client.put("/api/v1/developers/pie/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

	def test_API_delete_developer(self) :
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

		# response = self.client.get("/api/v1/developer/8/")

		# response_code = response.status_code
		# self.assertEqual(response.status_code, 404)


"""
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
"""
