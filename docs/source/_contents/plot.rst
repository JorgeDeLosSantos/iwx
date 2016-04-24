Plot
----

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


Documentation for plot module

.. automodule:: iwx.plot
   :members:
   :undoc-members:
   :show-inheritance: