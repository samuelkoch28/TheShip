import asyncio
import aiohttp
import keyboard
import laser

angle = 0

thrusters = {
    "back": "http://192.168.100.18:2003/thruster",
    "bottomLeft": "http://192.168.100.18:2007/thruster",
    "bottomRight": "http://192.168.100.18:2008/thruster",
    "front": "http://192.168.100.18:2004/thruster",
    "frontLeft": "http://192.168.100.18:2005/thruster",
    "frontRight": "http://192.168.100.18:2006/thruster"
}
 
thruster_states = {key: 0 for key in thrusters}
 
async def activate_thruster(session, thruster_name, thrust_percent):
    url = thrusters.get(thruster_name)
    if url:
        data = {"thrust_percent": thrust_percent}
        async with session.put(url, json=data) as response:
            if response.status == 200:
                thruster_states[thruster_name] = thrust_percent
            else:
                print(f"Failed to update {thruster_name} (Status: {response.status})")
 
async def control_thrusters():
    async with aiohttp.ClientSession() as session:
        keys = {
            "E": ["bottomLeft", "frontRight"],
            "Q": ["bottomRight", "frontLeft"],
            "W": ["back"],
            "S": ["front"],
            "D": ["frontLeft", "bottomLeft"],
            "A": ["frontRight", "bottomRight"]
        }
        while True:
            tasks = []
            active_thrusters = set()
            global angle
            if keyboard.is_pressed("L"):
                angle += 10
                laser.changeAngleTo(angle)
            if keyboard.is_pressed("K"):
                angle -= 10
                laser.changeAngleTo(angle)

            for key, thruster_list in keys.items():
                if keyboard.is_pressed(key):
                    active_thrusters.update(thruster_list)
           
            for thruster in thrusters:
                if thruster in active_thrusters:
                    if thruster_states[thruster] != 100:
                        tasks.append(activate_thruster(session, thruster, 100))
                else:
                    if thruster_states[thruster] != 0:
                        tasks.append(activate_thruster(session, thruster, 0))
 
            if tasks:
                await asyncio.gather(*tasks)
 
            await asyncio.sleep(0.1)
 
if __name__ == "__main__":
    print("Drücke W, A, S, D, Q oder E, um das Raumschiff zu steuern. ESC zum Beenden.")
    try:
        asyncio.run(control_thrusters())
    except KeyboardInterrupt:
        print("Beenden...")