# -*- coding: utf-8 -*-
import wx
from iwx.grid import *

app = wx.App()
fr = wx.Frame(None, -1, u"Hi")
dg = DataGrid(fr,(10,2))
fr.Show()
app.MainLoop()
