from opcua import Client, ua

# Connect to OPC UA server
server_url = "opc.tcp://192.168.100.18:2035/"
client = Client(server_url)

try:
    client.connect()
    print("Connected to OPC UA Server")


    jumpdrive_node = client.get_node("i=20001")
    jump_to_method = client.get_node("i=20002")
    input_args = [ua.Variant(0, ua.VariantType.Int32), ua.Variant(0, ua.VariantType.Int32)]  # Example x=1, y=2
    result = jumpdrive_node.call_method(jump_to_method, *input_args)
    print("JumpTo result:", result)

    

    

finally:
    client.disconnect()
    print("Disconnected from OPC UA Server")
