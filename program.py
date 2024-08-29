import requests
from easySteering import *
from communication import *
from jobs import *

async def execute():
    while(True):
        await SellEverythingAtCoreStation()
        await BuyIron()

asyncio.run(execute())