# server.py
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("Received:", msg.payload.decode())

client = mqtt.Client()
client.on_message = on_message

client.connect("broker", 1883)
client.subscribe("iot/data")

client.loop_forever()