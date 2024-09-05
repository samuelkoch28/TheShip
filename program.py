import requests
from easySteering import *
from communication import *
from jobs import *

async def execute():
    optimizeStorage()
    while(True):
        await sellEverythingAtCoreStation()
        await buyIron()

asyncio.run(execute())