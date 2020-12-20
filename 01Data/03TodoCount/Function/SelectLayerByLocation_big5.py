# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Description: 按位置选择导出Link
# 增加了输入要素的多版本号情况
# ---------------------------------------------------------------------------
import os,time,arcpy
from city_dict import city_ec_dict
from config import from_dir_big5,result_dir_big5,outline_dir,FileDirMaker,road_version #常量
from config import old_vno,new_vno,old_vno_altermate1,old_vno_altermate2#版本号常量
arcpy.env.overwriteOutput = True  #启用覆盖地理处理操作的输出


def SelectOutput(input_link_dir,outline_dir,output_tuple=(False,'')):   #output_tuple=(output_flag=False,output_shp)
  
  #前提——为要素类新建图层文件lyr
  input_lyr = input_link_dir.replace(".shp",".lyr")
  print(input_lyr)
  outline_lyr = outline_dir.replace(".shp",".lyr")
  print(outline_lyr)
    
  arcpy.MakeFeatureLayer_management(input_link_dir, input_lyr)
  arcpy.MakeFeatureLayer_management(outline_dir, outline_lyr)

  #按位置选择
  arcpy.SelectLayerByLocation_management(input_lyr, "INTERSECT", outline_lyr, "", 'NEW_SELECTION')

  #复制导出 
  if output_tuple[0]: #output_flag
    arcpy.CopyFeatures_management(input_lyr, output_tuple[1])   #注意复制导出的输入为图层lyr


def MakeDir(dir):   #新建文件夹函数
    if os.path.exists(dir) == False:
        os.mkdir(dir)


if __name__ == "__main__":

    time_start=time.time()
    city_ls = os.listdir(from_dir_big5)#城市选择导的顺序——按字母表顺序排序
    print(city_ls)

    num = 0
    for city in city_ls:
        
        city_c = city_ec_dict[city] #city英文城市名，city_c中文城市名
        
        #拼接输入（link和outline）、输出路径并返回值（元组）
        dirs = FileDirMaker(city,old_vno,new_vno,from_dir_big5,result_dir_big5,outline_dir)
        #备选路径——备选版本号1
        dirs_altermate1 = FileDirMaker(city,old_vno_altermate1,new_vno,from_dir_big5,result_dir_big5,outline_dir)
        #备选路径——备选版本号2
        dirs_altermate2 = FileDirMaker(city,old_vno_altermate2,new_vno,from_dir_big5,result_dir_big5,outline_dir)
        
        #新建成果中的城市文件夹
        output_city_file = os.path.join(result_dir_big5, city_c) 
        MakeDir(output_city_file)

        output_file = os.path.join(result_dir_big5, city_c, road_version) #新建成果中的【道路N次】文件夹
        MakeDir(output_file)
                
        #如果V1范围内shp不存在
        if os.path.exists(dirs[1][1]) == False:

            #try3种上版本版本号
            try:
                SelectOutput(dirs[1][0],dirs[0],(True,dirs[1][1]))  #V1 old_vno
            except:
                pass
            
            try:
                SelectOutput(dirs_altermate1[1][0],dirs_altermate1[0],(True,dirs_altermate1[1][1]))  #V1 old_vno_altermate1
            except:
                pass
            
            try:
                SelectOutput(dirs_altermate2[1][0],dirs_altermate2[0],(True,dirs_altermate2[1][1]))  #V1 old_vno_altermate2
            except:
                print("V1 in CompareExport can not be found!")
        else:
            print(dirs[1][1] + " exist！")
                
        #如果V2范围内shp不存在
        if os.path.exists(dirs[2][1]) == False:
            SelectOutput(dirs[2][0],dirs[0],(True,dirs[2][1]))  #V2
        else:
            print(dirs[2][1] + " exist！")

        num += 1
        print(city + " OK!")
    print(str(num) + " cities OK!")

    time_end=time.time()
    print(u'程序运行耗时：{:.2f}min'.format((time_end-time_start)/60)) 


