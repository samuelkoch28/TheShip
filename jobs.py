import requests
import asyncio
from easySteering import *
from communication import *
from cargoHold import *
from laser import *
from thruster import *

async def sellEverythingAtCoreStation():
    print("flying to Core Station")
    await flyToName("Core Station")
    cargoHold = getCargoHold()
    resources = cargoHold.get('hold').get('resources')
    for i in range(10):
        for resourceName, amount in resources.items():
            sell("Core Station", resourceName, amount)

async def buyIron():
    print("flying to Vesta")
    await flyToName("Vesta Station")
    cargoHold = getCargoHold()
    holdFree = cargoHold.get('hold').get('hold_free')
    while(not holdFree == 0):
        buy("Vesta Station", "IRON", holdFree)
        cargoHold = getCargoHold()
        holdFree = cargoHold.get('hold').get('hold_free')

async def farmPlatin():
    print("flying to coordinates")
    await flyToCoordinates(50489, 77896)
    print("arrived at coordinates")
    configure_oauth()

    time.sleep(4)
    changeToIdle()
    time.sleep(4)
    thrusterFront(5)
    time.sleep(5)
    thrusterFront(0)
    cargoHold = getCargoHold()
    holdFree = cargoHold.get('hold').get('hold_free')
    while(not holdFree == 0):
        activate_laser()
        time.sleep(9) 
        cargoHold = getCargoHold()
        holdFree = cargoHold.get('hold').get('hold_free')


