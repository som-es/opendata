import requests
import json

url = "https://www.parlament.gv.at/Filter/api/json/post?jsMode=EVAL&FBEZ=WFP_007&listeId=11070&showAll=true"
headers = {"Content-Type": "application/json", "Accept": "application/json"}

def handle_response(response):
    if response.status_code == 200:
        return response.json()
    
    return None

def get_sitzungen(gp: str):
    payload = {"MODUS": ["PLENAR"], "NRBRBV": ["NR"], "GP": [gp]}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return handle_response(response)

def get_gegenstand_info(gegenstand_path: str):
    gegenstand_url = f"https://www.parlament.gv.at{gegenstand_path}?json=True"
    response = requests.get(gegenstand_url)
    return handle_response(response)


# GP: Gesetzgebungsperiode

#gps = ["XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII"]
gps = ["XXVII"]

for gp in gps:
    data = get_sitzungen(gp)

#    gegenstaende = data["rows"]
    for gegenstand in data["rows"]:
        gegenstand_path = gegenstand[8]
        
        gegenstand_info = get_gegenstand_info(gegenstand_path)

        if not gegenstand_info:
            continue

        # ...
