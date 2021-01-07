import wx

class ImgPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        

class ImgFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='MP3 Tag Editor')