import cv2
import numpy as np

import wx

class WebcamFeed(object):
    
    def __init__(self):
        self.webcam = cv2.VideoCapture(0)
		
    def has_webcam(self):
        _, frame = self.webcam.read()
        if(isinstance(frame, np.ndarray)):
            return True
        return False
            
    def get_image(self, w=None, h=None):
        _, frame = self.webcam.read()
        if w != None and h != None:
            frame = cv2.resize(frame, (w, h))
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
    def size(self):
        _, frame = self.webcam.read()
        return frame.shape[:2]