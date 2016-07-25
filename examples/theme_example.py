# -*- coding: utf-8 -*-
"""
CSS Styles for wxPython controls
"""
import wx
import iwx.css as css

def test():
    fr = wx.Frame(None, -1, "This")
    sz = wx.BoxSizer(wx.VERTICAL)
    bt = wx.Button(fr, -1, "Button")
    lb = wx.StaticText(fr, -1, "Label")
    txt = wx.TextCtrl(fr, -1, "Editable")
    css.SetControlStyleSheet(fr, "#self{background-color: #585858;}")
    
    # Add controls
    sz.Add(bt, 1, wx.EXPAND|wx.ALL, 2)
    sz.Add(lb, 1, wx.EXPAND|wx.ALL, 2)
    sz.Add(txt, 1, wx.EXPAND|wx.ALL, 2)
    
    # Styles
    btstyle = "#self{color: #e0e0e0;}"
    lbstyle = "#self{background-color: #052205; color: #fafa77;}"
    txtstyle = "#self{font-size: 20px;}"
    
    css.SetControlStyleSheet(bt, btstyle)
    css.SetControlStyleSheet(lb, lbstyle)
    css.SetControlStyleSheet(txt, txtstyle)
    
    fr.SetSizer(sz)
    fr.Centre()
    fr.Show()

if __name__ == '__main__':
    app = wx.App()
    test()
    app.MainLoop()
