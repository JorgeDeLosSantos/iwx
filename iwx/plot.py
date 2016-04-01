# -*- coding: utf-8 -*-
import wx
import wx.lib.plot as plt
import numpy as np

from _cfg import *

class Axes(plt.PlotCanvas):
    def __init__(self,parent,**kwargs):
        plt.PlotCanvas.__init__(self,parent,**kwargs)
        self.SetBackgroundColour(AXES_BGCOLOR)
        self.lines = []
        self.title = ""
        self.xlabel = ""
        self.ylabel = ""
    
    def plot(self,x,y,color="k",legend=""):
        data = zip(x,y)
        self.lines.append(plt.PolyLine(data, legend=legend, colour=color))
        
    def show(self):
        self.Draw(plt.PlotGraphics(self.lines, self.title, self.xlabel, self.ylabel))
        
    def set_xlabel(self,label):
        self.xlabel = label
    
    def set_ylabel(self,label):
        self.ylabel = label
        
    def set_title(self,title):
        self.title = title
        
    def legend(self,status=True):
        self.SetEnableLegend(status)
        
    def grid(self,status=True):
        self.SetEnableGrid(status)
        
    def save(self,filename):
        return self.SaveFile(filename)
        



class Figure(wx.Frame):
    def __init__(self,parent=None,title="wxFigure",*args,**kwargs):
        wx.Frame.__init__(self,parent=parent, id=wx.ID_ANY, title=title,
                          size=(500,400),*args,**kwargs)
        
        # Sizer
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Axes
        self.axes = []
        
        # Color property
        self.SetBGColor(FIGURE_BGCOLOR)
        self.Centre(True)
        
    def add_axes(self):
        ax = Axes(self)
        self.axes.append(ax)
        self.sz.Add(ax, 1, wx.EXPAND|wx.ALL, 10)
        self.SetSizer(self.sz)
        return ax
        
    def SetBGColor(self, color):
        self.SetBackgroundColour(color)
        
    def GetBGColor(self):
        return self.GetBackgroundColour()
        
    def show(self):
        for ax in self.axes:
            try:
                ax.show()
            except:
                pass
        self.Show()


        
if __name__=='__main__':
    x = np.linspace(0,5,10)
    y = np.random.random(10)
    
    app = wx.App()
    fig = Figure()
    ax = fig.add_axes()
    ax.plot(x,y, color="#ff00ff", legend="ACC")
    ax.plot(x,x*y, color="#ff5566", legend="DB")
    ax.set_xlabel("X")
    ax.set_ylabel("y")
    ax.set_title("ABC")
    ax.grid()
    ax.legend()
    fig.show()
    app.MainLoop()
