import requests
from easySteering import *
from communication import *
from jobs import *

async def execute():
    while(True):
        await sellEverythingAtCoreStation()
        await farmPlatin()


asyncio.run(execute())