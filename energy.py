import requests
from thruster import *
import time

def omptimizeEnergy(inputData):
    url = getActiveNodeUrl()
    data = inputData

    response = requests.put(url, json=data)
    return response.json()

def getActiveNodeUrl():
    url ="http://192.168.100.18:2032/status"
    response = requests.get(url)
    if(response.json().get('role') == "active"):
        return "http://192.168.100.18:2032/limits"
    return "http://192.168.100.18:2033/limits"

def optimizeForFarming():
    print("optimizing for farming")
    data = {
    "scanner": 0.0,
    "thruster_back": 0.0,
    "thruster_front": 0.0,
    "thruster_bottom_left": 0.0,
    "thruster_front_right": 0.0,
    "thruster_bottom_right": 0.0,
    "thruster_front_left": 0.0,
    "laser": 0.4,
    "cargo_bot": 0.5,
    "sensor_void_energy": 0.0,
    "shield_generator": 0.0,
    "analyzer_alpha":0.0,
    "matter_stabilizer": 1.0,
    "sensor_atomic_field": 1.0
    }
    return omptimizeEnergy(data)

def optimizeForFlying():
    print("optimizing for flying")

    data = {
    "scanner": 0.01,
    "thruster_back": 1.0,
    "thruster_front": 0.8,
    "thruster_bottom_left": 0.8,
    "thruster_front_right": 0.8,
    "thruster_bottom_right": 0.8,
    "thruster_front_left": 0.8,
    "laser": 0.0,
    "cargo_bot": 1.0,
    "sensor_void_energy": 0.0,
    "shield_generator": 0.0,
    "analyzer_alpha": 0.0,
    "matter_stabilizer": 1.0,
    "sensor_atomic_field": 1.0
    }
    return omptimizeEnergy(data)

def optimizeForScanning():
    print("optimizing for scanning")

    data = {
    "scanner": 1.0,
    "thruster_back": 1.0,
    "thruster_front": 1.0,
    "thruster_bottom_left": 1.0,
    "thruster_front_right": 1.0,
    "thruster_bottom_right": 1.0,
    "thruster_front_left": 1.0,
    "laser": 0.0,
    "cargo_bot": 0.0,
    "sensor_void_energy": 1.0
    }
    return omptimizeEnergy(data)

def optimizeForTeleporting():
    print("optimizing for teleporting")

    data = {
    "scanner": 0.0,
    "thruster_back": 0.0,
    "thruster_front": 0.0,
    "thruster_bottom_left": 0.0,
    "thruster_front_right": 0.0,
    "thruster_bottom_right": 0.0,
    "thruster_front_left": 0.0,
    "laser": 0.0,
    "cargo_bot": 0.0,
    "sensor_void_energy": 0.0,
    "shield_generator": 0.0,
    "analyzer_alpha": 0.0,
    "jumpdrive": 0.22
    }
    return omptimizeEnergy(data)

def autoOptimize():
    if(isOneThrusterActive()):
        return optimizeForFlying()
    else:
        return optimizeForFarming()

while(True):
    print(autoOptimize())
    time.sleep(0.5)
