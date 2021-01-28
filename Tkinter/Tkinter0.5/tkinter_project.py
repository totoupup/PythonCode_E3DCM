#coding=utf-8
import arcpy
import os
import time
from Def_Projection_ROAD import projection
from Tkinter import *   #python2没有加强版ttk模块
import tkFileDialog    #python2

root = Tk()
root.title("Projection")

#将窗口放在屏幕中央
screenWidth = root.winfo_screenwidth()  #屏幕宽度
screenHeight = root.winfo_screenheight()    #屏幕高度
Width = 300 #窗口宽
Height = 700  #窗口高
x = (screenWidth - Width)/2 #窗口左上角x轴位置
y = (screenHeight - Height)/2   #窗口左上角y轴位置

root.geometry("%dx%d+%d+%d" % (Height,Width,x,y))

#Frame

#标签组件
label_1 = Label(root,text=u" 输入文件夹 ",font="Verdana 16 bold")
label_1.grid(row=0,column=0,sticky=E)
label_2 = Label(root,text=u" 投影文件夹 ")
label_2.grid(row=1,column=0)
label_3 = Label(root,text=u" 输出文件夹 ")
label_3.grid(row=2,column=0)



#按钮控件
#输入文件夹按钮
inputDir = StringVar()
def selectInputDir():
    dir = tkFileDialog.askdirectory()   #打开文件夹，文件用askopenfilename
    inputDir.set(dir)
inputBtn = Button(root,text=u"输入文件夹",command=selectInputDir)

#投影文件夹按钮
prjDir = StringVar()
def selectPrjDir():
    dir = tkFileDialog.askdirectory()   #打开文件夹，文件用askopenfilename
    prjDir.set(dir)
prjBtn = Button(root,text=u"投影文件夹",command=selectPrjDir)

#输出文件夹按钮
outputDir = StringVar()
def selectOutputDir():
    dir = tkFileDialog.askdirectory()   #打开文件夹，文件用askopenfilename
    outputDir.set(dir)
outputBtn = Button(root,text=u"输出文件夹",command=selectOutputDir)

#按钮grid布局
inputBtn.grid(row=0,column=4)
prjBtn.grid(row=1,column=4,sticky=E)
outputBtn.grid(row=2,column=4,sticky=E)


#文本控件
inputE = Entry(root,textvariable=inputDir)
prjE = Entry(root,textvariable=prjDir)
outputE = Entry(root,textvariable=outputDir)

#文本控件布局
inputE.grid(row=0,column=1,sticky=E)#columnspan
prjE.grid(row=1,column=1)
outputE.grid(row=2,column=1)


#投影按钮command参数
x = inputE.get()
print x
# y = prjE.get()
# z = outputE.get()
# projectionBtn = Button(root,text=u"经纬度坐标转平面坐标",command=lambda:projection(x,y,z)
# # projectionBtn.grid(row=0,column=3)

# #文本控件——文件添加前缀名、后缀名
root.mainloop()