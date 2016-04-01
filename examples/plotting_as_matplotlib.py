# -*- coding: utf-8 -*-
import numpy as np
import wx
from iwx.plot import Figure, Axes


def test_01():
    x = np.linspace(0,5,10)
    y = np.random.random(10)
    
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


def test_02():
    x = np.linspace(0,10)
    y = np.cos(x)*x
    
    fig = Figure()
    ax = fig.add_axes()
    ax.plot(x,y)
    fig.show()
    

if __name__ == '__main__':
    app = wx.App()
    test_01()
    test_02()
    app.MainLoop()
    
