# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# TodoCount_big5.py  输入数据大城市绿区\蓝区的V1\V2的范围内link
# Description: 统计V1\V2的link量，及8种sql统计量，并导出新增变化和删除量
# ---------------------------------------------------------------------------

import os,time,arcpy
arcpy.env.overwriteOutput = True  #启用覆盖地理处理操作的输出
import csv
from TodoCount import CountShapefile,SqlCountOutput
from city_dict import city_ce_dict,city_ec_dict  #中英对照字典
from config import result_dir_big5,region_ls,todo_count_dir_big5
from config import columns,old_vno,old_vno_altermate1,old_vno_altermate2,new_vno,road_version
from config import sql_dict,sql_dict2,FileDirMaker,fix_city_e_ls,todo_count_dir #常量

def CreateRegionInputshp(from_dir,road_version,old_vno,city_c,region):
  input_shp_region = os.path.join(result_dir_big5,city_c,road_version,region,\
                   old_vno+city_c+region+u"道路范围内.shp")
  return input_shp_region

def IsExistsDir(dir1,dir2,dir3):#判断各dir中真实存在的唯一dir
  dir_exist = ""
  for i in [dir1,dir2,dir3]:
    if os.path.exists(i):
      dir_exist = i
      break
  else:
    print "None dir exists!"
  return dir_exist

if __name__ == "__main__": 
  time_start=time.time()

  ls_count = []

  title = ["CITY","V1_COUNT_GREEN","V1_COUNT_BLUE","V2_COUNT_GREEN","V2_COUNT_BLUE"]\
       + columns + columns[:2]+columns[3:]#删去Del
  print(title)
  for city_e in fix_city_e_ls[:5]:#列表中前5个城市-北上广深沈
        
    ls_count_line = [city_e]
    ls_region_title_ori = [] #[V1_green,V2_green,V1_blue,V2_blue]
    ls_count_region_merge_ori = [] #绿区8+蓝区7种统计量

    city_c = city_ec_dict[city_e]

    for region in region_ls:   
      
      ## 输入数据——V1可能存在多种版本号的可能
      #V1
      dir1 = input_shp_V1 = CreateRegionInputshp(result_dir_big5,road_version,old_vno,city_c,region)
      print dir1
      dir2 = input_shp_V1_altermate1 = CreateRegionInputshp(result_dir_big5,road_version,old_vno_altermate1,city_c,region)
      dir3 = input_shp_V1_altermate2 = CreateRegionInputshp(result_dir_big5,road_version,old_vno_altermate2,city_c,region)
      input_shp_V1_exist = IsExistsDir(dir1,dir2,dir3)
      #V2
      input_shp_V2 = CreateRegionInputshp(result_dir_big5,road_version,new_vno,city_c,region)

      ## 输出数据
      #V1
      output_shp_V1 = input_shp_V2.replace(u"范围内", u"删除量")
      # print(output_shp_V1_green)
      #V2
      output_shp_V2 = input_shp_V2.replace(u"范围内", u"新增变化量")

      #V1\V2全量
      count_shp_V1_region = CountShapefile(input_shp_V1_exist)
      count_shp_V2_region = CountShapefile(input_shp_V2)
      ls_V1V2_region = [count_shp_V1_region,count_shp_V2_region]
      ls_region_title_ori += ls_V1V2_region#拼接列表

      ls_count_region = []
      for i in columns:
        sql = sql_dict[i]
        
        if i == 'Del':
          count = SqlCountOutput(input_shp_V1_exist,sql,output_shp_V1)
        else:
          count = SqlCountOutput(input_shp_V2,sql,output_shp_V2)
        
        ls_count_region.append(count)

      ls_count_region_merge_ori += ls_count_region  
      print "ls_count_region_merge_ori:{}".format(ls_count_region_merge_ori)
   
    ##组合成写入行
    #ls_region_title_ori=[V1_green,V2_green,V1_blue,V2_blue]
    ls_region_title = [ls_region_title_ori[0],ls_region_title_ori[2],ls_region_title_ori[1],ls_region_title_ori[3]]
    #print ls_region_title
    ls_count_region_merge = ls_count_region_merge_ori[:10]+ls_count_region_merge_ori[11:]#[前不包：后包]
    #print ls_count_region_merge
    ls_count_line += (ls_region_title + ls_count_region_merge)
    print ls_count_line
    ls_count.append(ls_count_line)
    print ls_count
  
  with open(todo_count_dir_big5,'w') as f:
      num = 0
      f.write(','.join(title)+'\n')
      for row in ls_count:    
        f.write(','.join(row)+'\n')    #TypeError: sequence item 0: expected string, list found    
        print '{} recorded!'.format(row[0])
        num += 1          
  print('{} cities successed!'.format(num))
  time_end=time.time()
  print(u'程序运行耗时：{:.2f}min'.format((time_end-time_start)/60))  

# print(ls_count)

