import requests
from easySteering import *
from communication import *

result = flyTo("Vesta Station")
print(result)

result = buy("Vesta Station", "IRON", 100)
print(result)

result = sell("Core Station", "GOLD", 1)
print(result)