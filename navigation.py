import requests

def getCoordinates():
    url = "http://192.168.100.18:2010/pos"

    response = requests.get(url)
    return response.json().get('pos')
