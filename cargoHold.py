import requests
import time

def getCargoHold():
    url = "http://192.168.100.18:2012/hold"

    response = requests.get(url)
    return response.json()

def swapCargo(x1, y1, x2, y2):
    url = "http://192.168.100.18:2012/swap_adjacent"

    data = {"a": {"x": x1, "y": y1}, "b": {"x": x2, "y": y2}}

    response = requests.post(url, json=data)
    print(response.json())
    return response.json()

def getStructure():
    url = "http://192.168.100.18:2012/structure"
    
    response = requests.get(url)
    return response.json()

def is_cargo_full():
    cargo_hold = getCargoHold()
    hold = cargo_hold.get("hold")
    hold_free = hold.get("hold_free")

    return hold_free == 0

def optimizeStorage():
    while(True):
        structure = getStructure().get('hold')
        for rowIndex, row in enumerate(structure):
            if(rowIndex < 10):
                for itemIndex, item in enumerate(row):
                    if(itemIndex < 12 and item is not None):
                        if(structure[rowIndex + 1][itemIndex] == None):
                            swapCargo(itemIndex, rowIndex, itemIndex, rowIndex + 1)
                            time.sleep(0.42)

