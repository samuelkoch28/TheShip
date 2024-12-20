import requests
import asyncio
from navigation import *
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

    response = requests.post(url, json=data)

    distance = 100
    while(distance > 100):
        distance = getDistance(x, y)
        print(distance)

    return response.json()

def changeToIdle():
    url = "http://192.168.100.18:2009/set_target"
    data = {"target": "idle"}

    repsponse = requests.post(url, json=data)
    return repsponse.json()


def changeToStop():
    url = "http://192.168.100.18:2009/set_target"
    data = {"target": "stop"}

    repsponse = requests.post(url, json=data)
    return repsponse.json()
