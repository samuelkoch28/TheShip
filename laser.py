import requests
import time
import asyncio
from jobs import *
from easySteering import *
from thruster import *
from navigation import *
from communication import *

oauth_config = {
    "client_secret": "JqxLU3kg74DoEVV4cVntDA0a39NtQfGn", 
    "authorize_url": "http://192.168.100.18:8080/realms/master/protocol/openid-connect/auth", 
    "token_url": "http://192.168.100.18:8080/realms/master/protocol/openid-connect/token"
}

def configure_oauth():
    url = "http://192.168.100.18:2018/configure_oauth"
    response = requests.post(url, json=oauth_config)
    print(response.json())

def activate_laser():
    url = "http://192.168.100.18:2018/activate"
    response = requests.post(url)
    print(response.json())

def getCargoHold():
    url = "http://192.168.100.18:2012/hold"
    response = requests.get(url)
    return response.json()

def sell(station_name, resource_name, amount):
    url = "http://192.168.100.18:2013/sell"
    data = {"station": station_name, "resource": resource_name, "amount": amount}
    response = requests.post(url, json=data)
    return response.json()



async def flyToCoordinates(x, y):
    url = "http://192.168.100.18:2009/set_target"
    data = {"target": {"x": x, "y": y}}

    response = requests.post(url, json=data)

    distance = 100
    while distance > 20:
        distance = getDistance(x, y)
        print(f"Current distance: {distance}")
        await asyncio.sleep(1)

    return response.json()

def is_cargo_full():
    cargo_hold = getCargoHold()
    hold_free = cargo_hold.get("hold_free")
    return hold_free == 0

def changeToIdle():
    url = "http://192.168.100.18:2009/set_target"
    data = {"target": "idle"}
    response = requests.post(url, json=data)
    return response.json()

async def farmGold():
    configure_oauth()

    while True:
        print("fotze")
        await flyToCoordinates(-10000, 20500)
        print("PENIS")

        time.sleep(4)
        changeToIdle()
        time.sleep(4)
        thrusterFront(5)
        time.sleep(5)
        thrusterFront(0)


        while not is_cargo_full():
            activate_laser()
            time.sleep(10)  

        await sellEverythingAtCoreStation()

asyncio.run(farmGold())
