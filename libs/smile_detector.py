#!/usr/bin/env python3
from __future__ import print_function
# from imutils.video.pivideostream import PiVideoStream
from imutils.video.videostream import VideoStream as PiVideoStream
import time
import datetime
import numpy as np
import cv2
import imutils

'''
Original
https://github.com/kankburhan/OpenCVResearch/blob/master/SmileObj/smile.py
'''

class SimpleStreamer(object):

    def __init__(self, flip = True):
        self.vs = PiVideoStream(resolution=(800, 608)).start()
        self.flip = flip
        time.sleep(2.0)

        # opencvの顔分類器(CascadeClassifier)をインスタンス化する
        self.face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
        self.smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')

    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        frame = self.process_image(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def process_image(self, frame):
        # opencvでframe(カラー画像)をグレースケールに変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 上記でグレースケールに変換したものをインスタンス化した顔分類器の
        # detectMultiScaleメソッドで処理し、認識した顔の座標情報を取得する
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.07,
            minNeighbors=8,
            minSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # import pdb; pdb.set_trace()
        
        # 取得した座標情報を元に、cv2.rectangleを使ってframe上に
        # 顔の位置を描画する
        for (x,y,w,h) in faces:
            try:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            except:
                print("Some error")
                pass
            face_gray = gray[y:(y+h),x:(x+w)]
            face_color = frame[y:(y+h),x:(x+w)]
            smiles = self.smile_cascade.detectMultiScale(
                face_gray,
                scaleFactor= 1.5,
                minNeighbors=22,
                minSize=(50, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            
            for (x, y, w, h) in smiles:
                # print("Found"+ str(len(smiles))+ "smiles!")
                cv2.putText(
                    face_color, 
                    "Found {} smiles".format(str(len(smiles))), 
                    (x,y), 
                    cv2.FONT_HERSHEY_PLAIN, 
                    2, 
                    (0,200,0),
                    2
                )
                cv2.rectangle(face_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
            if len(smiles)>0:
                cv2.imwrite("output/face_{}.png".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S")), face_color)

        # frameを戻り値として返す
        return frame
