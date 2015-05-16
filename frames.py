import wx
import gui
import numpy as np

from models import WebcamFeed

class VideoFrame(gui.wxVideoFrame):

    def __init__(self, parent):
        self.parent = parent
        gui.wxVideoFrame.__init__(self, parent)
        
        # Models
        self.webcam = WebcamFeed()
        if not self.webcam.has_webcam():
            print 'Webcam has not been detected.'
            self.Close()
        
        # Set the initial size of the application based on the image size of the webcam
        h, w = self.webcam.size()
        self.SetSize(wx.Size(w, h))
            
        # Bind a Timer for frame updates
        self.timer = wx.Timer(self)
        self.timer.Start(1000./30.)
        self.Bind(wx.EVT_TIMER, self.onUpdate, self.timer)
        self.updating = False
        
        # Bind Paint events
        self.m_panelVideo.Bind(wx.EVT_ERASE_BACKGROUND, self.onEraseBackground)              
        self.m_panelVideo.Bind(wx.EVT_PAINT, self.onPaint)
        
        # App States
        self.STATE_RUNNING = 1
        self.STATE_CLOSING = 2
        self.state = self.STATE_RUNNING    
        
    def onUpdate(self, event):
        if self.state == self.STATE_RUNNING:
            self.Refresh()
        
    def onPaint(self, event):
        fw, fh = self.m_panelVideo.GetSize()
        # Retrieve a scaled image from the opencv model
        frame = self.webcam.get_image(fw, fh)
        h, w = frame.shape[:2]
        image = wx.BitmapFromBuffer(w, h, frame) 
        
        # Use Buffered Painting to avoid flickering
        dc = wx.BufferedPaintDC(self.m_panelVideo)
        dc.DrawBitmap(image, 0, 0)    
        
    def onEraseBackground(self, event):
        return        