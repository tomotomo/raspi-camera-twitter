#!/usr/bin/env python3
'''
丸パクリ
https://qiita.com/n-yamanaka/items/91dbd7bd9fed5b3fbed4
Document
https://pypi.org/project/paho-mqtt/
'''

import  sys
from time import sleep
import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self):
        self.host = 'm15.cloudmqtt.com'
        self.port = 12724
        self.topic = 'topic_1'

        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_subscribe = self.on_subscribe


        print("*** Setup finished ***")

    def __del__(self):
        self.client.disconnect()
        print("*** Exit ***")

    def connect(self, username=None, password=None):
        # username と passwordが必要な場合
        if (username!=None):
            self.client.username_pw_set(username, password)
        self.client.connect(self.host, self.port, 60)

    def subscribe(self):
        self.client.subscribe(self.topic)
        self.client.loop_forever()

    def publish(self, message):
        self.client.publish(self.topic, message)

    def on_connect(self, client, userdata, flags, respons_code):
        print('status {0}'.format(respons_code))

    def on_message(self, client, userdata, msg):
        print(msg.topic + ' ' + str(msg.payload,'utf-8'))

    def on_publish(self, client, obj, mid):
        print("mid: " + str(mid))

    def on_subscribe(self, client, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(self, client, obj, level, string):
        print(string)

if __name__ == '__main__':
    print(__file__)
