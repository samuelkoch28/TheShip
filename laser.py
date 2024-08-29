import requests
import time
from easySteering import *

base_url = "http://192.168.100.18:2018"

oauth_config = {
    "client_secret": "JqxLU3kg74DoEVV4cVntDA0a39NtQfGn", 
    "authorize_url": "http://192.168.100.18:8080/realms/master/protocol/openid-connect/auth", 
    "token_url": "http://192.168.100.18:8080/realms/master/protocol/openid-connect/token"
}

def configure_oauth():
    url = f"{base_url}/configure_oauth"
    response = requests.post(url, json=oauth_config)
    print(response.json())

def activate_laser():
    url = f"{base_url}/activate"
    response = requests.post(url)
    print(response.json())

def get_current_coordinates():
    # Assuming there's an API to get the current coordinates
    url = f"{base_url}/current_coordinates"
    response = requests.get(url)
    return response.json()

def goToComet(x, y):
    flyToCoordinates(x, y)
    current_coords = get_current_coordinates()
    
    if current_coords["x"] == x and current_coords["y"] == y:
        changeToIdle()

configure_oauth()

goToComet(-10000, 20500)

while True:
    activate_laser()
    time.sleep(10)
