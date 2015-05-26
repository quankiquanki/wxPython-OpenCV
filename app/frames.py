import wx
import gui
import numpy as np

from models import WebcamFeed

"""
The Controller and View class.
It creates an openCV object and on each update retrieves a webcam image from it.
It will then draw the webcam image onto the frame.
"""
class VideoFrame(gui.wxVideoFrame):

    def __init__(self, parent):
        self.parent = parent
        gui.wxVideoFrame.__init__(self, parent)
        
        """ Create the webcam feed/openCV object  """
        self.webcam = WebcamFeed()
        if not self.webcam.has_webcam():
            print 'Webcam has not been detected.'
            self.Close()
        
        """ Sets the size based on the webcam image size """
        h, w = self.webcam.size()
        self.SetSize(wx.Size(w, h))
            
        """ Creates a 30 fps timer for the update loop """
        self.timer = wx.Timer(self)
        self.timer.Start(1000./30.)
        self.Bind(wx.EVT_TIMER, self.onUpdate, self.timer)
        self.updating = False
        
        """ Bind custom paint events """
        self.m_panelVideo.Bind(wx.EVT_ERASE_BACKGROUND, self.onEraseBackground)              
        self.m_panelVideo.Bind(wx.EVT_PAINT, self.onPaint)
        
        """ Bind a custom close event (needed for Windows) """
        self.Bind(wx.EVT_CLOSE, self.onClose)
        
        """ App states """
        self.STATE_RUNNING = 1
        self.STATE_CLOSING = 2
        self.state = self.STATE_RUNNING
    
    """ When closing, timer needs to be stopped and frame destroyed """
    def onClose(self, event):
        if not self.state == self.STATE_CLOSING:
            self.state = self.STATE_CLOSING
            self.timer.Stop()
            self.Destroy()    
    
    """ Main Update loop that calls the Paint function """
    def onUpdate(self, event):
        if self.state == self.STATE_RUNNING:
            self.Refresh()
    
    """ Retrieves a new webcam image and paints it onto the frame """
    def onPaint(self, event):
        fw, fh = self.m_panelVideo.GetSize()
        # Retrieve a scaled image from the opencv model
        frame = self.webcam.get_image(fw, fh)
        h, w = frame.shape[:2]
        image = wx.BitmapFromBuffer(w, h, frame) 
        
        # Use Buffered Painting to avoid flickering
        dc = wx.BufferedPaintDC(self.m_panelVideo)
        dc.DrawBitmap(image, 0, 0)    
    
    """ Background will never be erased, this avoids flickering """
    def onEraseBackground(self, event):
        return        