import requests, math, pika, json, asyncio
from easySteering import *
 
def getScannerResults():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.100.18", port=2014))
    channel = connection.channel()
 
    channel.exchange_declare(exchange='scanner/detected_objects', exchange_type='fanout')
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='scanner/detected_objects', queue=queue_name)
 
    # Warten auf eine Nachricht
    method_frame, properties, body = next(channel.consume(queue=queue_name, auto_ack=True))
   
    # Nachricht verarbeiten
    print(json.loads(body.decode('utf-8')))
 
    # Verbindung schließen
    channel.close()
    connection.close()
    return json.loads(body.decode('utf-8'))
 
asyncio.run(flyToCoordinates(13100, 13500))
while (True):
    data = getScannerResults()
    x = data[0]["pos"]["x"]
    y = data[0]["pos"]["y"]
 
    asyncio.run(flyToCoordinates(x,y))
    print(data[0])