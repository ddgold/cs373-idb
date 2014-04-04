#!/usr/bin/env python3

from django.test import TestCase
from django.test.client import Client
from json import dumps, loads

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
		# print(response_content)

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
		# print(response_content)

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
		# print(response_content)

	def test_API_get_single_game(self) :
		response = self.client.get("/api/v1/game/4/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 13)
		self.assertEqual(response_content["id"], 4)
		self.assertEqual(response_content["title"], "Grand Theft Auto III")

	def test_API_put_game(self) :
		values = dumps(the_wonderful_101).encode("utf-8")
		headers = "application/json"
		response = self.client.put("/api/v1/game/7/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		# response_content = loads(response.content.decode("utf-8"))
		# print(response_content)

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
		# print(response_content)

	def test_API_get_single_developer(self) :
		response = self.client.get("/api/v1/developer/2/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 12)
		self.assertEqual(response_content["id"], 2)
		self.assertEqual(response_content["name"], "Infinity Ward")

	def test_API_put_developer(self) :
		values = dumps(platinum_games).encode("utf-8")
		headers = "application/json"
		response = self.client.put("/api/v1/developer/5/", values, headers)

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		# response_content = loads(response.content.decode("utf-8"))
		# print(response_content)

		response = self.client.get("/api/v1/developer/5/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 200)

		response_content = loads(response.content.decode("utf-8"))
		self.assertEqual(len(response_content), 12)
		self.assertEqual(response_content["id"], 5)
		self.assertEqual(response_content["name"], "Platinum Games")

	def test_API_delete_developer(self) :
		response = self.client.delete("/api/v1/developer/8/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 204)

		response = self.client.get("/api/v1/developer/8/")

		response_code = response.status_code
		self.assertEqual(response.status_code, 404)

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
