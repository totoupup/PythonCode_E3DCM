#coding=utf-8
#——————————————————————————————————————————————————————————————————————
#
#           统计POI的全部、新增、删除、不变4种数据量，生成csv文件
#
#——————————————————————————————————————————————————————————————————————

import arcpy
import os

#city_e_seq_ls：与《预处理变化量统计表》顺序匹配的英文城市名列表 63-香港-澳门-珠澳/珠海
#统计差分量——由于字典不是序列类型，统计顺序随机，这里使用列表
city_e_seq_ls =['BEIJING', 'SHANGHAI', 'GUANGZHOU', 'SHENZHEN', 'SHENYANG', 'NANJING',\
                'HANGZHOU', 'TIANJIN', 'CHENGDU', 'XIAN', 'SUZHOU', 'ZHENGZHOU', 'WUHAN',\
                'DALIAN', 'WUXI', 'NINGBO', 'HK', 'CHANGCHUN', 'CHANGSHA', 'WENZHOU',\
                'JINAN', 'TAIYUAN', 'HEFEI', 'DONGGUAN', 'XIAMEN', 'HAERBIN', 'KUNMING',\
                'CHONGQING', 'QINGDAO', 'TANGSHAN', 'FOSHAN', 'FUZHOU', 'MC', 'MCZH', 'NANNING',\
                'HUHEHAOTE', 'LANZHOU', 'YANGZHOU', 'SHIJIAZHUANG', 'QUANZHOU', 'YANTAI',\
                'NANCHANG', 'WULUMUQI', 'GUIYANG', 'BAODING', 'HAIKOU', 'SHAOXING', 'TAIZHOU',\
                'SANYA', 'LIUZHOU', 'QINHUANGDAO', 'XINING', 'ZHUHAI', 'WEIFANG', 'XUZHOU',\
                'YANCHENG', 'NANTONG', 'JINHUA','CHANGZHOU', 'HUIZHOU', 'ZHONGSHAN', 'YINCHUAN', 'WUHU']

f = open(r'D:\PythonCode_E3DCM\01Data\04BackPoiProcess\02POI\POI_4\count_POI.csv','w+')#【修改1】统计成果csv生成路径
title = ['CITY','POI','POI_ADD','POI_DEL','POI_INVARI']#需与dirs列表元素顺序一致
f.write(','.join(title)+'\n') 

ls = []#存放63个元素（城市名及对应的4种统计值的列表）的列表

#拼出POI——4种需要统计的数据路径
root = r'D:\PythonCode_E3DCM\01Data\04BackPoiProcess\02POI\POI_4'#【修改2】POI_4种数据所在根目录,含中文加u# 
paths = os.listdir(root)
print paths
dirs = []#POI4种路径的列表
for path in paths:
    if '.csv' not in path:
        dirs.append(os.path.join(root,path))
print dirs #打印出统计顺序并检查与title是否一致

for city_e in city_e_seq_ls:
    print city_e+' is counting...'
    ls_4 = []
    for i in dirs:
        #arcpy.GetCount_management()获取shp属性表行数   
        shpfile_POI =i+ '/' + city_e + '_OUTLINE_IX_POI.shp'
        try:
            result_POI = arcpy.GetCount_management(shpfile_POI)
            count_POI = str(int(result_POI.getOutput(0)))
        except:
            count_POI ='null'
            
        #把每个城市的4种统计数据存入列表ls_4
        ls_4.append(count_POI)
    #每个城市的【英文名与4种统计数据ls_4】作为元素，存入ls
    ls.append([city_e]+ls_4)
    #ls_4.clear()
print ls    

#写入csv
num = 0
for row in ls:    
    #print(row)   row=['CITY','POI','POI_ADD','POI_DEL','POI_INVARI']
    #str.join(seq),seq期望是序列类型数据：字符串或列表
    f.write(','.join(row)+'\n')    #TypeError: sequence item 0: expected string, list found    
    print '{} recorded！'.format(row[0])
    num += 1

f.close()        
print '{} cities successed！'.format(num)





