# -*- coding: utf-8 -*-
import wx
import wx.lib.plot as plt
import numpy as np

from _cfg import *

class Axes(plt.PlotCanvas):
    """
    Axes is a class inherited from `wx.lib.plot.PlotCanvas`
    
    Parameters
    ----------
    
    parent : `wx.Frame`, `wx.Panel`
        Parent object
        
    """
    def __init__(self,parent,**kwargs):
        plt.PlotCanvas.__init__(self,parent,**kwargs)
        self.SetBackgroundColour(AXES_BGCOLOR)
        self.lines = []
        self.title = ""
        self.xlabel = ""
        self.ylabel = ""
    
    def plot(self,x,y,color="k",legend="", **kwargs):
        """
        Plot a line from x and y coordinates, with legend and color 
        specified.
        """
        data = zip(x,y)
        self.lines.append(plt.PolyLine(data, legend=legend, colour=color, **kwargs))
        
    def draw(self):
        """
        Draw all lines in the current axes
        """
        self.Draw(plt.PlotGraphics(self.lines, self.title, self.xlabel, self.ylabel))
        
    def set_xlabel(self,label):
        """
        Set the x-axis label
        """
        self.xlabel = label
    
    def set_ylabel(self,label):
        """
        Set the y-axis label
        """
        self.ylabel = label
        
    def set_title(self,title):
        """
        Set the axes title
        """
        self.title = title
        
    def legend(self,status=True):
        """
        Show or hide legend line.
        """
        self.SetEnableLegend(status)
        
    def grid(self,status=True):
        """
        Show or hide axes grid.
        """
        self.SetEnableGrid(status)
        
    def save(self,filename):
        """
        Save current plot to filename
        """
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
                ax.draw()
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
