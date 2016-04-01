## iwx

**iwx** is a collection of enhanced controls for wx

### Demo

#### Plot module

```python
# -*- coding: utf-8 -*-
"""
Plotting in wxPython like Matplotlib
"""

import numpy as np
import wx
from iwx.plot import Figure, Axes


def test():
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
    
if __name__ == '__main__':
    app = wx.App()
    test()
    app.MainLoop()
```

and obtain:

![](examples/images/plot.png)