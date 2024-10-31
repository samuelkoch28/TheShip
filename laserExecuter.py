from laser import *


while True:
    for i in range(5):
        activate_laser()
        time.sleep(11)
    deactivate_laser()