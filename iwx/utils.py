# -*- coding: utf-8 -*-
import numpy as np


def isempty(iterable):
    """
    Return True if iterable is a empty object.
    
    iterable : list,tuple,str
        Iterable object
    
    """
    if not iterable:
        return True
    else:
        return False


def rgb2hex(r,g,b):
    """
    Convert a RGB vector to hexadecimal values
    """
    hexfmt = "#%02x%02x%02x"%(r,g,b)
    return hexfmt


def hex2rgb(hexstr):
    """
    Convert a hexadecimal color format to RGB array
    """
    _str = hexstr.lstrip("#")
    rgb = [int(_str[k:k+2],16) for k in range(0,len(_str),2)]
    return rgb
    

def testing_utils():
    assert(rgb2hex(0,0,0)=="#000000")
    assert(rgb2hex(0.0,0.0,255.0)=="#0000ff")
    assert(isempty('') is True)
    assert(isempty([1,2,3]) is False)
    assert(isempty("abc") is False)
    assert(isempty("") is True)
        
        
if __name__=='__main__':
    hex2rgb("#ff00ff")
    
