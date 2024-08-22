import requests

def sell(station, what, amount):
    url = "http://192.168.100.18:2011/sell"
    data = {"station": station, "what": what, "amount": amount}

    response = requests.post(url, json=data)
    return response.json()

def buy(station, what, amount):
    url = "http://192.168.100.18:2011/buy"
    data = {"station": station, "what": what, "amount": amount}

    response = requests.post(url, json=data)
    return response.json()

def getStationsInReach():
    url = "http://192.168.100.18:2011/stations_in_reach"

    response = requests.get(url)
    return response.json()