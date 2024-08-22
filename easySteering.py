import requests

def flyToName(name):
    url = "http://192.168.100.18:2009/set_target"
    data = {"target": target}

    response = requests.post(url, json=data)
    return response.json()

def flyToCoordinates(x, y):
    url = "http://192.168.100.18:2009/set_target"
    data = {"target": {"x": x, "y": y}}

    response = requests.post(url, json=data)
    return response.json()