import requests
import math

def getDistance(x1, y1):
    x2 = getCoordinates().get('x')
    y2 = getCoordinates().get('y')

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance

def getCoordinates():
    url = "http://192.168.100.18:2010/pos"

    response = requests.get(url)
    return response.json().get('pos')
