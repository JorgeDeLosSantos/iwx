# -*- coding: utf-8 -*-
import tinycss as tcss
from collections import namedtuple


def SetControlStyleSheet(wxCtrl, style):
    """
    Apply CSS style to wxCtrl object
    
    
    wxCtrl:  wxPython control
        A wxPython control
    
    style: ``str``
        A string with CSS style, like: ``#self{property: value}``, where 
        ``#self`` can be any string, because currently specific selectors 
        are not supported.
    """
    parsed = parse_stylesheet(style)
    properties = {"background-color": _SetBackgroundColor,
                  "font-size": _SetFontSize,
                  "font-family": _SetFontFaceName,
                  "color": _SetForegroundColor}
    for prop,val in parsed.items():
        if prop in properties:
            properties[prop](wxCtrl,val)


def parse_stylesheet(src):
    """
    Parse a stylesheet using tinycss
    
    src : ``str``
        A string like: ``"#self{property: value}"``
    """
    propfuns = {"background-color":get_background,
                "font-size":get_font_size,
                "font-family": get_font_family,
                "color": get_foreground}
                
    props = {}
    css = tcss.CSSPage3Parser()
    sheet = css.parse_stylesheet(src)
    for rule in sheet.rules:
        for decl in rule.declarations:
            if decl.name in propfuns:
                props[decl.name] = propfuns[decl.name](decl.value[0].value) # 
                
    return props
            

# ========================= get_property functions  ==================

def get_background(prop):
    """
    Background Color property
    """
    return prop
    
    
def get_font_size(prop):
    """
    Font size property
    """
    return prop
    
    
def get_font_family(prop):
    """
    Font family property
    """
    return prop
    
def get_foreground(prop):
    """
    Foreground Color property
    """
    return prop
    


# ===================== _Set* functions ======================

def _SetFontSize(ctrl,size):
    """
    Set the FontSize for a control
    """
    cfont = ctrl.GetFont()
    cfont.SetPointSize(size)
    ctrl.SetFont(cfont)


def _SetFontFaceName(ctrl,name):
    """
    Set the font name
    
    Parameters
    ----------
    
    ctrl: wxPython control
        A wxPython control
        
    name: str
        A font name, i.e. "Arial", "Courier New"
        
    """
    cfont = ctrl.GetFont()
    cfont.SetFaceName(name)
    ctrl.SetFont(cfont)

        
def _SetBackgroundColor(ctrl,color):
    """
    Set the background color
    
    Parameters
    ----------
    
    ctrl : wxPython control
        A wxPython control
    
    color : str, wx.Color
        A string or wx.Color class
    """
    ctrl.SetBackgroundColour(color)
    

def _SetForegroundColor(ctrl,color):
    """
    Set the background color
    
    Parameters
    ----------
    
    ctrl : wxPython control
        A wxPython control
    
    color : str, wx.Color
        A string or wx.Color class
    """
    ctrl.SetForegroundColour(color)


# ========================== Themes ================================

def SetTheme(container, theme):
    prop = namedtuple('Properties','container_color,control_color')
    black = prop("#101010","#595959")
    white = prop("#dadada","#f0f0f0")
    blue = prop("#7777dd","#aaaaff")
    
    if "black" in theme:
        container.SetBackgroundColour(black.container_color)
        _recursive_theme(container.GetChildren(), black)
    elif "blue" in theme:
        container.SetBackgroundColour(blue.container_color)
        _recursive_theme(container.GetChildren(), blue)
    else:
        container.SetBackgroundColour(white.container_color)
        _recursive_theme(container.GetChildren(), white)


def _recursive_theme(children, props):
    for child in children:
        print child.__class__
        if child.__class__.__name__ in ["Panel","Frame"]:
            child.SetBackgroundColour(props.container_color)
            child.Refresh()
            return self._recursive_theme(child.GetChildren(), properties)
        else: #Otherwise
            child.SetBackgroundColour(props.control_color)
            child.Refresh()


# ============================  Tests functions =====================


def test():
    import wx
    app = wx.App()
    fr = wx.Frame(None, -1, "This")
    sz = wx.BoxSizer(wx.VERTICAL)
    bt = wx.Button(fr, -1, "Button")
    lb = wx.StaticText(fr, -1, "Label")
    txt = wx.TextCtrl(fr, -1, "Editable")
    SetControlStyleSheet(fr, "#self{background-color: #585858;}")
    
    # Add controls
    sz.Add(bt, 1, wx.EXPAND|wx.ALL, 2)
    sz.Add(lb, 1, wx.EXPAND|wx.ALL, 2)
    sz.Add(txt, 1, wx.EXPAND|wx.ALL, 2)
    
    # Styles
    btstyle = "#self{color: #e0e0e0;}"
    lbstyle = "#self{background-color: #052205; color: #fafa77;}"
    txtstyle = "#self{font-size: 20px;}"
    
    SetControlStyleSheet(bt, btstyle)
    SetControlStyleSheet(lb, lbstyle)
    SetControlStyleSheet(txt, txtstyle)
    
    fr.SetSizer(sz)
    fr.Centre()
    fr.Show()
    app.MainLoop()


def test_theme():
    import wx
    app = wx.App()
    fr = wx.Frame(None, -1, "This")
    sz = wx.BoxSizer(wx.VERTICAL)
    bt = wx.Button(fr, -1, "Button")
    lb = wx.StaticText(fr, -1, "Label")
    txt = wx.TextCtrl(fr, -1, "Editable")
    
    # Add controls
    sz.Add(bt, 1, wx.EXPAND|wx.ALL, 2)
    sz.Add(lb, 1, wx.EXPAND|wx.ALL, 2)
    sz.Add(txt, 1, wx.EXPAND|wx.ALL, 2)
    
    SetTheme(fr, "blue")
    
    fr.SetSizer(sz)
    fr.Centre()
    fr.Show()
    app.MainLoop()


if __name__=='__main__':
    test_theme()
    
