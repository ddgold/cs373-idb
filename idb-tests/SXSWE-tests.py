#!/usr/bin/env python3

from django.test import TestCase
from urllib.request import urlopen, Request
from json import dumps, loads

RESPONSE_1 = "{ id: 1 }"

CHILDISH_GAMBINO = {
	"name": "Childish Gambino",
	"id": 1,
	"genre": "hip hop",
	"year_established": "2002",
	"origin": "United States",
	"website": "http://iamdonald.com/",
	"instruments": ["bass", "drums", "guitar", "synthesizer", "sequencer", "sampler", "vocals"],
	"facebook": "iamdonald",
	"twitter": "DonaldGlover",
	"youtube": "ChildishGambinoVEVO",
	"members": ["Donald Glover"],
	"labels": ["Island", "Glass Note"],
	"images": ["http://upload.wikimedia.org/wikipedia/commons/3/3a/CG_Coachella.jpg"]
}

CHILDISH_GAMBINO_SMALL = [{'genre': 'hip hop', 'name': 'Childish Gambino', 'id': 1}]

DELL = {
        "id": 1,
        "name": "Dell",
        "established": "1984-11-04",
        "location": "Round Rock, Texas, United States",
        "industry": "technology",
        "CEO": "Michael Dell",
        "images": ["http://upload.wikimedia.org/wikipedia/commons/4/48/Dell_Logo.svg"],
        "facebook": "Dell",
        "twitter": "Dell",
        "website": "http://dell.com"
    }

DELL_SMALL = [
    {
        "id": 1,
        "name": "Dell",
        "industry": "technology"
    }
]

WOODIE = {
        "name": "Woodie Awards",
        "id": 1,
        "date": "2014-03-16",
        "description": "MTV’s Woodie Festival is back. Plan for an unforgettable musical lineup, free food, drinks & surprises! Come nightfall the Woodie Awards will take over the event for an epic night of music performances.",
        "type": "outdoor",
        "images": ["http://upload.wikimedia.org/wikipedia/en/c/c5/MtvU_logo_2011.png"],
        "location_name": "Red River Stage",
        "location_address": "Red River & E 1st St, Austin, Texas"
    }

WOODIE_SMALL = [
    {
        "name": "Woodie Awards",
        "id": 1,
        "date": "2014-03-16"
    }
]
# ----------------------
# RESTful API Unit Tests
# SXSWE
# ----------------------

class test_API(TestCase) :

	# ARTISTS

	def test_get_artists (self):
		request = Request("http://sxswe.apiary-mock.com/api/artists")
		response_body = urlopen(request).read().decode("utf-8")
		response = loads(response_body)
		expected = CHILDISH_GAMBINO_SMALL
		self.assertTrue(expected == response)

	def test_get_artist (self):
		request = Request("http://sxswe.apiary-mock.com/api/artists/{id}")
		response_body = urlopen(request).read().decode("utf-8")
		response = loads(response_body)
		expected = CHILDISH_GAMBINO
		self.assertTrue(expected == response)

	def test_post_artists (self):
		values = dumps(CHILDISH_GAMBINO).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://sxswe.apiary-mock.com/api/artists", data=values, headers=headers)
		response = urlopen(request)
		response_body = response.read().decode("utf-8")

		expected = RESPONSE_1

		self.assertEqual(response.getcode(), 201)
		self.assertTrue(expected == response_body)


	def test_put_artists (self):
		values = dumps(CHILDISH_GAMBINO).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://sxswe.apiary-mock.com/api/artists/{id}", data=values, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)

		response_body = response.read()
		
		self.assertEqual(response.getcode(), 204)


	def test_delete_artists (self):
		request = Request("http://sxswe.apiary-mock.com/api/artists/{id}")
		request.get_method = lambda: 'DELETE'

		response = urlopen(request)
		response_body = response.read()
		
		self.assertEqual(response.getcode(), 204)

	def test_get_artist_sponsors (self):
		request = Request("http://sxswe.apiary-mock.com/api/artists/{id}/sponsors")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		response_dict = loads(response_body)

		expected = [DELL]

		self.assertEqual(response.getcode(), 200)
		self.assertTrue(expected == response_dict)
	
	def test_get_artist_events (self):
		request = Request("http://sxswe.apiary-mock.com/api/artists/{id}/events")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		response_dict = loads(response_body)

		expected = [WOODIE]

		self.assertEqual(response.getcode(), 200)
		self.assertTrue(expected == response_dict)

	# SPONSORS
	def test_get_sponsors (self):
		request = Request("http://sxswe.apiary-mock.com/api/sponsors")
		response_body = urlopen(request).read().decode("utf-8")
		response = loads(response_body)
		expected = DELL_SMALL
		self.assertTrue(expected == response)

	def test_get_sponsor (self):
		request = Request("http://sxswe.apiary-mock.com/api/sponsors/{id}")
		response_body = urlopen(request).read().decode("utf-8")
		response = loads(response_body)
		expected = DELL
		self.assertTrue(expected == response)

	def test_post_sponsors (self):
		values = dumps(DELL).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://sxswe.apiary-mock.com/api/sponsors", data=values, headers=headers)
		response = urlopen(request)
		response_body = response.read().decode("utf-8")

		expected = RESPONSE_1

		self.assertEqual(response.getcode(), 201)
		self.assertTrue(expected == response_body)

	def test_put_sponsors (self):
		values = dumps(DELL).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://sxswe.apiary-mock.com/api/sponsors/{id}", data=values, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)

		response_body = response.read()
		
		self.assertEqual(response.getcode(), 204)

	def test_delete_sponsors (self):
		request = Request("http://sxswe.apiary-mock.com/api/sponsors/{id}")
		request.get_method = lambda: 'DELETE'

		response = urlopen(request)
		response_body = response.read()
		
		self.assertEqual(response.getcode(), 204)

	def test_get_sponsor_events (self):
		request = Request("http://sxswe.apiary-mock.com/api/sponsors/{id}/events")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		response_dict = loads(response_body)

		expected = [WOODIE]

		self.assertEqual(response.getcode(), 200)
		self.assertTrue(expected == response_dict)

	def test_get_sponsor_artists (self):
		request = Request("http://sxswe.apiary-mock.com/api/sponsors/{id}/artists")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		response_dict = loads(response_body)
		
		expected = [CHILDISH_GAMBINO]

		self.assertEqual(response.getcode(), 200)
		self.assertTrue(expected == response_dict)

	# EVENTS
	def test_get_events (self):
		request = Request("http://sxswe.apiary-mock.com/api/events")
		response_body = urlopen(request).read().decode("utf-8")
		response = loads(response_body)
		expected = WOODIE_SMALL
		self.assertTrue(expected == response)

	def test_get_event (self):
		request = Request("http://sxswe.apiary-mock.com/api/events/{id}")
		response_body = urlopen(request).read().decode("utf-8")
		response = loads(response_body)
		expected = WOODIE
		self.assertTrue(expected == response)

	def test_post_events (self):
		values = dumps(WOODIE).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://sxswe.apiary-mock.com/api/events", data=values, headers=headers)
		response = urlopen(request)
		response_body = response.read().decode("utf-8")

		expected = RESPONSE_1

		self.assertEqual(response.getcode(), 201)
		self.assertTrue(expected == response_body)

	def test_put_events (self):
		values = dumps(WOODIE).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://sxswe.apiary-mock.com/api/events/{id}", data=values, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)

		response_body = response.read()
		
		self.assertEqual(response.getcode(), 204)

	def test_delete_events (self):
		request = Request("http://sxswe.apiary-mock.com/api/events/{id}")
		request.get_method = lambda: 'DELETE'

		response = urlopen(request)
		response_body = response.read()
		
		self.assertEqual(response.getcode(), 204)

	def test_get_events_sponsors (self):
		request = Request("http://sxswe.apiary-mock.com/api/events/{id}/sponsors")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		response_dict = loads(response_body)

		expected = [DELL]

		self.assertEqual(response.getcode(), 200)
		self.assertTrue(expected == response_dict)

	def test_get_events_artists (self):
		request = Request("http://sxswe.apiary-mock.com/api/events/{id}/artists")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		response_dict = loads(response_body)
		
		expected = [CHILDISH_GAMBINO]

		self.assertEqual(response.getcode(), 200)
		self.assertTrue(expected == response_dict)

print ("SXSWE-tests.py")

print("Done.")