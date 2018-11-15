#!/usr/bin/env python3
'''
丸パクリ
https://qiita.com/n-yamanaka/items/91dbd7bd9fed5b3fbed4
Document
https://pypi.org/project/paho-mqtt/
'''

import os
from libs.mqtt import MqttClient

class MyClient(MqttClient):
    def on_message(self, client, userdata, msg):
        payload = str(msg.payload,'utf-8')
        if (payload=='trigger'):
            print('TRIGGERED!!!')
        else:
            print(payload)

username = os.environ.get('MQTT_USER')
password = os.environ.get('MQTT_PSW')

if __name__ == '__main__':
    client = MyClient()
    client.connect(username,password)
    client.subscribe()
