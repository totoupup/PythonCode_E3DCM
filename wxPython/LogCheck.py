# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:03:05 2021

@author: zhutong
"""

import wx

#创建应用程序对象
app = wx.App()

# =============================================================================
# #创建窗口对象
# frm = wx.Frame(None,title="Log Check",pos=(600,300),size=(500,400))
# #显示窗口
# frm.Show()
# =============================================================================

#自定义窗口类MyFrame
class MyFrame(wx.Frame):
    
    def __init__(self):
        
        super().__init__(None,title="Log Check",pos=(600,300),size=(500,400))
        
        panel = wx.Panel(parent=self)#创建面板对象
        
        self.statictext = wx.StaticText(parent=panel,label="open log",pos=(110,20))#创建静态文本对象
        
        b = wx.Button(parent=panel, label='...',pos=(100,50))
        
        self.Bind(wx.EVT_BUTTON, self.on_click, b)
        
        dialog = wx.FileDialog(parent=panel, pos=(10,50))#创建对象
        
    def on_click(self, event):#把
        self.statictext.SetLabelText("log selected！")
        
        
        
    def open_file(self, event):
        self.Filename.GetFilename()
        self.Filename.SetFilename()

frm = MyFrame()
frm.Show()        
# =============================================================================
# ❹处的super()是一个特殊函数，帮助Python将父类和子类关联起来。
# 这行代码让Python调用ElectricCar的父类的方法__init__()，让ElectricCar实例包含父类的所有属性。
# 父类也称为超类（superclass），名称super因此而得名。
# =============================================================================

#进入主事件循环
app.MainLoop()

pathtext = wx.TextCtrl(parent=panel, pos = (5,5),size = (350,24))
pathtext.GetLineText()
wx.FileDialog()

