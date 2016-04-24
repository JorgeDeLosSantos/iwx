# -*- coding: utf-8 -*-
import wx
from _cfg import *


class IFrame(wx.Frame):
    """
    An enhanced Frame
    """
    def __init__(self,parent,title,*args,**kwargs):
        wx.Frame.__init__(self,parent=parent, id=wx.ID_ANY, title=title,*args,**kwargs)
        
        # Color property
        self.SetBGColor(FRAME_BGCOLOR)
        self.Centre(True)
        
    def SetBGColor(self, color):
        """
        Short-version
        """
        self.SetBackgroundColour(color)
        
    def GetBGColor(self):
        return self.GetBackgroundColour()
        


class IPanel(wx.Panel):
    """
    An enhanced panel
    """
    def __init__(self,parent,*args,**kwargs):
        wx.Panel.__init__(self,parent,id=wx.ID_ANY,style=wx.SIMPLE_BORDER)
        
        # Color properties
        self.SetBGColor(PANEL_BGCOLOR)
        
    def SetBGColor(self, color):
        self.SetBackgroundColour(color)

    def GetBGColor(self):
        return self.GetBackgroundColour()


        
if __name__=='__main__':
    app = wx.App()
    fr = IFrame(None, u"Enhanced Frame")
    bsz = wx.BoxSizer(wx.VERTICAL)
    fr.Show()
    app.MainLoop()
