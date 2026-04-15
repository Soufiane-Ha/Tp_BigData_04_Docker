import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("broker", 1883)

client.loop_start()  # 🔥 مهم

while True:
    client.publish("iot/data", "Temperature: 25C")
    print("Data sent")
    time.sleep(2)