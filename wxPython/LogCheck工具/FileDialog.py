#!/usr/bin/python
 
import wx
 
def onButton(event):
    print("Button pressed.")
 
app = wx.App()
 
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,200,50)
 
# Create open file dialog
openFileDialog = wx.FileDialog(frame, "Open", "", "", 
                                      "(*.log)|*.log", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
 
openFileDialog.ShowModal()

print(openFileDialog.GetPath())
openFileDialog.Destroy()