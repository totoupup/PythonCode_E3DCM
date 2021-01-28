#coding=utf-8
import arcpy
import os
import time
from Def_Projection_common_E import projection  #python2投影函数
from Tkinter import *   #python2没有加强版ttk模块
import tkFileDialog    #python2
arcpy.env.overwriteOutput = True  #启用覆盖地理处理操作的输出

# initialdir = r"D:\03code\python\Tkinter\DATA"

root = Tk()
root.title("经纬度坐标转平面坐标")

#【将窗口放在屏幕中央】
screenWidth = root.winfo_screenwidth()  #屏幕宽度
screenHeight = root.winfo_screenheight()    #屏幕高度
Width = 300 #窗口宽
Height = 700  #窗口高
x = (screenWidth - Width)/2 #窗口左上角x轴位置
y = (screenHeight - Height)/2   #窗口左上角y轴位置

root.geometry("%dx%d+%d+%d" % (Height,Width,x,y))

#Frame
font_str = "10" #字体大小

#【标签组件】
label_1 = Label(root, text=u" 输入文件路径:",font=font_str)#
label_1.grid(row=0, column=0,sticky=E, padx=20, pady=10)
label_2 = Label(root, text=u" 投影文件路径:",font=font_str)
label_2.grid(row=1, column=0, sticky=E, padx=20, pady=10)
label_3 = Label(root, text=u" 输出文件路径:",font=font_str)
label_3.grid(row=2, column=0, sticky=E, padx=20, pady=10)

#【按钮控件】
#输入文件夹按钮
inputDir = StringVar()
def selectInputDir():
    #方法1——点选文件夹
    dir1 = tkFileDialog.askdirectory()   #打开文件夹，文件用askopenfilename，选中后返回值是文件路径
    inputDir.set(dir1)
    #方法2——使用系统剪切板【为什么没写代码就可以】
    #dir2 = TK().clipboard_get()   #打开文件夹，文件用askopenfilename，选中后返回值是文件路径
    #inputDir.set(dir2)
    
inputBtn = Button(root,text=u"选择文件夹",command=selectInputDir,font=font_str)

#投影文件夹按钮
prjDir = StringVar()
def selectPrjDir():
    dir = tkFileDialog.askdirectory()   #打开文件夹，文件用askopenfilename
    prjDir.set(dir)
prjBtn = Button(root,text=u"选择文件夹",command=selectPrjDir,font=font_str)

#输出文件夹按钮
outputDir = StringVar()
def selectOutputDir():
    dir = tkFileDialog.askdirectory()   #打开文件夹，文件用askopenfilename
    outputDir.set(dir)
outputBtn = Button(root,text=u"选择文件夹",command=selectOutputDir,font=font_str)

#按钮grid布局
inputBtn.grid(row=0,column=2, padx=20, pady=10)
prjBtn.grid(row=1,column=2,sticky=E, padx=20, pady=10)
outputBtn.grid(row=2,column=2,sticky=E, padx=20, pady=10)


#【文本控件】
inputE = Entry(root,textvariable=inputDir, width=60)
prjE = Entry(root,textvariable=prjDir, width=60)
outputE = Entry(root,textvariable=outputDir, width=60)

#文本控件布局
inputE.grid(row=0,column=1)#columnspan,sticky=E
prjE.grid(row=1,column=1)
outputE.grid(row=2,column=1)


def doProjection():
    #投影按钮command参数
    print "#############################"
    #获得目前Entry的字符串内容
    #注意1路径被复制到Entry或2点击按钮选择文件夹后，get才有内容
    x = inputE.get()  
    print x
    y = prjDir.get()
    print y
    z = outputDir.get()
    print z
    print "#############################"
    projection(x, y, z)

projectionBtn = Button(root,text=u"确定",width=16,command=doProjection)
projectionBtn.grid(row=4,column=1,padx=10,pady=30)

# #文本控件——文件添加前缀名、后缀名
root.mainloop()
