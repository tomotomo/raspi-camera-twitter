#!/usr/bin/env python3
'''
丸パクリ
https://qiita.com/n-yamanaka/items/91dbd7bd9fed5b3fbed4
Document
https://pypi.org/project/paho-mqtt/
'''

import os
from libs.mqtt import MqttClient
from datetime import datetime
from time import sleep

username = os.environ.get('MQTT_USER')
password = os.environ.get('MQTT_PSW')

if __name__ == '__main__':
    client = MqttClient()
    client.connect(username,password)
    client.publish('Hello Mqtt :{}'.format(datetime.now()))
    sleep(10)
    client.publish('Who are you? :{}'.format(datetime.now()))
    sleep(10)
    client.publish('trigger')
