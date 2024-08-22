import requests

def getCargoHold():
    url = "http://192.168.100.18:2012/hold"

    response = requests.get(url)
    return response.json()