# -*- coding: utf-8 -*-
# =============================================================================
#                   输入文件——点选、复制、拖拽
#                   选择待投影的文件夹、投影文件所在文件夹
# =============================================================================
"""
Created on Thu Feb  4 16:12:00 2021

@author: zhutong
"""

import wx

#创建应用程序对象
app = wx.App()


#自定义窗口类MyFrame
class MyFrame(wx.Frame):
    
    def __init__(self):
        
        super().__init__(None,title="通用经纬度转平面坐标工具",pos=(600,300),size=(500,400))
        
        panel = wx.Panel(parent=self)#创建面板对象
        
        #self.statictext = wx.StaticText(parent=panel,label="open log",pos=(60,20))#创建静态文本对象
        
        self.shp_text = wx.TextCtrl(parent=panel,value="待投影数据所在文件夹",pos=(60,40),size=(350,25))#【文本控件1】        
        open_shp_button = wx.Button(parent=panel, label='Open',pos=(430,40))#【按钮控件1】
        
        self.prj_text = wx.TextCtrl(parent=panel,,value="投影文件所在文件夹"pos=(60,70),size=(350,25))#【文本控件2】
        open_prj_button = wx.Button(parent=panel, label='Open',pos=(430,40))#【按钮控件2】
        
        check_button = wx.Button(parent=panel, label='经纬度转平面投影',pos=(60,85))#【按钮控件3】
        
        self.Bind(wx.EVT_BUTTON, self.onButton_open, open_shp_button)#绑定事件1
        
        self.Bind(wx.EVT_BUTTON, self.onButton_check, check_button)#绑定事件2
        
        self.Bind(wx.EVT_BUTTON, self.onButton_clear, clear_button)#绑定事件3
        
        self.Bind(wx.EVT_TEXT, self.text_record, self.shp_text)#绑定事件4
        
# =============================================================================
#         dlg = wx.MessageDialog(None, ’所选择的不是log文件!’,
#                       ’错误’, wx.YES_NO | wx.ICON_QUESTION)
#         result = dlg.ShowModal()
#         dlg.Destroy()
# =============================================================================
        
        
# =============================================================================
#     # def on_click(self, event):#
#     #     self.statictext.SetLabelText("log selected！")
# =============================================================================
    def onButton_open(self,event):#在事件源（控件）上产生特定事件（左键单击）后的处理程序        
        # Create open file dialog
        openFileDialog = wx.FileDialog(None, "Open", "", "", 
                                              "(*.log)|*.log", 
                                               wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
         
        openFileDialog.ShowModal()
        self.path = openFileDialog.GetPath()        
        print(self.path)
        
        openFileDialog.Destroy()
        self.shp_text.SetValue(self.path)#将路径显示在文本框1中
        
        self.prj_text.Clear()
        return self.path    
    

    
    def onButton_check(self,event):
   

    
if __name__ == "__main__":    

    # #创建窗口对象
    frm = MyFrame()
    # #显示窗口
    frm.Show()       
    
    
    #进入主事件循环
    app.MainLoop()

