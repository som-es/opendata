import requests
import json

url = "https://www.parlament.gv.at/Filter/api/json/post?jsMode=EVAL&FBEZ=WFW_008&listeId=10008?showAll=true"

headers = {"Content-Type": "application/json", "Accept": "application/json"}

def handle_response(response):
    if response.status_code == 200:
        return response.json()
    
    return None

def get_nr_delegates(gp: str):
    payload = {"M": ["M"], "W": ["W"], "NRBR": ["NR"], "GP": [gp]}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return handle_response(response)

def get_person_info(person_path: str):
    person_url = f"https://www.parlament.gv.at{person_path}?json=True"
    response = requests.get(person_url)
    return handle_response(response)

for delegate in get_nr_delegates("XXVII")["rows"]:
    info = get_person_info(delegate[len(delegate) - 1])
    #info = json.dumps(info, indent=4)
    #print(info)
    #break
