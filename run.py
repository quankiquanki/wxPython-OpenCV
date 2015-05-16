import wx

from frames import VideoFrame

# Run wx App
app = wx.App(False)
frame = VideoFrame(None)
frame.Show()
app.MainLoop()