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


def changeToIdle():
    url = "http://192.168.100.18:2009/set_target"
    data = {"target": "idle"}
    response = requests.post(url, json=data)
    return response.json()

def pointLaserTo(x2, y2):
    x1 = getCoordinates().get('x')
    y1 = getCoordinates().get('y')
    shipAngle = getCoordinates().get('angle')
 
    dx = x2 - x1
    dy = y2 - y1
    angle_radians = math.atan2(dy, dx)
    angle_degrees = math.degrees(angle_radians)
    angle_degrees = 360 - angle_degrees
    angle_degrees += 90
    angle_degrees -= shipAngle
    if angle_degrees < 0:
        angle_degrees += 360
   
    changeAngleTo(angle_degrees)

def changeAngleTo(alpha):
    url = "http://192.168.100.18:2018/angle"
    data = {"angle": alpha}
    response = requests.put(url, json=data)
    return response.json()
