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
from Def_Projection_common_E import createPrjFile,projection
#创建应用程序对象
app = wx.App()


#自定义窗口类MyFrame
class MyFrame(wx.Frame):
    
    def __init__(self):
        
        super(MyFrame,self).__init__(None,title="通用经纬度转平面坐标工具",pos=(600,500),size=(600,300))#Python2语法
        
        panel = wx.Panel(parent=self)#创建面板对象
        
        self.statictext_shp = wx.StaticText(parent=panel,label="待投影数据所在文件夹",pos=(60,30))#创建静态文本对象
        self.statictext_shp = wx.StaticText(parent=panel,label="投影文件所在文件夹",pos=(60,80))#创建静态文本对象

        self.shp_text = wx.TextCtrl(parent=panel,value="",pos=(60,50),size=(350,25))#【文本控件1】        
        open_shp_button = wx.Button(parent=panel, label='打开',pos=(430,50))#【按钮控件1】


        
        self.prj_text = wx.TextCtrl(parent=panel,value="",pos=(60,100),size=(350,25))#【文本控件2】
        open_prj_button = wx.Button(parent=panel, label='打开',pos=(430,100))#【按钮控件2】
        
        projection_button = wx.Button(parent=panel, label='平面投影',pos=(280,140),size=(200,30))#【按钮控件3】
        
        self.Bind(wx.EVT_BUTTON, self.onButton_opendir(event=self.shp_text), open_shp_button)#绑定事件1——打开文件夹
        
        self.Bind(wx.EVT_BUTTON, self.onButton_opendir(event=self.prj_text), open_prj_button)#绑定事件2——打开文件夹
        
        self.Bind(wx.EVT_BUTTON, self.onButton_projection, projection_button)#绑定事件3——投影

        self.Bind(wx.EVT_TEXT, self.inputText, self.shp_text)#绑定事件4——直接在文本框输入路径

        self.Bind(wx.EVT_TEXT, self.inputText, self.prj_text)#绑定事件4——直接在文本框输入路径
                
        
# =============================================================================
#     # def on_click(self, event):#
#     #     self.statictext.SetLabelText("log selected！")
# =============================================================================
    def onButton_opendir(self,control):#在事件源（控件）上产生特定事件（左键单击）后的处理程序        
        # Create open file dialog
        openDirDialog = wx.DirDialog(parent=None, message="选择一个文件夹", defaultPath="", style=wx.DD_DEFAULT_STYLE)
         
        openDirDialog.ShowModal()
        self.path = openDirDialog.GetPath()        
        print(self.path)
        
        openDirDialog.Destroy()
        control.SetValue(self.path)#将路径显示在文本框1中

    def inputText(self,control):
        self.path = control.GetValue()

    def onButton_projection(self,event):
        inWorkspace = self.shp_text.GetValue()
        prjdir = self.prj_text.GetValue()
        prjWorkspace = createPrjFile(inWorkspace,add_str="prj_")#新建投影成果根目录prjWorkspace
        projection(inWorkspace,prjdir,prjWorkspace)

    
if __name__ == "__main__":
    # #创建窗口对象
    frm = MyFrame()
    # #显示窗口
    frm.Show()       
    
    
    #进入主事件循环
    app.MainLoop()

