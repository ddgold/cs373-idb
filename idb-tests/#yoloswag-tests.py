from django.test import TestCase
from urllib.request import urlopen, Request
from json import dumps, loads


# Create your tests here.



class APItests(TestCase) :

	#Figures

	def test_get_all_figures(self) :


		request = Request("http://cs373idb.apiary-mock.com/api/figures")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)
		expected_response = [{
		    "id": 1,
		    "title":"Atlas",
		    "kind":"Titan",
		    "biography":"Long text description here."
		}, {
		    "id": 2,
		    "title":"Athena",
		    "kind":"Olympian",
		    "biography":"Long text description here."
		}, {
		    "id": 3,
		    "title":"Loki",
		    "kind":"God",
		    "biography":"Long text description here."
		}]

		self.assertTrue(expected_response == response_data)

	def test_post_figure(self) :

		values = dumps({
            "title":"Loki",
            "kind":"God",
            "biography":"Long text description here.",
            "images":[{"link":"http://upload.wikimedia.org/wikipedia/commons/4/40/Processed_SAM_loki.jpg"},
                      {"link":"http://upload.wikimedia.org/wikipedia/commons/a/ac/Loki_taunts_Bragi.jpg"},
                      {"link":"http://upload.wikimedia.org/wikipedia/commons/c/cb/Louis_Huard_-_The_Punishment_of_Loki.jpg"}],
            "videos":[{"link":"http://www.youtube.com/embed/o43-oAL2ogY"}],
            "related_figures":[],
            "related_stories":[],
            "related_cultures":[{"id":3, "name":"Nordic"}],
            "external_links":[{"name":"Wikipedia: Loki", "link":"http://en.wikipedia.org/wiki/Loki"},
                              {"name":"Pantheon.Org", "link":"http://www.pantheon.org/articles/l/loki.html"}]
        }).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://cs373idb.apiary-mock.com/api/figures", data=values, headers=headers)
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 201)
		response_data = loads(response_body)
		expected_response = {
		    "id": 3
		}

		self.assertTrue(expected_response == response_data)

	def test_get_figure(self) :
		expected_response = {
            "id": 3,
            "title":"Loki",
            "kind":"God",
            "biography":"Long text description here.",
            "images":[{"link":"http://upload.wikimedia.org/wikipedia/commons/4/40/Processed_SAM_loki.jpg"},
                      {"link":"http://upload.wikimedia.org/wikipedia/commons/a/ac/Loki_taunts_Bragi.jpg"},
                      {"link":"http://upload.wikimedia.org/wikipedia/commons/c/cb/Louis_Huard_-_The_Punishment_of_Loki.jpg"}],
            "videos":[{"link":"http://www.youtube.com/embed/o43-oAL2ogY"}],
            "related_figures":[],
            "related_stories":[],
            "related_cultures":[{"id":3, "name":"Nordic"}],
            "external_links":[{"name":"Wikipedia: Loki", "link":"http://en.wikipedia.org/wiki/Loki"},
                              {"name":"Pantheon.Org", "link":"http://www.pantheon.org/articles/l/loki.html"}]
        }

		request = Request("http://cs373idb.apiary-mock.com/api/figures/{id}")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)

		self.assertTrue(expected_response == response_data)

	def test_delete_figure(self) :
		request = Request("http://cs373idb.apiary-mock.com/api/figures/{id}")
		request.get_method = lambda: 'DELETE'

		response = urlopen(request)
		response_body = response.read()

		self.assertEqual(response.getcode(), 204)

	#Stories

	def test_get_all_stories(self) :


		request = Request("http://cs373idb.apiary-mock.com/api/stories")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)
		expected_response = [{
		    "id": 1,
		    "title":"The Birth of Athena",
		    "summary":"Long text description here."
		}, {
		    "id": 2,
		    "title":"The Punishment of Atlas",
		    "summary":"Long text description here."
		}, {
		    "id": 3,
		    "title":"Reginsmál",
		    "summary":"Long text description here."
		}]

		self.assertTrue(expected_response == response_data)

	def test_post_story(self) :

		values = dumps({
		    "title":"The Punishment of Atlas",
		    "summary":"Long text description here.",
		    "images":[{"link":"http://upload.wikimedia.org/wikipedia/commons/8/8c/MAN_Atlante_fronte_1040572.JPG"}],
		    "videos":[],
		    "related_figures":[{"id":1, "name":"Atlas"}, {"id":2, "name":"Athena"}],
		    "related_stories":[],
		    "related_cultures":[{"id":1, "name":"Greek"}, {"id":2, "name":"Roman"}],
		    "external_links":[{"name":"Wikipedia: Atlas", "link":"http://en.wikipedia.org/wiki/Atlas_(mythology)"},
		                    {"name":"Ancient History", "link":"http://ancienthistory.about.com/od/atlastitanmyth/f/081409WorldonShouders.htm"}]
		}).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://cs373idb.apiary-mock.com/api/stories", data=values, headers=headers)
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 201)
		response_data = loads(response_body)
		expected_response = {
		    "id": 2
		}

		self.assertTrue(expected_response == response_data)

	def test_get_story(self) :
		expected_response = {
		    "id": 2,
		    "title":"The Punishment of Atlas",
		    "summary":"Long text description here.",
		    "images":[{"link":"http://upload.wikimedia.org/wikipedia/commons/8/8c/MAN_Atlante_fronte_1040572.JPG"}],
		    "videos":[],
		    "related_figures":[{"id":1, "name":"Atlas"}, {"id":2, "name":"Athena"}],
		    "related_stories":[],
		    "related_cultures":[{"id":1, "name":"Greek"}, {"id":2, "name":"Roman"}],
		    "external_links":[{"name":"Wikipedia: Atlas", "link":"http://en.wikipedia.org/wiki/Atlas_(mythology)"},
		                    {"name":"Ancient History", "link":"http://ancienthistory.about.com/od/atlastitanmyth/f/081409WorldonShouders.htm"}]
		}

		request = Request("http://cs373idb.apiary-mock.com/api/stories/{id}")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)

		self.assertTrue(expected_response == response_data)

	def test_delete_story(self) :
		request = Request("http://cs373idb.apiary-mock.com/api/stories/{id}")
		request.get_method = lambda: 'DELETE'

		response = urlopen(request)
		response_body = response.read()

		self.assertEqual(response.getcode(), 204)

	#Cultures

	def test_get_all_cultures(self) :


		request = Request("http://cs373idb.apiary-mock.com/api/cultures")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)
		expected_response = [{
		    "id": 1,
		    "title":"Greek",
		    "region":"Greece",
		    "language":"Greek",
		    "history":"Long text description here."
		}, {
		    "id": 2,
		    "title":"Roman",
		    "region":"Mediterranean",
		    "language":"Latin",
		    "history":"Long text description here."
		}, {
		    "id": 3,
		    "title":"Nordic",
		    "region":"Scandinavia",
		    "language":"Old Norse",
		    "history":"Long text description here."
		}]

		self.assertTrue(expected_response == response_data)

	def test_post_culture(self) :

		values = dumps({
		    "title":"Greek",
		    "region":"Greece",
		    "language":"Greek",
		    "history":"Long text description here.",
		    "images":[{"link":"http://upload.wikimedia.org/wikipedia/commons/a/ad/Parthenon_from_west.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/1/19/William_Faden._Composite_Mediterranean._1785.I.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/8/87/ArchaicGr.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/7/7c/Beginning_Odyssey.svg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/9/96/EarlyAthenianCoin.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/4/4a/Law_Code_Gortyn_Louvre_Ma703.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/a/a4/Socrates_Louvre.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/2/22/Greek-Persian_duel.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/1/1c/Homer_British_Museum.jpg"}],
		    "videos":[{"link":"http://www.youtube.com/embed/WptSXfvY-vs"},
		              {"link":"http://www.youtube.com/embed/vHMu2gVzspA"}],
		    "related_figures":[{"id":1, "name":"Atlas"}, {"id":2, "name":"Athena"}],
		    "related_stories":[],
		    "related_cultures":[{"id":2, "name":"Roman"}],
		    "external_links":[{"name":"Wikipedia: Greeks", "link":"http://en.wikipedia.org/wiki/Greeks"},
		                      {"name":"Wikipedia: Ancient Greece", "link":"http://en.wikipedia.org/wiki/Ancient_Greece"},
		                      {"name":"ancientgreece.com", "link":"http://www.ancientgreece.com/s/Main_Page/"},
		                      {"name":"BBC: Ancient Greeks", "link":"http://www.bbc.co.uk/schools/primaryhistory/ancient_greeks/"},
		                      {"name":"History Channel: Ancient Greeks", "link":"http://www.history.com/topics/ancient-history/ancient-greece"}]
		}).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://cs373idb.apiary-mock.com/api/cultures", data=values, headers=headers)
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 201)
		response_data = loads(response_body)
		expected_response = {
		    "id": 1
		}

		self.assertTrue(expected_response == response_data)

	def test_get_culture(self) :
		expected_response = {
		    "id": 1,
		    "title":"Greek",
		    "region":"Greece",
		    "language":"Greek",
		    "history":"Long text description here.",
		    "images":[{"link":"http://upload.wikimedia.org/wikipedia/commons/a/ad/Parthenon_from_west.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/1/19/William_Faden._Composite_Mediterranean._1785.I.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/8/87/ArchaicGr.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/7/7c/Beginning_Odyssey.svg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/9/96/EarlyAthenianCoin.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/4/4a/Law_Code_Gortyn_Louvre_Ma703.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/a/a4/Socrates_Louvre.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/2/22/Greek-Persian_duel.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/1/1c/Homer_British_Museum.jpg"}],
		    "videos":[{"link":"http://www.youtube.com/embed/WptSXfvY-vs"},
		              {"link":"http://www.youtube.com/embed/vHMu2gVzspA"}],
		    "related_figures":[{"id":1, "name":"Atlas"}, {"id":2, "name":"Athena"}],
		    "related_stories":[],
		    "related_cultures":[{"id":2, "name":"Roman"}],
		    "external_links":[{"name":"Wikipedia: Greeks", "link":"http://en.wikipedia.org/wiki/Greeks"},
		                      {"name":"Wikipedia: Ancient Greece", "link":"http://en.wikipedia.org/wiki/Ancient_Greece"},
		                      {"name":"ancientgreece.com", "link":"http://www.ancientgreece.com/s/Main_Page/"},
		                      {"name":"BBC: Ancient Greeks", "link":"http://www.bbc.co.uk/schools/primaryhistory/ancient_greeks/"},
		                      {"name":"History Channel: Ancient Greeks", "link":"http://www.history.com/topics/ancient-history/ancient-greece"}]
		}

		request = Request("http://cs373idb.apiary-mock.com/api/cultures/{id}")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)

		self.assertTrue(expected_response == response_data)

	def test_delete_culture(self) :
		request = Request("http://cs373idb.apiary-mock.com/api/cultures/{id}")
		request.get_method = lambda: 'DELETE'

		response = urlopen(request)
		response_body = response.read()

		self.assertEqual(response.getcode(), 204)




print("Done.")