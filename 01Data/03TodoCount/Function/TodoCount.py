# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# TodoCount.py  输入数据为V1\V2的范围内link
# Description: 统计V1\V2的link量，及8种sql统计量，并导出新增变化和删除量
# ---------------------------------------------------------------------------

import os,time,arcpy
arcpy.env.overwriteOutput = True  #启用覆盖地理处理操作的输出
import csv
from city_dict import city_ce_dict,city_ec_dict  #中英对照字典
from config import from_dir,result_dir,columns,old_vno,old_vno_altermate1,old_vno_altermate2,new_vno
from config import sql_dict,sql_dict2,FileDirMaker,fix_city_e_ls,todo_count_dir #常量


def CountShapefile(input_shp):#输入一个shp，返回它的属性表行数
    input_lyr = input_shp.replace(".shp",".lyr")
    try:
        arcpy.MakeFeatureLayer_management(input_shp,input_lyr)
        count = str(arcpy.GetCount_management(input_lyr))
    except:
      count = "null"

    # #删除图层、防止后续冲突(占用状态无法删除)
    # arcpy.DeleteFeatures_management(input_lyr)
    return count 


def SqlCountOutput(input_shp,sql,output_shp):

    input_lyr = input_shp.replace(".shp",".lyr")
    try:
      #按属性选择 
      arcpy.MakeFeatureLayer_management(input_shp,input_lyr)
      result = arcpy.SelectLayerByAttribute_management(input_lyr, "NEW_SELECTION", sql)
      
      #记录选中数量
      count = str(arcpy.GetCount_management(input_lyr))
      # count = result.outputCount
      # print("{}:{}".format(sql_dict2[sql],str(count)))

      #按条件导出shp
      sql_TODO = "\"Status\" <>''OR \"ToDo\" <>'' " #新增变化量
      sql_DEL = "\"Status\" like'%删%'  OR \"Status\" like'%受影响%'" #删除量
      if sql == sql_TODO or sql == sql_DEL:
        arcpy.CopyFeatures_management(input_lyr,output_shp)
        # result.saveToFile(output_shp)
    except:
      count = "null"
    return count


if __name__ == "__main__": 
  time_start=time.time()
        
  # print(columns)
  ls_count = []

  title = ["CITY","V1_COUNT","V1_COUNT"]+columns
  print(title)
  for city_e in fix_city_e_ls:
        
    ls_count_line = [city_e]
    
    input_shp_V1 = FileDirMaker(city_e, old_vno, new_vno, '', result_dir, '')[1][1]
    # print(input_shp_V1)
    input_shp_V2 = FileDirMaker(city_e, old_vno, new_vno, '', result_dir, '')[2][1]
    # print(input_shp_V2)
    output_shp_V1 = input_shp_V2.replace(u"范围内", u"删除量")
    # print(output_shp_V1)
    output_shp_V2 = input_shp_V2.replace(u"范围内", u"新增变化量")
    # print(output_shp_V2)
    
    #统计V1\V2的link量
    #统计V1
    if os.path.isfile(input_shp_V1) == True:
      count_shp_V1 = CountShapefile(input_shp_V1) 

    elif os.path.isfile(input_shp_V1.replace(old_vno,old_vno_altermate1)) == True: #升级包V1版本号不统一时，尝试备选版本号1
      count_shp_V1 = CountShapefile(input_shp_V1.replace(old_vno,old_vno_altermate1))

    elif os.path.isfile(input_shp_V1.replace(old_vno,old_vno_altermate2)) == True: #升级包V1版本号不统一时，尝试备选版本号2
      count_shp_V1 = CountShapefile(input_shp_V1.replace(old_vno,old_vno_altermate2))
    
    else:
      count_shp_V1 = "null"  
    #统计V2
    count_shp_V2 = CountShapefile(input_shp_V2)

    ls_count_line += [count_shp_V1,count_shp_V2]
    # print(ls_count_line)

    for i in columns:
      sql = sql_dict[i]
      # print(i)

      if i == 'Del':
            
        if os.path.isfile(input_shp_V1) == True:
          count = SqlCountOutput(input_shp_V1,sql,output_shp_V1)
          # print(old_vno)
        elif os.path.isfile(input_shp_V1.replace(old_vno,old_vno_altermate1)) == True:
          #升级包V1版本号不统一时，尝试备选版本号1
          count = SqlCountOutput(input_shp_V1.replace(old_vno,old_vno_altermate1),sql,output_shp_V1)
          # print(old_vno_altermate1)
        elif os.path.isfile(input_shp_V1.replace(old_vno,old_vno_altermate2)) == True:
          #升级包V1版本号不统一时，尝试备选版本号2
          count = SqlCountOutput(input_shp_V1.replace(old_vno,old_vno_altermate2),sql,output_shp_V1)
          # print(old_vno_altermate2)
        
        else:
          count = "null"

      else:
        count = SqlCountOutput(input_shp_V2,sql,output_shp_V2)

      ls_count_line.append(count)
      #写入csv    
    ls_count.append(ls_count_line)
    # print(city_e)
    print(ls_count_line)

  with open(todo_count_dir,'w') as f:
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

