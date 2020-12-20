# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Description: 统计范围内公交车Todo量
# ---------------------------------------------------------------------------
import os,time,arcpy
from city_dict import city_ce_dict,city_ec_dict  #中英对照字典
from config import old_vno,new_vno,from_dir,result_dir,outline_dir,FileDirMaker,fix_city_e_ls,bus_count_dir #常量
arcpy.env.overwriteOutput = True  #启用覆盖地理处理操作的输出

time_start = time.time()

city_e_ls = os.listdir(from_dir)
print(u"from_dir列表城市数：{}".format(len(city_e_ls)))
print(city_e_ls)


def BusCount(city_e,input_link,input_link_compare):

    #添加属性索引        
    arcpy.AddIndex_management(input_link, "LINK_PID", "", "NON_UNIQUE", "NON_ASCENDING")

    # Process: 添加连接
    input_link_lyr = arcpy.MakeFeatureLayer_management(input_link, input_link.replace(".shp",".lyr"))
    input_link_compare_lyr = arcpy.MakeFeatureLayer_management(input_link_compare, input_link_compare.replace(".shp",".lyr"))
    arcpy.AddJoin_management(input_link_lyr, "LINK_PID", input_link_compare_lyr, "LINKID", "KEEP_ALL")

    # Process: 按属性选择图层
    arcpy.SelectLayerByAttribute_management(input_link_lyr, "NEW_SELECTION", "\"LINK_COMPARE.TODO\" <> ' ' ")

    # Process: 获取计数
    count = str(arcpy.GetCount_management(input_link_lyr))  #str改成int后count全部为null，why？

    return count

num_ok = 0
num_null = 0
if __name__ == "__main__":

    ls_bus_count = []
    for city_e in fix_city_e_ls:    #使用《预处理统计表》中除-珠澳-外62城市顺序


        #范围内link
        input_link = FileDirMaker(city_e,old_vno,new_vno,from_dir,result_dir,outline_dir)[2][1]
        #print(input_link)
        
        #link_compare路径
        input_link_compare = FileDirMaker(city_e,old_vno,new_vno,from_dir,result_dir,outline_dir)[3]
        #print(input_link_compare)

        try:
            count = BusCount(city_e,input_link,input_link_compare)
            num_ok += 1
        except:
            count = "null"
            num_null += 1

        ls_bus_count.append([city_e,count])
        print(city_e,count)
    print(u"统计OK数：{0}，统计null数：{1}".format(num_ok,num_null))

    with open(bus_count_dir,"w") as f: #【分两部分统计时，二次运行前修改csv文件名】
        num = 0
        for row in ls_bus_count:
            f.write(','.join(row)+'\n')
            print '{} recorded!'.format(row[0])
            num += 1          
    print('{} cities successed!'.format(num))
    
    
time_end = time.time()
print(u'程序运行耗时：{:.2f}min'.format((time_end-time_start)/60))

# 检查输入文件夹结构正确
# 运行前修改config的from_dir，old_vno
# 分两部分统计时，二次运行前修改csv文件名，确保不覆盖写
