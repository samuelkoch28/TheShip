import requests
import asyncio
import time
from navigation import *
from easySteering import *
from thruster import *
from laser import *
from cargoHold import *
from jobs import *

def moveShip(x, y):
    url = "http://192.168.100.18:2009/set_target"
    data = {"target": {"x": x, "y": y}}

    requests.post(url, json=data)

    distance = 21
    while(distance > 20):
        distance = getDistance(x, y)
        print(distance)

    changeToStop()
    time.sleep(2)
    changeToIdle()
    thrusterFront(8)
    time.sleep(3)
    changeToStop()

def farmMaterial():
    activate_laser()
    time.sleep(9)

    response = requests.get('http://192.168.100.18:2018/state')
    res = response.json()
    cooling = res["is_cooling_down"]

    if (cooling is True):
        print("Now Cooling")
        while cooling is True:
            response = requests.get('http://192.168.100.18:2018/state')
            res = response.json()
            cooling = res["is_cooling_down"]
            time.sleep(2)


chronotitX = 40100
chronotitY = 53134

uranX = -21500
uranY = 36500
while(True):
    moveShip(uranX, uranY)  
    while not is_cargo_full():   
        farmMaterial()
    asyncio.run(sellEverythingAtCoreStation()) 