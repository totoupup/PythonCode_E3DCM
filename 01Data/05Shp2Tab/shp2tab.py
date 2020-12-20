#coding=UTF-8
##平面SHP转TAB，python2

import arcpy
import os,time
time_start = time.time()

#设置输入、输出路径
SHP_root = r"D:\PythonCode_E3DCM\01Data\05Shp2Tab\prjROAD"#设置平面SHP输入路径
TAB_root = r"D:\PythonCode_E3DCM\01Data\05Shp2Tab\prjTAB"#设置TAB输出路径

city_list = os.listdir(SHP_root)

for city in city_list:
    print city.upper()+" processing..."
    
    #RD_LINK.shp
    Input_LINK = SHP_root + "\\" + city + "\\RD_LINK.shp"  

    #RD_NODE.shp
    Input_NODE = SHP_root + "\\" + city + "\\RD_NODE.shp"

    #Output_TAB
    Output_TAB = "MITAB,"+TAB_root + "\\" + city  

    ##SHP转TAB——事先安装好ArcGIS的扩展模块Data Interoperabillity
    arcpy.QuickExport_interop(Input_LINK, Output_TAB)
    arcpy.QuickExport_interop(Input_NODE, Output_TAB)
    print city.upper()+" succeed!"
    
print "All is ok!"
 
time_end=time.time()
last = round((time_end-time_start)/60,2)
print u'TAB格式转换耗时：{:.2f}min'.format(last)

