import wx

from app.frames import VideoFrame

""" Standard way of starting a wxPython app """
app = wx.App(False)
frame = VideoFrame(None)
frame.Show()
app.MainLoop()