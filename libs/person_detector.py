from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from imutils.object_detection import non_max_suppression
import imutils
import time
from datetime import datetime
import numpy as np
import cv2
# twiter uploader
from .twitter_notification import upload

net = cv2.dnn.readNetFromCaffe('/home/pi/MobileNetSSD_deploy.prototxt',
        '/home/pi/MobileNetSSD_deploy.caffemodel')


class PersonDetector(object):
    def __init__(self, flip = True):
        self.vs = PiVideoStream(resolution=(640, 480)).start()
        self.flip = flip
        self.last_uploaded = datetime.now()
        time.sleep(2.0)
        
    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        # PersonDetectorはFlipしない
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        frame = self.process_image(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def process_image(self, frame):
        persons = 0
        frame = imutils.resize(frame, width=300)
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
        net.setInput(blob)
        detections = net.forward()

        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            # 認識した物体の確からしさ
            if confidence < 0.5:
                continue

            idx = int(detections[0, 0, i, 1])
            # 15は人
            if idx != 15:
                continue

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype('int')
            label = '{}: {:.2f}%'.format('Person', confidence * 100)
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            persons += 1

        # if persons > 1:
        #     timestamp = datetime.now()
        #     if (timestamp - self.last_uploaded).seconds >= 15:
        #         cv2.imwrite("image.jpg", frame)
        #         print('Uploading...')
        #         upload(persons)
        #         self.last_uploaded = timestamp
        #         print('Finished.')

        return frame
