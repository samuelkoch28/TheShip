import requests
import time
import requests
from easySteering import *

base_url = "http://192.168.100.18:2018"

oauth_config = {
    "client_secret": "JqxLU3kg74DoEVV4cVntDA0a39NtQfGn", 
    "authorize_url": "http://192.168.100.18:8080/realms/master/protocol/openid-connect/auth", 
    "token_url": "http://192.168.100.18:8080/realms/master/protocol/openid-connect/token"
}

def goToComet(x,y):
    flyToCoordinates( x,  y)

    

def configure_oauth():
    url = f"{base_url}/configure_oauth"
    response = requests.post(url, json=oauth_config)
    print(response.json())


def activate_laser():
    url = f"{base_url}/activate"
    response = requests.post(url)
    print(response.json())

configure_oauth()
goToComet(-10000, 20500)

while(True):
    activate_laser()
    time.sleep(10)
