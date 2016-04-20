# -*- coding: utf-8 -*-
import wx
import css
from _cfg import *

class ButtonGroup(wx.Panel):
    def __init__(self,parent,labels,*args,**kwargs):
        wx.Panel.__init__(self,parent,*args,**kwargs)
        self.orientation = 'vertical'
        self.labels = labels
        self.buttons = []
        
        # Init components
        self._initComponents()
        
    def _initComponents(self):
        # Sizer for this
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Make buttons
        for label in self.labels:
            btn = wx.Button(self, -1, label)
            btn.SetWindowStyleFlag(wx.BORDER_NONE)
            self.buttons.append(btn)
            self.sz.Add(btn, 1, wx.EXPAND|wx.ALL, 0)
            btn.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        
        # Config sizer
        self.SetSizer(self.sz)
        
        # Set Default BG
        DEFAULT_COLOR = self.GetBackgroundColour() # Panel color
        self.SetBackgroundColor(DEFAULT_COLOR)

        
    def SetBackgroundColor(self,color):
        """
        Set back-color for every button
        """
        for button in self.buttons:
            button.SetBackgroundColour(color)
            
        self.SetBackgroundColour(color)
        
        
    def SetCSS(self,src):
        for button in self.buttons:
            css.SetControlStyleSheet(button, src)

        

if __name__=='__main__':
    app = wx.App()
    fr = wx.Frame(None, -1, u"Enhancement Frame")
    lbls = ('wxPython','PyQt','Pyside','PyGTK')
    bt = ButtonGroup(fr, lbls)
    bt.SetCSS("#self{font-size:16px; background-color: #fafa00; font-family: 'Times New Roman';}")
    bt2 = wx.Button(fr,-1,"ABC")
    css.SetControlStyleSheet(bt2, "#self{font-size:16px; background-color: #fafa00; font-family: 'Times New Roman';}")
    sz = wx.BoxSizer(wx.VERTICAL)
    sz.Add(bt, 1, wx.EXPAND|wx.ALL, 5)
    sz.Add(bt2, 1, wx.EXPAND|wx.ALL, 5)
    fr.SetSizer(sz)
    fr.Show()
    app.MainLoop()
