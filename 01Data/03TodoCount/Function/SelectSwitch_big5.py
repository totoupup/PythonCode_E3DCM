# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Description: 输入数据：按全区outline位置——选择导出的全范围内道路
#        处理：
#        1、按绿区outline位置选择导出——绿区道路范围内Link
#        2、反向选择导出——蓝区道路范围内Link
#        3、分别对蓝绿区数据进行sql查询统计和导出（引用TodoCount.py）
# 难点：输入、输出路径的处理
# 增加了输入要素的多版本号情况
# ---------------------------------------------------------------------------
import os,time,arcpy
from TodoCount import CountShapefile,SqlCountOutput
from SelectLayerByLocation import MakeDir
from city_dict import city_ec_dict,city_ce_dict
from config import FileDirMaker,road_version
from config import result_dir_big5,outline_green_dir,region_ls
from config import old_vno,new_vno,old_vno_altermate1,old_vno_altermate2#版本号常量
arcpy.env.overwriteOutput = True  #启用覆盖地理处理操作的输出

city_ls = [i.decode(encoding='gbk') for i in os.listdir(result_dir_big5)]
print(city_ls)

def SelectSwitchOutput(input_link_dir,outline_dir,output_link_dir_green,output_link_dir_blue):
  
  # 前提——为要素类新建图层文件lyr
  input_lyr = input_link_dir.replace(".shp",".lyr")
  print(input_lyr)
  outline_lyr = outline_dir.replace(".shp",".lyr")
  print(outline_lyr)
    
  arcpy.MakeFeatureLayer_management(input_link_dir, input_lyr)
  arcpy.MakeFeatureLayer_management(outline_dir, outline_lyr)

  # 01按绿区位置选择
  arcpy.SelectLayerByLocation_management(input_lyr, "INTERSECT", outline_lyr, "", 'NEW_SELECTION')
  # 复制导出绿区道路
  arcpy.CopyFeatures_management(input_lyr, output_link_dir_green)   #注意复制导出的输入为图层lyr

  # 02反向选择——按蓝区位置选择
  arcpy.SelectLayerByLocation_management(input_lyr, "INTERSECT", outline_lyr, "", 'SWITCH_SELECTION')
  # 复制导出蓝区道路
  arcpy.CopyFeatures_management(input_lyr, output_link_dir_blue)   #注意复制导出的输入为图层lyr


def GetOutdir(input_link_dir):
    #————————————————————————
    # 输入【版本号+道路范围内.shp】文件路径   
    # 返回【版本号+绿区\蓝区道路范围内.shp】文件路径
    # 返回文件在输入文件所在目录下——绿区\蓝区文件夹内
    #————————————————————————

    # 列出文件名
    output_link_name_green = os.path.basename(input_link_dir).replace(u"道路范围内",u"绿区道路范围内")
    output_link_name_blue = os.path.basename(input_link_dir).replace(u"道路范围内",u"蓝区道路范围内")
    # 拼接绝对路径
    output_link_dir_green = os.path.join(os.path.dirname(input_link_dir),u"绿区",output_link_name_green)
    output_link_dir_blue = os.path.join(os.path.dirname(input_link_dir),u"蓝区",output_link_name_blue)
    
    print "____________________"
    print output_link_dir_green
    print output_link_dir_blue
    print "____________________"
    
    green_blue_dirs = [output_link_dir_green,output_link_dir_blue]
    return green_blue_dirs

if __name__ == "__main__":

    time_start=time.time()

    num = 0
    for city_c in city_ls:

        #city_c = city.decode(encoding='gbk')

        # 新建绿区、蓝区文件夹
        for region in region_ls:
            # 例D:\PythonCode_inWork\23TodoCount\output\Result_big5\沈阳\道路1次\绿区
            region_dir = os.path.join(result_dir_big5,city_c,road_version,region)
            print region_dir
            MakeDir(region_dir)
            print region_dir + " created!"
        
        city_e = city_ce_dict[city_c] #city_e英文城市名，city_c中文城市名
        
        ### 输入数据1——【V1道路范围内.shp】
        # FileDirMaker()函数参数 result_dir=result_dir_big5
        # 本模块的输入数据 result_dir_big5 来自 SelectLayerByLocation.py 模块的输出数据
        dirs = FileDirMaker(city_e,old_vno,new_vno,"",result_dir_big5,"")
        dirs_altermate1 = FileDirMaker(city_e,old_vno_altermate1,new_vno,"",result_dir_big5,"")#备选路径——备选版本号1        
        dirs_altermate2 = FileDirMaker(city_e,old_vno_altermate2,new_vno,"",result_dir_big5,"")#备选路径——备选版本号2
        #input_link_dir_V1 = dirs[1][1]

        ### 输入数据2——【V2道路范围内.shp】
        input_link_dir_V2 = dirs[2][1]
        print "input_link_dir_V2:" + input_link_dir_V2

        ### 输入数据3——【Green_*_Outline.shp】
        green_outline_name = city_e + "_Green_20Q3_Submit_Outline_M.shp"
        green_outline_dir = os.path.join(outline_green_dir,green_outline_name)

        # 对V1道路范围内.shp进行蓝绿选择
        # try3种上版本版本号
        if os.path.exists(dirs[1][1]) == True:
            input_link_dir = dirs[1][1]
        
        elif os.path.exists(dirs_altermate1[1][1]) == True:
            input_link_dir = dirs_altermate1[1][1]

        elif os.path.exists(dirs_altermate2[1][1]) == True:
            input_link_dir = dirs_altermate2[1][1]
        
        print "input_link_dir_V1:" + input_link_dir
        
        try:    
            #SelectSwitchOutput(input_link_dir,outline_dir,output_link_dir_green,output_link_dir_blue)
            SelectSwitchOutput(dirs[1][1],green_outline_dir,GetOutdir(dirs[1][1])[0],GetOutdir(dirs[1][1])[1])  #V1 old_vno
        except:
            print("V1 in Road_N select failed!")

       
        # 对V2道路范围内.shp进行蓝绿选择
        try:
            SelectSwitchOutput(dirs[2][1],green_outline_dir,GetOutdir(dirs[2][1])[0],GetOutdir(dirs[2][1])[1])
        except:
            print("V2 in Road_N select failed!")


        num += 1
        print(city_e + " OK!")
    print(str(num) + " cities OK!")

    time_end=time.time()
    print(u'程序运行耗时：{:.2f}min'.format((time_end-time_start)/60)) 


