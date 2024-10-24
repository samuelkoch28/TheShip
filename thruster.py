import requests

base_url = "http://192.168.100.18:2018"

oauth_config = {
    "client_secret": "JqxLU3kg74DoEVV4cVntDA0a39NtQfGn", 
    "authorize_url": "http://192.168.100.18:8080/realms/master/protocol/openid-connect/auth", 
    "token_url": "http://192.168.100.18:8080/realms/master/protocol/openid-connect/token"
}

def thrusterFront(thrustPercent):
    url = "http://192.168.100.18:2004/thruster"
    data = {"thrust_percent": thrustPercent}

    response = requests.put(url, json=data)
    return response.json()

def isOneThrusterActive():
    isOneThrusterActive = False
    urls = [
        "http://192.168.100.18:2003/thruster",
        "http://192.168.100.18:2004/thruster",
        "http://192.168.100.18:2005/thruster",
        "http://192.168.100.18:2006/thruster",
        "http://192.168.100.18:2007/thruster",
        "http://192.168.100.18:2008/thruster"
    ]
    for url in urls:
        response = requests.get(url)
        if(response.json().get('thrust_percent') > 0):
            isOneThrusterActive = True

    return isOneThrusterActive