import unittest
from urllib.request import urlopen
from urllib.request import Request
from json import dumps, loads





# -----------
# TestAPI
# -----------

class tests (unittest.TestCase) :

    # =================
    # players
    # =================
    
    # ----------
    # playerlist
    # ----------
    
    def test_player_list (self):
        try:
            request = Request("http://cs373loldbapi.apiary.io/players")
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)

        self.assertTrue(opened.status == 200)
        
        API_response = loads(response_body)
        
        expected_response = [
        { "playername": "TheOddOne", "id": 1, "summonericonid": 627 },
        { "playername": "Dyrus", "id": 2, "summonericonid": 627 },
        { "playername": "Bjergsen", "id": 3, "summonericonid": 641 },
        { "playername": "WildTurtle", "id": 4, "summonericonid": 558 },
        { "playername": "Xpecial", "id": 5, "summonericonid": 627 },
        { "playername": "Cruzerthebruzer", "id": 6, "summonericonid": 625 },
        { "playername": "Crumbzz", "id": 7, "summonericonid": 625 },
        { "playername": "scarra", "id": 8, "summonericonid": 556 },
        { "playername": "Imaqtpie", "id": 9, "summonericonid": 23 },
        { "playername": "KiWiKiD", "id": 10, "summonericonid": 556 }
        ]
        
        self.assertTrue(API_response == expected_response)                 
    
    # ---------
    # getplayer
    # ---------    
    
    def test_get_player (self):
        try:
            request = Request("http://cs373loldbapi.apiary.io/players/2")
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)
        
        self.assertTrue(opened.status == 200)
        
        API_response = loads(response_body)
        
        expected_response = [
        {
        "playername": "Dyrus",
        "id": 2,
        "teamids": [1],
        "summonerlevel": 30,
        "championkills": 3715,
        "minionkills": 90658,
        "wins": 880,
        "soloqueuedivisonid": 3,
        "region": "NA",
        "summonericonid": 627
        }
        ]
        
        self.assertTrue(API_response == expected_response)
                                               
    # ----------    
    # makeplayer
    # ----------    
    
    def test_make_player (self):
        values = dumps({ "playername": "Dyrus", "teamname": "Team SoloMid", "summonerlevel": 30, 
        "championkills": 3715, "minionkills": 90658, "wins": 880, "soloqueuedivisionname": "Vladimir's Maulers", 
        "region": "NA", "summonericonid": 627})
        
        headers = {"Content-Type": "application/json"}
        vbin = values.encode("utf-8")
        try:
            request = Request("http://cs373loldbapi.apiary.io/players", data=vbin, headers=headers)
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)

        self.assertTrue(opened.status == 201)
        
        API_response = loads(response_body)
        
        expected_response =  {"playername": "Dyrus", "id": 2} 
        
        self.assertTrue(API_response == expected_response)
    
    # ------------    
    # deleteplayer
    # ------------
    
    #change this to validate the 204 response instead
    def test_delete_player (self):
        try:
            request = Request("http://cs373loldbapi.apiary.io/players/1")
            request.get_method = lambda: 'DELETE'
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)

        self.assertTrue(opened.status == 204)
  

    # ----------        
    # editplayer
    # ----------    
    
    def test_edit_player (self):
        values = dumps({ "playername": "Dyrus", "teamname": "Team SoloMid", "summonerlevel": 30, 
        "championkills": 3715, "minionkills": 90658, "wins": 880, "soloqueuedivisionname": "Vladimir's Maulers", 
        "region": "NA", "summonericonid": 627})
        
        headers = {"Content-Type": "application/json"}
        vbin = values.encode("utf-8")
        try:
            request = Request("http://cs373loldbapi.apiary.io/players", data=vbin, headers=headers)
            request.get_method = lambda: 'PUT'
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)        
        self.assertTrue(opened.status == 204)

        
    
    # =================
    # teams
    # =================
    
    # --------
    # teamlist
    # --------
    
    def test_team_list (self):
        try:
            request = Request("http://cs373loldbapi.apiary.io/teams")
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)
        
        self.assertTrue(opened.status == 200)
        
        API_response = loads(response_body)
        
        expected_response = [ 
        { "teamname": "Team SoloMid", "id": 1, "memberids": [1,2,3,4,5], "3v3divisionid": 1, "5v5divisionid": 1, "logoid": 1 },
        { "teamname": "Team Dignitas", "id": 2, "memberids": [6,7,8,9,10], "3v3divisionid": 2, "5v5divisionid": 2, "logoid": 2 }
        ]
        
        self.assertTrue(API_response == expected_response)
    
    # -------
    # getteam
    # -------
    
    def test_get_team (self):
        try:
            request = Request("http://cs373loldbapi.apiary.io/teams/1")
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)
        
        self.assertTrue(opened.status == 200)
        
        API_response = loads(response_body)
        
        expected_response = [{ "teamname": "Team SoloMid", "id": 1, "memberids": [1,2,3,4,5], "wins": 700, "3v3divisionid": 1,
        "5v5divisionid": 1, "logoid": 1, "region": "NA" }]
        
        self.assertTrue(API_response == expected_response)
    
    # --------
    # maketeam
    # --------
    
    def test_make_team (self):
        values = dumps({ "teamname": "Team Dignitas", "memberids": [6,7,8,9,10], "wins": 500, 
                      "3v3divisionname": "Katarina's Brawlers", "5v5divisionname": "Wukong's Lancers", "logoid": 2, 
                      "region": "NA"})
        
        headers = {"Content-Type": "application/json"}
        vbin = values.encode("utf-8")
        try:
            request = Request("http://cs373loldbapi.apiary.io/teams", data=vbin, headers=headers)
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)
        
        self.assertTrue(opened.status == 201)
        
        API_response = loads(response_body)
        
        expected_response = { "teamname" : "Team Dignitas", "id": 2 }
                
        self.assertTrue(API_response == expected_response)
    
    # ----------
    # deleteteam
    # ----------   
    
    #change this to validate the 204 response instead    
    def test_delete_team (self):
        try:
            request = Request("http://cs373loldbapi.apiary.io/teams/1")
            request.get_method = lambda: 'DELETE'
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)
        self.assertTrue(opened.status == 204)
        
        
    
    # --------    
    # editteam
    # --------
    
    def test_edit_team (self):
        values = dumps({ "teamname": "Team Dignitas", "memberids": [6,7,8,9,10], "wins": 500, 
                      "3v3divisionname": "Katarina's Brawlers", "5v5divisionname": "Wukong's Lancers", "logoid": 2, 
                      "region": "NA"})
        
        headers = {"Content-Type": "application/json"}
        vbin = values.encode("utf-8")
        try:
            request = Request("http://cs373loldbapi.apiary.io/teams", data=vbin, headers=headers)
            request.get_method = lambda: 'PUT'
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)
        
        self.assertTrue(opened.status == 204)
        
        
    
    # =================
    # divisions
    # =================
    
    # ------------
    # divisionlist
    # ------------
    
    def test_division_list (self):        
        try:
            request = Request("http://cs373loldbapi.apiary.io/divisions")
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)
        
        self.assertTrue(opened.status == 200)
        
        API_response = loads(response_body)
        
        expected_response = [ 
        {"divisionname": "Hecarim's Duelists", "id": 1 },
        { "divisionname": "Wukong's Lancers", "id": 2 },
        { "divisionname": "Vladimir's Maulers", "id": 3 } 
        ] 
        
        self.assertTrue(API_response == expected_response)
    
    # -----------    
    # getdivision
    # -----------
    
    def test_get_division (self):
        try:
            request = Request("http://cs373loldbapi.apiary.io/divisions/1")
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)
        
        self.assertTrue(opened.status == 200) 
        
        API_response = loads(response_body)
        
        expected_response = [
        { "divisionname": "Hecarim's Duelists", "id": 1, "teamids": [1,10,201], 
        "tier": "Challenger", "subtier": "I", "region": "NA" }
        ]
        
        self.assertTrue(API_response == expected_response)
    
    # ------------
    # makedivision
    # ------------    
    
    def test_make_division (self):
        values = dumps({ "divisionname": "Wukong's Lancers" })
        
        headers = {"Content-Type": "application/json"}
        vbin = values.encode("utf-8")
        try:
            request = Request("http://cs373loldbapi.apiary.io/divisions", data=vbin, headers=headers)
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)
        
        self.assertTrue(opened.status == 201)
        
        API_response = loads(response_body)
        
        expected_response = { "divisionname" : "Wukong's Lancers", "id": 2}
        
        self.assertTrue(API_response == expected_response)
    
    # --------------    
    # deletedivision
    # --------------    
    
    #change this to validate the 204 response instead    
    def test_delete_division (self):
        try:
            request = Request("http://cs373loldbapi.apiary.io/divisions/1")
            request.get_method = lambda: 'DELETE'
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)
        self.assertTrue(opened.status == 204)
        
        
    
    # ------------    
    # editdivision
    # ------------
    
    def test_edit_division (self):
        values = dumps({ "divisionname": "Wukong's Lancers" })
        
        headers = {"Content-Type": "application/json"}
        vbin = values.encode("utf-8")
        try:
            request = Request("http://cs373loldbapi.apiary.io/divisions", data=vbin, headers=headers)
            request.get_method = lambda : 'PUT'
            opened = urlopen(request)            
            response_body = opened.read().decode("utf-8")
        except:
            self.assertTrue(False)
        
        self.assertTrue(opened.status == 204)
        
        

# ----
# main
# ----

print("tests.py")
unittest.main()
print("Done.")
