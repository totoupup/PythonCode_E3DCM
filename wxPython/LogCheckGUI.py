# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:03:05 2021
@author: zhutong
"""

import wx

#创建应用程序对象
app = wx.App()


#自定义窗口类MyFrame
class MyFrame(wx.Frame):
    
    def __init__(self):
        
        super().__init__(None,title="Log Check",pos=(600,300),size=(600,400))
        
        panel = wx.Panel(parent=self)#创建面板对象
        
        self.statictext = wx.StaticText(parent=panel,label="open log",pos=(60,20))#创建静态文本对象
        
        filepath_text = wx.TextCtrl(parent=panel,value="",pos=(60,50),size=(350,25))#【文本控件1】
        
        open_button = wx.Button(parent=panel, label='...',pos=(430,50))#【按钮控件】
        
        log_text = wx.TextCtrl(parent=panel,pos=(60,90),size=(450,200),style=wx.TE_MULTILINE)#【文本控件2】
        
        self.Bind(wx.EVT_BUTTON, self.onButton, open_button)#
        
        filepath_text.SetValue(self.onButton(''))
        
        
# =============================================================================
#     # def on_click(self, event):#
#     #     self.statictext.SetLabelText("log selected！")
# =============================================================================
    def onButton(self,event):#在事件源（控件）上产生特定事件（左键单击）后的处理程序        
        # Create open file dialog
        openFileDialog = wx.FileDialog(None, "Open", "", "", 
                                              "(*.log)|*.log", 
                                               wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
         
        openFileDialog.ShowModal()
        path = openFileDialog.GetPath()        
        print(path)
        
        openFileDialog.Destroy()
        
        return path        
     
    
        
    

# #创建窗口对象
frm = MyFrame()
# #显示窗口
frm.Show()       


#进入主事件循环
app.MainLoop()

