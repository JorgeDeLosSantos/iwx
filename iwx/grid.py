# -*- coding: utf-8 -*-
import wx
import wx.aui as aui
import wx.grid as grid
import wx.lib.scrolledpanel as scrolled
import os
import numpy as np

from utils import *


class DataGrid(grid.Grid):
    """
    Create a wx.grid.Grid based grid, with other features, 
    as add and delete rows and columns interactively.
    """
    def __init__(self,parent,gridsize,**kwargs):
        grid.Grid.__init__(self,parent=parent,id=-1,**kwargs)
        rows = int(gridsize[0])
        cols = int(gridsize[1])
        self.CreateGrid(rows,cols)
        self.SetRowLabelSize(20)
        
        self.Bind(grid.EVT_GRID_CELL_CHANGE, self.OnCellEdit)
        self.Bind(grid.EVT_GRID_CELL_RIGHT_CLICK, self.OnRightClick)
        
    def UpdateGridSize(self,rows,cols):
        self.ClearGrid()
        ccols = self.GetNumberCols()
        crows = self.GetNumberRows()
        
        if rows > crows:
            self.AppendRows(rows-crows)
        elif rows < crows:
            self.DeleteRows(0,crows-rows)
            
        if cols > ccols:
            self.AppendCols(cols-ccols)
        elif cols < ccols:
            self.DeleteCols(0,ccols-cols)
            
    def SetArrayData(self,data):
        """
        Data must be a numpy array
        """
        r,c = data.shape # For numpy array
        self.UpdateGridSize(r,c)
        for i in range(r):
            for j in range(c):
                val = str(data[i][j])
                self.SetCellValue(i,j,val)
        
    def GetArrayData(self):
        nrows = self.GetNumberRows()
        ncols = self.GetNumberCols()
        X = np.zeros((nrows,ncols))
        for i in range(nrows):
            for j in range(ncols):
                cval = self.GetCellValue(i,j)
                if not isempty(cval):
                    try:
                        X[i][j] = float(cval)
                    except:
                        # Revisar valores devueltos
                        X[i][j] = np.nan
                else:
                    X[i][j] = np.nan
        return X
        
    def GetSelectedData(self):
        scols = self.GetSelectedCols()
        srows = self.GetSelectedRows()
        X = np.zeros((len(srows),len(scols)))
        for ii,row in enumerate(srows):
            for jj,col in enumerate(scols):
                try:
                    X[ii][jj] = self.GetCellValue(row,col)
                except ValueError:
                    X[ii][jj] = np.nan
        return X
                
        
    def GetSelectedCols(self):
        scols = []
        top_left = self.GetSelectionBlockTopLeft()
        bottom_right = self.GetSelectionBlockBottomRight()
        if not isempty(bottom_right) and not isempty(top_left):
            max_col = bottom_right[0][1]
            min_col = top_left[0][1]
            scols = range(min_col,max_col+1)
        return scols
        
    def GetSelectedRows(self):
        srows = []
        top_left = self.GetSelectionBlockTopLeft()
        bottom_right = self.GetSelectionBlockBottomRight()
        if not isempty(bottom_right) and not isempty(top_left):
            max_row = bottom_right[0][0]
            min_row = top_left[0][0]
            srows = range(min_row,max_row+1)
        return srows
        
    def OnCellEdit(self,event):
        """
        """
        row,col = (event.GetRow(),event.GetCol())
        cval = self.GetCellValue(row,col)
        if cval.startswith("="):
            try:
                cval = str(eval(cval[1:]))
                self.SetCellValue(row,col,cval)
            except:
                pass
        try:
            cval = float(cval)
        except ValueError:
            cval = np.nan
        self.SetCellValue(row,col,str(cval))
        
            
    def OnRightClick(self,event):
        pum = wx.Menu()
        delrows = wx.MenuItem(pum, -1, "Delete rows")
        pum.AppendItem(delrows)
        delcols = wx.MenuItem(pum, -1, "Delete columns")
        pum.AppendItem(delcols)
        pum.AppendSeparator()
        addrow = wx.MenuItem(pum, -1, "Add row...")
        pum.AppendItem(addrow)
        addcol = wx.MenuItem(pum, -1, "Add column...")
        pum.AppendItem(addcol)
        pum.AppendSeparator()
        randomfill = wx.MenuItem(pum, -1, "Randomly fill columns")
        pum.AppendItem(randomfill)
        
        # Binds
        pum.Bind(wx.EVT_MENU, self.del_rows, delrows)
        pum.Bind(wx.EVT_MENU, self.del_cols, delcols)
        pum.Bind(wx.EVT_MENU, self.add_row, addrow)
        pum.Bind(wx.EVT_MENU, self.add_col, addcol)
        pum.Bind(wx.EVT_MENU, self.random_fill, randomfill)
        
        # Show 
        self.PopupMenu(pum)
        pum.Destroy()

    def del_rows(self,event):
        rows = self.GetSelectedRows()
        self.DeleteRows(rows[0],len(rows))
        
    def del_cols(self,event):
        cols = self.GetSelectedCols()
        self.DeleteCols(cols[0],len(cols))
        
    def add_row(self,event):
        self.AppendRows(1)
        
    def add_col(self,event):
        self.AppendCols(1)
    
    def random_fill(self,event):
        cols = self.GetSelectedCols()
        nrows = self.GetNumberRows()
        for ii in range(nrows):
            for col in cols:
                val = str(np.random.rand())
                self.SetCellValue(ii,col,val)
        

        
if __name__=='__main__':
    app = wx.App()
    fr = wx.Frame(None, -1, u"ABC")
    dp = DataPanel(fr)
    fr.Show()
    app.MainLoop()
