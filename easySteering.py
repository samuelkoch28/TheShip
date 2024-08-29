import requests
import asyncio
from communication import *


async def flyToName(name):
    url = "http://192.168.100.18:2009/set_target"
    data = {"target": name}

    response = requests.post(url, json=data)

    stationsInReach = {}
    firstStationInReach = {}
    while(not firstStationInReach == name):
        stationsInReach = list(getStationsInReach().get("stations", {}).keys())        
        if(stationsInReach):
            firstStationInReach = stationsInReach[0]
    return response.json()

async def flyToCoordinates(x, y):
    url = "http://192.168.100.18:2009/set_target"
    data = {"target": {"x": x, "y": y}}

    stationsInReach = {}
    while(stationsInReach == {}):
        stationsInReach = getStationsInReach().get('stations')

    response = requests.post(url, json=data)
    return response.json()

def changeToIdle():
    url = "http://192.168.100.18:2009/set_target"
    data = {"target": "idle"}

    repsponse = requests.post(url, json=data)
    return repsponse.json()
    