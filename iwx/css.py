# -*- coding: utf-8 -*-
import tinycss as tcss


def get_background(prop):
    """
    BackgroundColor property
    """
    return prop
    
    
def get_font_size(prop):
    """
    Font size property
    """
    return prop
    
    
def get_font_family(prop):
    return prop
    

def parse_stylesheet(src):
    propfuns = {"background-color":get_background,
                "font-size":get_font_size,
                "font-family": get_font_family}
                
    props = {}
    css = tcss.CSSPage3Parser()
    sheet = css.parse_stylesheet(src)
    for rule in sheet.rules:
        for decl in rule.declarations:
            if decl.name in propfuns:
                props[decl.name] = propfuns[decl.name](decl.value[0].value) # 
                
    return props
    

def SetControlStyleSheet(wxCtrl, style):
    """
    A wxPython control expected
    """
    parsed = parse_stylesheet(style)
    properties = {"background-color": _SetBackgroundColor,
                  "font-size": _SetFontSize,
                  "font-family": _SetFontFaceName}
    for prop,val in parsed.items():
        if prop in properties:
            properties[prop](wxCtrl,val)


def _SetFontSize(ctrl,size):
    cfont = ctrl.GetFont()
    cfont.SetPointSize(size)
    ctrl.SetFont(cfont)
        
def _SetFontFaceName(ctrl,family):
    cfont = ctrl.GetFont()
    cfont.SetFaceName(family)
    ctrl.SetFont(cfont)
        
def _SetBackgroundColor(ctrl,color):
    ctrl.SetBackgroundColour(color)

def test():
    txt = "#self{background-color: #fafafa; font-size: 10px;}"
    print parse_stylesheet(txt)

if __name__=='__main__':
    import wx
    app = wx.App()
    fr = wx.Frame(None, -1, u"This")
    SetControlStyleSheet(fr, "#self{background-color: #ff00ff}")
    fr.Show()
    app.MainLoop()
    
