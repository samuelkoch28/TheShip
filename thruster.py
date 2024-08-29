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

    repsponse = requests.put(url, json=data)
    return repsponse.json()