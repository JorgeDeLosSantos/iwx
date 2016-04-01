# -*- coding: utf-8 -*-
import wx
import wx.lib.plot as plt
import numpy as np
import os
import wx.lib.embeddedimage as im

from _cfg import *
from utils import *

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
    """
    Figure class, `wx.Frame` based.
    
    Parameters
    ----------
    
    parent : wxPython container
        Parent object (None default)
        
    title  : str
        Title for Figure (wxFigure default)
    
    """
    def __init__(self,parent=None,title="wxFigure",*args,**kwargs):
        wx.Frame.__init__(self,parent=parent, id=wx.ID_ANY, title=title,
                          size=(500,400),*args,**kwargs)
        
        # Icon
        self.SetIcon(fig_icon.GetIcon())
        
        # Sizer
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Axes
        self.axes = [] # List of axes
        
        # Color property
        self.SetBGColor(FIGURE_BGCOLOR)
        self.Centre(True)
        
    def add_axes(self):
        """
        Add an axes (currently not multiple axes support)
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


        
if __name__=='__main__':
    app = wx.App()
    app.MainLoop()
