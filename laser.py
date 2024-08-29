import requests
import time
from easySteering import *


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

def get_current_coordinates():
    url = "http://192.168.100.18:2010/pos"
    response = requests.get(url)
    return response.json()

def goToComet(x, y):
    flyToCoordinates(x, y)

configure_oauth()

goToComet(-10000, 20500)

#changeToIdle()

while True:
    activate_laser()
    time.sleep(10)
