import requests
from easySteering import *
from communication import *
from cargoHold import *


def SellEverythingAtCoreStation():
    stationsInReach = {}
    flyToName("Core Station")
    while(stationsInReach == {}):
        stationsInReach = getStationsInReach().get('stations')
    cargoHold = getCargoHold()
    resources = cargoHold.get('hold').get('resources')
    for resourceName, amount in resources.items():
        sell("Core Station", resourceName, amount)

