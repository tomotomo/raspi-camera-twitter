#!/usr/bin/env python3
# from imutils.video.pivideostream import PiVideoStream
from imutils.video.videostream import VideoStream as PiVideoStream
import time
import datetime
import numpy as np
import cv2


class SimpleStreamer(object):
    def __init__(self, flip = False):
        self.vs = PiVideoStream(resolution=(640, 480)).start()
        self.flip = flip
        time.sleep(2.0)

    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 1)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
