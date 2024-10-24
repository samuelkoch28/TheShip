from cargoHold import *


while True:
    try:
        optimizeStorage()
    except:
        print("failed")
        time.sleep(1)