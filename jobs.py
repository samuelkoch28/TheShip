import requests
import asyncio
from easySteering import *
from communication import *
from cargoHold import *


async def SellEverythingAtCoreStation():
    await flyToName("Core Station")
    cargoHold = getCargoHold()
    resources = cargoHold.get('hold').get('resources')
    for resourceName, amount in resources.items():
        sell("Core Station", resourceName, amount)

async def BuyIron():
    await flyToName("Vesta Station")
    cargoHold = getCargoHold()
    holdFree = cargoHold.get('hold').get('hold_free')
    buy("Vesta Station", "IRON", holdFree)
