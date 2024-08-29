import requests
import time
from easySteering import *
from thruster import *

def farmGold():
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

    configure_oauth()

    asyncio.run(flyToCoordinates(-10000, 20500))

    time.sleep(10)
    changeToIdle()
    time.sleep(4)
    thrusterFront(5)
    time.sleep(5)
    thrusterFront(0)

    while True:
        activate_laser()
        time.sleep(10)
