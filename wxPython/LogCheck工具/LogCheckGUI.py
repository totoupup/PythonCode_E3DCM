# -*- coding: utf-8 -*-
# =============================================================================
#                   输入文件——点选、复制、拖拽
# 
# =============================================================================
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
        
        #self.statictext = wx.StaticText(parent=panel,label="open log",pos=(60,20))#创建静态文本对象
        
        self.filepath_text = wx.TextCtrl(parent=panel,value="",pos=(60,40),size=(350,25))#【文本控件1】
        
        open_button = wx.Button(parent=panel, label='Open',pos=(430,40))#【按钮控件1】
        
        check_button = wx.Button(parent=panel, label='Check',pos=(60,85))#【按钮控件2】
        
        clear_button = wx.Button(parent=panel, label='Clear',pos=(330,85))#【按钮控件3】
        
        self.log_text = wx.TextCtrl(parent=panel,pos=(60,120),size=(450,200),style=wx.TE_MULTILINE)#【文本控件2】
        
        self.Bind(wx.EVT_BUTTON, self.onButton_open, open_button)#绑定事件1
        
        self.Bind(wx.EVT_BUTTON, self.onButton_check, check_button)#绑定事件2
        
        self.Bind(wx.EVT_BUTTON, self.onButton_clear, clear_button)#绑定事件3
        
        self.Bind(wx.EVT_TEXT, self.text_record, self.filepath_text)#绑定事件4
        
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
        openFileDialog = wx.FileDialog(None, "...", "", "", 
                                              "(*.log)|*.log", 
                                               wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
         
        openFileDialog.ShowModal()
        self.path = openFileDialog.GetPath()        
        print(self.path)
        
        openFileDialog.Destroy()
        self.filepath_text.SetValue(self.path)#将路径显示在文本框1中
        
        self.log_text.Clear()
        return self.path    
    
    def text_record(self,event):
        self.path = self.filepath_text.GetValue()
    
    def onButton_check(self,event):
        #error_ls=[]
        #打印出切图log中未“已修正”的数据行
        log = self.path #log文件路径
        f = open(log,'rt',encoding='UTF-8')
        log = f.readlines()
        num = 0
        for line in log:
            if '已修正' not in line:
                #error_ls.append(line)
                self.log_text.WriteText(line)
                print(line)
                num += 1
        self.log_text.WriteText("检查完成：共以上{}行数据未提示“已修正”，请确认！".format(num))       
        #error_ls.append("检查完成：共以上{}行数据未提示“已修正”，请确认！".format(num)) 
        #self.log_text.WriteText(str(error_ls))

    def onButton_clear(self,event):  
        self.log_text.Clear()
        
    
if __name__ == "__main__":    

    # #创建窗口对象
    frm = MyFrame()
    # #显示窗口
    frm.Show()       
    
    
    #进入主事件循环
    app.MainLoop()

