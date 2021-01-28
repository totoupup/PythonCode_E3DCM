# coding=utf-8
# ---------------------------------------------------------------------------
# Def_Projection.py
# 输入什么，投影什么
# ---------------------------------------------------------------------------
import arcpy
import os
import time


#【修改1】
inWorkspace=u'D:/20Q3/00DATA/20Q3G2_01/'#输入文件result的上级根目录
prjdir=u'D:/PythonCode_inWork/prjFile/'#投影文件所在路径
outWorkspace=u'D:/20Q3/00DATA/prjROAD/'#投影后成果文件夹路径


def projection(inWorkspace,prjdir,outWorkspace):
    time_start=time.time()
    #带投影城市列表
    city_files=os.listdir(inWorkspace)

    num_ok = 0
    num_fail = 0
    #新建城市成果文件夹并投影
    for city_file in city_files:

        city = city_file.replace('20Q3','')#【修改2】
        
        if os.path.exists(outWorkspace + city) == False:
            os.mkdir(outWorkspace + city_file)

        print city + u"投影中..."
        #参数1：待投影文件——裁剪后link&node源数据
        RD_LINK = inWorkspace + city_file + '/RD_LINK.shp'
        RD_NODE = inWorkspace + city_file + '/RD_NODE.shp'
    
        
        #参数2：投影后输出成果文件
        prj_link = outWorkspace + city_file + '/RD_LINK.shp'
        prj_node = outWorkspace + city_file + '/RD_NODE.shp'


        #参数3：投影文件
        prj_file = prjdir+ city.lower() + '.prj' 
        
        # Process: 批量投影
        try:        
            arcpy.Project_management(RD_LINK, prj_link, prj_file)
            arcpy.Project_management(RD_NODE, prj_node, prj_file)
            print city + u"投影已成功！"
            num_ok += 1
        except:
            print city + u"投影失败！请确认！"
            num_fail += 1

    print str(num_ok)+"  ok!"
    print str(num_fail)+" fail!"
    time_end=time.time()
    print u'投影耗时：{:.2f}min'.format((time_end-time_start)/60) 

if __name__ == "__main__":
    projection(inWorkspace,prjdir,outWorkspace)