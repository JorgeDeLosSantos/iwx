# -*- coding: utf-8 -*-
"""
CSS Styles for wxPython controls
"""
import wx
import iwx.css as css

def test():
    fr = wx.Frame(None, -1, "Test Frame", size=(300,200))
    bt = wx.Button(fr, -1, "Button")
    sz = wx.BoxSizer(wx.VERTICAL)
    sz.Add(bt, 1, wx.EXPAND|wx.ALL, 10)
    fr.SetSizer(sz)
    css.SetControlStyleSheet(bt, "#self{font-size: 16px; background-color: #00ffff;}")
    css.SetControlStyleSheet(fr, "#self{background-color: #fafafa;}")
    fr.Show()

if __name__ == '__main__':
    app = wx.App()
    test()
    app.MainLoop()
