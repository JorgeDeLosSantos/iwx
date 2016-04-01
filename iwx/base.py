# -*- coding: utf-8 -*-
import wx
from _cfg import *


class Frame(wx.Frame):
    def __init__(self,parent,title,*args,**kwargs):
        wx.Frame.__init__(self,parent=parent, id=wx.ID_ANY, title=title,*args,**kwargs)
        
        # Color property
        self.SetBGColor(FRAME_BGCOLOR)
        self.Centre(True)
        
    def SetBGColor(self, color):
        self.SetBackgroundColour(color)
        
    def GetBGColor(self):
        return self.GetBackgroundColour()
        


class Panel(wx.Panel):
    def __init__(self,parent,*args,**kwargs):
        wx.Panel.__init__(self,parent,-1, style=wx.SIMPLE_BORDER)
        
        # Color properties
        self.SetBGColor(PANEL_BGCOLOR)
        
    def SetBGColor(self, color):
        self.SetBackgroundColour(color)

    def GetBGColor(self):
        return self.GetBackgroundColour()


        
if __name__=='__main__':
    app = wx.App()
    fr = Frame(None, u"Enhancement Frame")
    bsz = wx.BoxSizer(wx.VERTICAL)
    p1 = Panel(fr)
    p2 = Panel(fr)
    bsz.Add(p1, 1, wx.EXPAND)
    bsz.Add(p2, 2, wx.EXPAND)
    fr.SetSizer(bsz)
    fr.Show()
    app.MainLoop()
