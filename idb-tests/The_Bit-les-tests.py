#!/usr/bin/env python

from urllib.request import Request, urlopen
from json import dumps, loads
import unittest


class TestAPI(unittest.TestCase):
    #-----------------#
    # ALBUM DATA
    #-----------------#


    # 1
    # Lists the albums in the database
    #
    def test_get_albums(self):
        # Use this URL to access a mockup of the API server.
        response = urlopen("http://bitles.apiary-mock.com/api/albums")

        # Validate  HTTP status code
        self.assertEqual(response.getcode(), 200)

        #Read our response, variable-width decode utf-8, accepted by python3
        our_response = response.readall().decode("utf-8")

        #Decoding JSON. Will take a JSON string and turn it into a python dictionary.
        our_response = loads(our_response)

        expected_response = [
            {
                "id": "twist_and_shout",
                "name": "Twist and Shout",
                "artists": ["KEY_beatles"],
                "date_released": 1964,
                "labels": ["KEY_capitol"]
            }
        ]

        #Validate string
        self.assertTrue(expected_response == our_response)


    # 2
    # Displays the information for a specific album, id is the database primary key
    #
    def test_get_single_album(self):
        # Use this URL to access a mockup of the API server.
        response = urlopen("http://bitles.apiary-mock.com/api/albums/{id}")

        # Validate  HTTP status code        
        self.assertEqual(response.getcode(), 200)

        #Read our response, variable-width decode utf-8, accepted by python3
        our_response = response.readall().decode("utf-8")

        #Decoding JSON. Will take a JSON string and turn it into a python dictionary.
        our_response = loads(our_response)
        self.assertTrue(our_response["id"] == "twist_and_shout")
        self.assertTrue(our_response["name"] == "Twist and Shout")
        self.assertTrue(our_response["artists"] == ["KEY_beatles"])
        self.assertTrue(our_response["date_released"] == 1964)
        self.assertTrue(our_response["tracks"] == ["Anna (Go to Him)",
                                                   "Chains",
                                                   "Boys",
                                                   "Ask Me Why",
                                                   "Please Please Me",
                                                   "Love Me Do",
                                                   "From Me to You",
                                                   "P.S. I Love You",
                                                   "Baby It's You",
                                                   "Do You Want to Know a Secret",
                                                   "Taste of Honey",
                                                   "There's a Place",
                                                   "Twist and Shout",
                                                   "She Loves You"])
        self.assertTrue(our_response["genre"] == ["Pop"])
        self.assertTrue(our_response["peak_chart"] == None)
        self.assertTrue(our_response["videos"] == "http://www.youtube.com/watch?v=pVlr4g5-r18")
        self.assertTrue(our_response["length"] == 1903)
        self.assertTrue(our_response["labels"] == ["KEY_capitol"])
        self.assertTrue(our_response["producers"] == ["George Martin"])
        self.assertTrue(our_response["sales"] == 300000)
        self.assertTrue(
            our_response["artwork"] == "http://upload.wikimedia.org/wikipedia/en/6/61/BeatlesTwistanShoutSingle.jpg")
        self.assertTrue(our_response[
                            "sellers"] == "http://www.amazon.com/Twist-Shout-Beatles-Canadian-Pressing/dp/B00B7C0ET2/ref=sr_1_15?ie=UTF8&qid=1395101443&sr=8-15&keywords=twist+and+shout+the+beatles")
        self.assertTrue(
            our_response["description"] == "The Beatles' second album released in Canada in mono by Capitol Records.")


        # 3
        # Create a new entry for album.
        #

    def test_post_single_album(self):
        #Take a python object(dictionary) and serialize to JSON
        values = dumps({
            "id": "twist_and_shout",
            "name": "Twist and Shout",
            "artists": ["KEY_beatles"],
            "date_released": 1964,
            "tracks": ["Anna (Go to Him)",
                       "Chains",
                       "Boys",
                       "Ask Me Why",
                       "Please Please Me",
                       "Love Me Do",
                       "From Me to You",
                       "P.S. I Love You",
                       "Baby It's You",
                       "Do You Want to Know a Secret",
                       "Taste of Honey",
                       "There's a Place",
                       "Twist and Shout",
                       "She Loves You"],
            "genre": ["Pop"],
            "peak_chart": -1,
            "videos": ["http://www.youtube.com/watch?v=pVlr4g5-r18"],
            "length": 1903,
            "labels": ["KEY_capitol"],
            "producers": ["George Martin"],
            "sales": 300000,
            "artwork": ["http://upload.wikimedia.org/wikipedia/en/6/61/BeatlesTwistanShoutSingle.jpg"],
            "sellers": [
                "http://www.amazon.com/Twist-Shout-Beatles-Canadian-Pressing/dp/B00B7C0ET2/ref=sr_1_15?ie=UTF8&qid=1395101443&sr=8-15&keywords=twist+and+shout+the+beatles"],
            "description": "The Beatles' second album released in Canada in mono by Capitol Records."
        })
        headers = {"Content-Type": "application/json"}
        values = values.encode("utf-8")
        request = Request("http://bitles.apiary-mock.com/api/albums", data=values, headers=headers)

        response = urlopen(request)
        self.assertEqual(response.getcode(), 201)
        #formatting response
        our_response = response.readall().decode("utf-8")

        actual_response = '{ id: \"twist_and_shout\"}'
        self.assertEqual(our_response, actual_response)

    # 4
    # Update an existing album entry.
    #
    def test_put_album(self):
        values = dumps({
            "id": "twist_and_shout",
            "name": "Twist and Shout",
            "artists": ["KEY_beatles"],
            "date_released": 1964,
            "tracks": ["Anna (Go to Him)",
                       "Chains",
                       "Boys", "Ask Me Why",
                       "Please Please Me",
                       "Love Me Do",
                       "From Me to You",
                       "P.S. I Love You",
                       "Baby It's You",
                       "Do You Want to Know a Secret",
                       "Taste of Honey",
                       "There's a Place",
                       "Twist and Shout",
                       "She Loves You"],
            "genre": ["Pop"],
            "peak_chart": None,
            "videos": "http://www.youtube.com/watch?v=pVlr4g5-r18",
            "length": 1903,
            "labels": ["KEY_capitol"],
            "producers": ["George Martin"],
            "sales": 300000,
            "artwork": "http://upload.wikimedia.org/wikipedia/en/6/61/BeatlesTwistanShoutSingle.jpg",
            "sellers": "http://www.amazon.com/Twist-Shout-Beatles-Canadian-Pressing/dp/B00B7C0ET2/ref=sr_1_15?ie=UTF8&qid=1395101443&sr=8-15&keywords=twist+and+shout+the+beatles",
            "description": "The Beatles' second album released in Canada in mono by Capitol Records."
        })
        headers = {"Content-Type": "application/json"}
        values = values.encode("utf-8")
        request = Request("http://bitles.apiary-mock.com/api/albums/{id}", data=values, headers=headers)
        request.get_method = lambda: 'PUT'
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)


    # 5
    # Delete an existing album
    #
    def test_delete_album(self):
        request = Request("http://bitles.apiary-mock.com/api/albums/{id}")
        request.get_method = lambda: 'DELETE'
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)


    # 6
    # List all related labels
    #
    def test_get_albums_labels(self):
        response = urlopen("http://bitles.apiary-mock.com/api/albums/{id}/labels")
        self.assertEqual(response.getcode(), 200)
        our_response = response.readall().decode("utf-8")
        our_response = loads(our_response)
        expected_response = [
            {
                "id": "capitol",
                "name": "Capitol Records",
                "founded": 1942,
                "ended": -1,
                "location": "Los Angeles, CA"
            }
        ]
        self.assertTrue(expected_response == our_response)


    # 7
    # List all related artists
    #
    def test_get_albums_artists(self):
        response = urlopen("http://bitles.apiary-mock.com/api/albums/{id}/artists")
        self.assertEqual(response.getcode(), 200)
        our_response = response.readall().decode("utf-8")
        our_response = loads(our_response)
        expected_response = [
            {
                "id": "beatles",
                "band_name": "The Beatles",
                "hometown": "Liverpool, England",
                "start_year": 1960,
                "end_year": 1970
            }
        ]
        self.assertTrue(expected_response == our_response)


    #-----------------#
    # ARTIST DATA
    #-----------------#
    # 8
    # Lists the artists in the database
    #
    def test_get_artists(self):
        response = urlopen("http://bitles.apiary-mock.com/api/artists")
        self.assertEqual(response.getcode(), 200)
        our_response = response.readall().decode("utf-8")
        our_response = loads(our_response)
        expected_response = [
            {
                "id": "beatles",
                "band_name": "The Beatles",
                "hometown": "Liverpool, England",
                "start_year": 1960,
                "end_year": 1970
            }
        ]
        self.assertTrue(expected_response == our_response)


    # 9
    # Displays the information for a specific artist, id is the database primary key
    #
    def test_get_single_artist(self):
        response = urlopen("http://bitles.apiary-mock.com/api/artists/{id}")
        self.assertEqual(response.getcode(), 200)
        our_response = response.readall().decode("utf-8")
        our_response = loads(our_response)
        self.assertTrue(our_response["id"] == "beatles")
        self.assertTrue(our_response["members"] == ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"])
        self.assertTrue(our_response["band_name"] == "The Beatles")
        self.assertTrue(our_response["hometown"] == "Liverpool, England")
        self.assertTrue(our_response["start_year"] == 1960)
        self.assertTrue(our_response["end_year"] == 1970)
        self.assertTrue(our_response["albums"] == ["KEY_twist_and_shout"])
        self.assertTrue(our_response["labels"] == ["KEY_capitol"])
        self.assertTrue(our_response["images"] ==
                        "http://2.bp.blogspot.com/_xzXp2k6_nh0/TSCZBEyuudI/AAAAAAAABA4/tnOe-vsHx1w/s1600/TheBeatlesLogo2+-+copia.jpg")
        self.assertTrue(our_response["facebook"] == "https://facebook.com/thebeatles")
        self.assertTrue(our_response["twitter"] == "https://twitter.com/thebeatles")
        self.assertTrue(our_response[
                            "google_map"] == "https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=Liverpool,+England,+United+Kingdom&amp;aq=0&amp;oq=Liverpool+england&amp;sll=53.408371,-2.991573&amp;sspn=0.214685,0.506058&amp;ie=UTF8&amp;hq=&amp;hnear=Liverpool,+Merseyside,+United+Kingdom&amp;t=m&amp;z=12&amp;ll=53.408371,-2.991573&amp;output=embed")


    # 10
    # Create a new entry for artist.
    #

    def test_post_single_artist(self):
        values = dumps({
            "id": "beatles",
            "members": ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],
            "band_name": "The Beatles",
            "hometown": "Liverpool, England",
            "start_year": 1960,
            "end_year": 1970,
            "albums": ["KEY_twist_and_shout"],
            "labels": ["KEY_capitol"],
            "images": [
                "http://2.bp.blogspot.com/_xzXp2k6_nh0/TSCZBEyuudI/AAAAAAAABA4/tnOe-vsHx1w/s1600/TheBeatlesLogo2+-+copia.jpg"],
            "facebook": "https://facebook.com/thebeatles",
            "twitter": "https://twitter.com/thebeatles",
            "google_map": "https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=Liverpool,+England,+United+Kingdom&amp;aq=0&amp;oq=Liverpool+england&amp;sll=53.408371,-2.991573&amp;sspn=0.214685,0.506058&amp;ie=UTF8&amp;hq=&amp;hnear=Liverpool,+Merseyside,+United+Kingdom&amp;t=m&amp;z=12&amp;ll=53.408371,-2.991573&amp;output=embed"
        })
        headers = {"Content-Type": "application/json"}
        values = values.encode("utf-8")
        request = Request("http://bitles.apiary-mock.com/api/artists", data=values, headers=headers)

        response = urlopen(request)
        self.assertEqual(response.getcode(), 201)
        our_response = response.readall().decode("utf-8")

        actual_response = '{ id: \"beatles\"}'
        self.assertEqual(our_response, actual_response)

    # 11
    # Update an existing artist
    #
    def test_put_artist(self):
        values = dumps({
            "id": "beatles",
            "members": ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],
            "band_name": "The Beatles",
            "hometown": "Liverpool, England",
            "start_year": 1960,
            "end_year": 1970,
            "albums": ["KEY_twist_and_shout"],
            "labels": ["KEY_capitol"],
            "images": [
                "http://2.bp.blogspot.com/_xzXp2k6_nh0/TSCZBEyuudI/AAAAAAAABA4/tnOe-vsHx1w/s1600/TheBeatlesLogo2+-+copia.jpg"],
            "facebook": "https://facebook.com/thebeatles",
            "twitter": "https://twitter.com/thebeatles",
            "google_map": "https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=Liverpool,+England,+United+Kingdom&amp;aq=0&amp;oq=Liverpool+england&amp;sll=53.408371,-2.991573&amp;sspn=0.214685,0.506058&amp;ie=UTF8&amp;hq=&amp;hnear=Liverpool,+Merseyside,+United+Kingdom&amp;t=m&amp;z=12&amp;ll=53.408371,-2.991573&amp;output=embed"
        })
        headers = {"Content-Type": "application/json"}
        values = values.encode("utf-8")
        request = Request("http://bitles.apiary-mock.com/api/artists/{id}", data=values, headers=headers)
        request.get_method = lambda: 'PUT'
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)

    # 12
    # Delete an existing artist
    #
    def test_delete_artist(self):
        request = Request("http://bitles.apiary-mock.com/api/artists/{id}")
        request.get_method = lambda: 'DELETE'
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)


    # 13
    # List all related albums
    #
    def test_get_artists_album(self):
        response = urlopen("http://bitles.apiary-mock.com/api/artists/{id}/albums")
        self.assertEqual(response.getcode(), 200)
        our_response = response.readall().decode("utf-8")
        our_response = loads(our_response)
        expected_response = [
            {
                "id": "twist_and_shout",
                "name": "Twist and Shout",
                "artists": ["KEY_beatles"],
                "date_released": 1964,
                "labels": ["KEY_capitol"]
            }
        ]
        self.assertTrue(expected_response == our_response)


    # 14
    # List all related labels
    #
    def test_get_artists_labels(self):
        response = urlopen("http://bitles.apiary-mock.com/api/artists/{id}/labels")
        self.assertEqual(response.getcode(), 200)
        our_response = response.readall().decode("utf-8")
        our_response = loads(our_response)
        expected_response = [
            {
                "id": "capitol",
                "name": "Capitol Records",
                "founded": 1942,
                "ended": -1,
                "location": "Los Angeles, CA"
            }
        ]
        self.assertTrue(expected_response == our_response)


    #-----------------#
    # LABEL DATA
    #-----------------#
    # 15
    # Lists the labels in the database
    #
    def test_get_label(self):
        response = urlopen("http://bitles.apiary-mock.com/api/labels")
        self.assertEqual(response.getcode(), 200)
        our_response = response.readall().decode("utf-8")
        our_response = loads(our_response)
        expected_response = [
            {
                "id": "capitol",
                "name": "Capitol Records",
                "founded": 1942,
                "ended": -1,
                "location": "Los Angeles, CA"
            }
        ]
        self.assertTrue(expected_response == our_response)


    # 16
    # Displays the information for a specific label, id is the database primary key
    #
    def test_get_single_label(self):
        response = urlopen("http://bitles.apiary-mock.com/api/labels/{id}")
        self.assertEqual(response.getcode(), 200)
        our_response = response.readall().decode("utf-8")
        our_response = loads(our_response)
        self.assertTrue(our_response["id"] == "capitol")
        self.assertTrue(our_response["name"] == "Capitol Records")
        self.assertTrue(our_response["albums"] == ["Bad Animals",
                                                   "KEY_twist_and_shout",
                                                   "Bazooka!!!",
                                                   "Catarsis",
                                                   "As Far as Siam",
                                                   "Honky Tonk"])
        self.assertTrue(our_response["artists"] == ["KEY_beatles",
                                                    "50_cent",
                                                    "Avicii",
                                                    "Red Hot Chili Peppers",
                                                    "Katy Perry",
                                                    "The Beach Boys"])
        self.assertTrue(our_response["founded"] == 1942)
        self.assertTrue(our_response["ended"] == -1)
        self.assertTrue(our_response["founders"] == ["Johnny Mercer", "Buddy DeSylva", "Glenn Wallichs"])
        self.assertTrue(our_response["location"] == "Los Angeles, CA")
        self.assertTrue(our_response[
                            "google_map"] == "https://maps.google.com/maps?f=q&amp;source=embed&amp;hl=en&amp;geocode=&amp;q=capitol+records&amp;aq=&amp;sll=34.098444,-118.297691&amp;sspn=0.298227,0.506058&amp;ie=UTF8&amp;hq=capitol+records&amp;hnear=&amp;t=m&amp;ll=34.098444,-118.297691&amp;spn=0.298227,0.506058")
        self.assertTrue(our_response["parent"] == "Universal Music Group")
        self.assertTrue(our_response["website"] == "http://www.capitolrecords.com/")
        self.assertTrue(our_response["logo"] == "http://upload.wikimedia.org/wikipedia/en/8/8f/CapitolRecords_Logo.png")
        self.assertTrue(our_response["facebook"] == "https://www.facebook.com/capitolrecords")
        self.assertTrue(our_response["twitter"] == "https://twitter.com/CapitolRecords")
        self.assertTrue(our_response[
                            "description"] == "Capitol Records is a major American record label that is part of the Capitol Music Group")


    # 17
    # Create a new entry for label.
    #
    def test_post_single_label(self):
        values = dumps({
            "id": "capitol",
            "name": "Capitol Records",
            "albums": ["Bad Animals",
                       "KEY_twist_and_shout",
                       "Bazooka!!!",
                       "Catarsis",
                       "As Far as Siam",
                       "Honky Tonk"],
            "artists": ["KEY_beatles",
                        "50_cent",
                        "Avicii",
                        "Red Hot Chili Peppers",
                        "Katy Perry",
                        "The Beach Boys"],
            "founded": 1942,
            "ended": -1,
            "founders": ["Johnny Mercer", "Buddy DeSylva", "Glenn Wallichs"],
            "location": "Los Angeles, CA",
            "google_map": "https://maps.google.com/maps?f=q&amp;source=embed&amp;hl=en&amp;geocode=&amp;q=capitol+records&amp;aq=&amp;sll=34.098444,-118.297691&amp;sspn=0.298227,0.506058&amp;ie=UTF8&amp;hq=capitol+records&amp;hnear=&amp;t=m&amp;ll=34.098444,-118.297691&amp;spn=0.298227,0.506058",
            "parent": "Universal Music Group",
            "website": "http://www.capitolrecords.com/",
            "logo": "http://upload.wikimedia.org/wikipedia/en/8/8f/CapitolRecords_Logo.png",
            "facebook": "https://www.facebook.com/capitolrecords",
            "twitter": "https://twitter.com/CapitolRecords",
            "description": "Capitol Records is a major American record label that is part of the Capitol Music Group"
        })
        headers = {"Content-Type": "application/json"}
        values = values.encode("utf-8")
        request = Request("http://bitles.apiary-mock.com/api/labels", data=values, headers=headers)

        response = urlopen(request)
        self.assertEqual(response.getcode(), 201)
        #formatting response
        our_response = response.readall().decode("utf-8")
        actual_response = '{ id: \"capitol\"}'
        self.assertEqual(our_response, actual_response)

    # 18
    # Update an existing label
    #
    def test_put_label(self):
        values = dumps({
            "id": "capitol",
            "name": "Capitol Records",
            "albums": ["Bad Animals",
                       "KEY_twist_and_shout",
                       "Bazooka!!!",
                       "Catarsis",
                       "As Far as Siam",
                       "Honky Tonk"],
            "artists": ["KEY_beatles",
                        "50_cent",
                        "Avicii",
                        "Red Hot Chili Peppers",
                        "Katy Perry",
                        "The Beach Boys"],
            "founded": 1942,
            "ended": -1,
            "founders": ["Johnny Mercer", "Buddy DeSylva", "Glenn Wallichs"],
            "location": "Los Angeles, CA",
            "google_map": "https://maps.google.com/maps?f=q&amp;source=embed&amp;hl=en&amp;geocode=&amp;q=capitol+records&amp;aq=&amp;sll=34.098444,-118.297691&amp;sspn=0.298227,0.506058&amp;ie=UTF8&amp;hq=capitol+records&amp;hnear=&amp;t=m&amp;ll=34.098444,-118.297691&amp;spn=0.298227,0.506058",
            "parent": "Universal Music Group",
            "website": "http://www.capitolrecords.com/",
            "logo": "http://upload.wikimedia.org/wikipedia/en/8/8f/CapitolRecords_Logo.png",
            "facebook": "https://www.facebook.com/capitolrecords",
            "twitter": "https://twitter.com/CapitolRecords",
            "description": "Capitol Records is a major American record label that is part of the Capitol Music Group"
        })
        headers = {"Content-Type": "application/json"}
        values = values.encode("utf-8")
        request = Request("http://bitles.apiary-mock.com/api/labels/{id}", data=values, headers=headers)
        request.get_method = lambda: 'PUT'
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)

    # 19
    # Create a new entry for a label.
    #
    def test_delete_labels(self):
        request = Request("http://bitles.apiary-mock.com/api/labels/{id}")
        request.get_method = lambda: 'DELETE'
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)


    # 20
    # List all related albums
    #
    def test_get_labels_albums(self):
        response = urlopen("http://bitles.apiary-mock.com/api/labels/{id}/albums")
        self.assertEqual(response.getcode(), 200)
        our_response = response.readall().decode("utf-8")
        our_response = loads(our_response)
        expected_response = \
            [
                {
                    "id": "twist_and_shout",
                    "name": "Twist and Shout",
                    "artists": ["KEY_beatles"],
                    "date_released": 1964,
                    "labels": ["KEY_capitol"]
                }
            ]
        self.assertTrue(expected_response == our_response)


    # 21
    # List all related artists
    #
    def test_get_labels_artists(self):
        response = urlopen("http://bitles.apiary-mock.com/api/labels/{id}/artists")
        self.assertEqual(response.getcode(), 200)
        our_response = response.readall().decode("utf-8")
        our_response = loads(our_response)
        expected_response = \
            [
                {
                    "id": "beatles",
                    "band_name": "The Beatles",
                    "hometown": "Liverpool, England",
                    "start_year": 1960,
                    "end_year": 1970,
                    }
            ]
        self.assertTrue(expected_response == our_response)


print("tests.py")
unittest.main()
print("Done.")