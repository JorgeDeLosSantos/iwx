# -*- coding: utf-8 -*-
#
#

import wx
import css
from _cfg import *

class ButtonGroup(wx.Panel):
    """
    Create a group of wx.Button arranged vertically 
    
    parent : ``wx.Frame``, ``wx.Panel``
        A wxPython container
    labels : ``list``, ``tuple``
        A list of strings
    """
    def __init__(self,parent,labels,*args,**kwargs):
        wx.Panel.__init__(self,parent,*args,**kwargs)
        self.orientation = 'vertical'
        self.labels = labels
        self.buttons = []
        
        # Initialize components
        self._initComponents()
        
    def _initComponents(self):
        """
        Initialize components
        """
        # Sizer for this
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Make buttons
        for label in self.labels:
            btn = wx.Button(self, -1, label)
            btn.SetWindowStyleFlag(wx.BORDER_NONE) # Quit border
            self.buttons.append(btn) # Append button reference to self.buttons
            self.sz.Add(btn, 1, wx.EXPAND|wx.ALL, 0) # Add to sizer
            btn.SetBackgroundStyle(wx.BG_STYLE_COLOUR) # BG style color
        
        # Config sizer
        self.SetSizer(self.sz)
        
        # Set Default BG
        DEFAULT_COLOR = self.GetBackgroundColour() # Panel color
        self.SetBackgroundColor(DEFAULT_COLOR)

        
    def SetBackgroundColor(self,color):
        """
        Set background color for each button
        """
        for button in self.buttons:
            button.SetBackgroundColour(color)
        # Main panel back-color
        self.SetBackgroundColour(color)
        
    def SetCSS(self,src):
        """
        Set style for each button
        """
        for button in self.buttons:
            css.SetControlStyleSheet(button, src)


# ============================ TESTs ==============================

def test_group_button():
    fr = wx.Frame(None, -1, u"Frame")
    sz = wx.BoxSizer(wx.VERTICAL)
    
    lbls = ('wxPython','PyQt','Pyside','PyGTK')
    bt = ButtonGroup(fr, lbls)
    
    sz.Add(bt, 1, wx.EXPAND|wx.ALL, 5)
    fr.SetSizer(sz)
    fr.Show()

# ================================================================



if __name__=='__main__':
    app = wx.App()
    test_group_button()
    app.MainLoop()
