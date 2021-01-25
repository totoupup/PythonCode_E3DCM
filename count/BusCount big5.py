# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Description: 统计范围内公交车Todo量
# ---------------------------------------------------------------------------
import os,time,arcpy 
from BusCount import BusCount
from TodoCount_big5 import CreateRegionInputshp,IsExistsDir
from config import from_dir_big5,region_ls,bus_count_dir_big5
from city_dict import city_ce_dict,city_ec_dict  #中英对照字典
from config import old_vno,new_vno,road_version,result_dir,FileDirMaker,fix_city_e_ls #常量
arcpy.env.overwriteOutput = True  #启用覆盖地理处理操作的输出

time_start = time.time()

city_e_ls = [i.decode(encoding='gbk') for i in os.listdir(from_dir_big5)]
print(u"from_dir列表城市数：{}".format(len(city_e_ls)))
print(city_e_ls)



num_ok = 0
num_null = 0
if __name__ == "__main__":

    title_bus_count = ["CITY","GREEN","BLUE",]
    ls_bus_count = []
    for city_e in fix_city_e_ls[:5]:    #使用《预处理统计表》中除-珠澳-外62城市顺序
        
        city_c = city_ec_dict[city_e]
        #link_compare路径
        input_link_compare = FileDirMaker(city_e,old_vno,new_vno,from_dir_big5,"","")[3]
        print(input_link_compare)
        
        bus_count_region = []
        for region in region_ls:

            ## 输入数据V2
            input_shp_V2 = CreateRegionInputshp(from_dir_big5,road_version,new_vno,city_c,region)
            print(input_shp_V2)

            try:
                count = BusCount(city_e,input_shp_V2,input_link_compare)
                num_ok += 1
            except:
                count = "null"
                num_null += 1
            
            bus_count_region.append(count)#绿区、蓝区
        
        ls_bus_count.append([city_e]+bus_count_region)
    print(ls_bus_count)
    print(u"统计OK数：{0}，统计null数：{1}".format(num_ok,num_null))

    with open(bus_count_dir_big5,"w") as f: #【分两部分统计时，二次运行前修改csv文件名】
        f.write(','.join(title_bus_count)+'\n')

        num = 0
        for row in ls_bus_count:
            f.write(','.join(row)+'\n')
            print '{} recorded!'.format(row[0])
            num += 1          
    print('{} cities successed!'.format(num))
    
    
time_end = time.time()
print(u'程序运行耗时：{:.2f}min'.format((time_end-time_start)/60))


