# -*- coding: utf-8 -*-
import wx
import wx.lib.plot as plt
import numpy as np
import os
import wx.lib.embeddedimage as im

from _cfg import *
from utils import *

"""
Plotting module for iwx
-----------------------

Using wxPython Pyplot to plot like Matplotlib

**MiniDemo using "plot" function**

::

    import wx
    import numpy as np
    from iwx import plot
    
    app = wx.App()
    x = np.linspace(0,5)
    y = np.cos(x)
    fig, ax = plot(x,y,width=5,show=False)
    fig.show()
    app.MainLoop()
    
Or just: ::

    import wx
    import numpy as np
    from iwx import plot
    
    app = wx.App()
    x = np.linspace(0,5)
    y = np.cos(x)
    plot(x, y)
    app.MainLoop()
    

**MiniDemo using Figure & Axes classes**
    
:: 

    import wx
    import numpy as np
    from iwx.plot import Figure, Axes

    n = 100 # Number of points
    x = np.linspace(0,3*np.pi,n)
    y1 = np.cos(x) + np.random.random(n)
    y2 = np.sin(x) + np.random.random(n)
    
    fig = Figure()
    ax = fig.add_axes()
    ax.plot(x,y1, color="#00ffff", legend="Y1", width=2)
    ax.plot(x,y2, color="#ff00ff", legend="Y2", width=3)
    ax.set_xlabel("X")
    ax.set_ylabel("y")
    ax.set_title("Graphics")
    ax.grid()
    ax.legend()
    fig.show()
"""


class Axes(plt.PlotCanvas):
    """
    Axes is a class inherited from `wx.lib.plot.PlotCanvas`
    
    parent : `wx.Frame`, `wx.Panel`
        Parent object
        
    """
    def __init__(self,parent,**kwargs):
        plt.PlotCanvas.__init__(self,parent,**kwargs)
        self.SetBackgroundColour(AXES_BGCOLOR)
        self.lines = []
        #~ self.bars = []
        self.title = ""
        self.xlabel = ""
        self.ylabel = ""
    
    def plot(self,x,y,color="k",legend="", **kwargs):
        """
        Plot a line from x and y coordinates, with legend and color 
        specified.
        
        x : ``numpy.ndarray``, ``list``, ``tuple``
            1-D Array
        y : ``numpy.ndarray``, ``list``, ``tuple``
            1-D Array
        color: ``str``, ``wx.Color``
            Line color
        legend : ``str``
            Label/legend for line
            
        """
        data = zip(x,y)
        self.lines.append(plt.PolyLine(data, legend=legend, colour=color, **kwargs))
        
    #~ def bar(self,x,data,**kwargs):
        #~ for k,dt in enumerate(data):
            #~ cdata = zip([x[k],x[k]],[0,dt])
            #~ self.bars.append(plt.PolyLine(cdata, colour='#0000FF', width=20))
            
    def draw(self):
        """
        Draw all lines in this axes
        """
        if self.lines:
            self.Draw(plt.PlotGraphics(self.lines, self.title, self.xlabel, self.ylabel))
        elif self.bars:
            self.Draw(plt.PlotGraphics(self.bars, self.title, self.xlabel, self.ylabel))
        else:
            pass
            
        
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
        Show or hide legend
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
        self.SaveFile(filename)
        


class Figure(wx.Frame):
    """
    Figure class, ``wx.Frame`` based.
    
    parent : wxPython container
        Parent object (None default)
    title  : ``str``
        Title for Figure (wxFigure default)
    
    """
    def __init__(self,parent=None,title="wxFigure",*args,**kwargs):
        wx.Frame.__init__(self,parent=parent, id=wx.ID_ANY, title=title,
                          size=(500,400),*args,**kwargs)
        
        # Icon
        self.SetIcon(fig_icon.GetIcon())
        
        # Default Sizer
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Axes
        self.axes = [] # List of axes
        
        # Color property
        self.SetBGColor(FIGURE_BGCOLOR)
        self.Centre(True)
        
    def add_axes(self):
        """
        Add an axes (currently not multiple axes supported)
        """
        ax = Axes(self)
        self.axes.append(ax)
        self.sz.Add(ax, 1, wx.EXPAND|wx.ALL, 10)
        self.SetSizer(self.sz)
        return ax
        
    def SetBGColor(self, color):
        """
        Set background color
        """
        self.SetBackgroundColour(color)
        
    def GetBGColor(self):
        """
        Get background color
        """
        return self.GetBackgroundColour()
        
    def show(self):
        """
        Draw all axes contained in the Figure and 
        call the Show method inherited from `wx.Frame`
        """
        for ax in self.axes:
            try:
                ax.draw()
            except:
                pass
        self.Show()



def plot(x,y,color="k",legend="", show=True, **kwargs):
    fig = Figure() # Create a Figure class
    ax = fig.add_axes()
    ax.plot(x,y, color=color, legend=legend, **kwargs)
    if show:
        fig.show()
    else:
        return fig, ax

        
if __name__=='__main__':
    x = np.linspace(0,5)
    y = np.cos(x)
    app = wx.App()
    fig, ax = plot(x,y,width=5,show=False)
    fig.show()
    app.MainLoop()
