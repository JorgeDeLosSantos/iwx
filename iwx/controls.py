# -*- coding: utf-8 -*-
import wx
from _cfg import *


class Frame(wx.Frame):
    def __init__(self,parent,title,*args,**kwargs):
        wx.Frame.__init__(self,parent=parent, id=wx.ID_ANY, title=title,*args,**kwargs)
        self.SetBackgroundColour(FRAME_BGCOLOR)
        self.Centre(True)
        self.Show()




        
if __name__=='__main__':
    app = wx.App()
    fr = Frame(None, u"Enhancement Frame")
    app.MainLoop()
