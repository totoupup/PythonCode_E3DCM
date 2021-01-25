# coding=utf-8
#——————————————————————————————————————————————————————————————————————
#
#                       统计绿地、水系差分量，写入csv文件
#
#——————————————————————————————————————————————————————————————————————
import os,arcpy
from City_Dictionary_u import city_dict2#全部城市60个，不包括香港、澳门 City_Dictionary

f = open(r'D:\20Q4M2\DATA\20Q4M2G2\prj_BACK\count.csv','w+')#统计结果csv文件的生成路径
title = ['CITY','GREENURBAN_SymDiff','WATER_SymDiff']#统计结果csv文件的表头
back_symdiff_dir = r'D:\20Q4M2\DATA\20Q4M2G2\prj_BACK\back_symdiff'
version_no = '20Q4M2'#统计的绿地、水系差分量的前缀版本号

f.write(','.join(title)+'\n')

city_e_seq_ls =['BEIJING', 'SHANGHAI', 'GUANGZHOU', 'SHENZHEN', 'SHENYANG', 'NANJING',\
                'HANGZHOU', 'TIANJIN', 'CHENGDU', 'XIAN', 'SUZHOU', 'ZHENGZHOU', 'WUHAN',\
                'DALIAN', 'WUXI', 'NINGBO', 'HK', 'CHANGCHUN', 'CHANGSHA', 'WENZHOU',\
                'JINAN', 'TAIYUAN', 'HEFEI', 'DONGGUAN', 'XIAMEN', 'HAERBIN', 'KUNMING',\
                'CHONGQING', 'QINGDAO', 'TANGSHAN', 'FOSHAN', 'FUZHOU', 'MC', 'MCZH', 'NANNING',\
                'HUHEHAOTE', 'LANZHOU', 'YANGZHOU', 'SHIJIAZHUANG', 'QUANZHOU', 'YANTAI',\
                'NANCHANG', 'WULUMUQI', 'GUIYANG', 'BAODING', 'HAIKOU', 'SHAOXING', 'TAIZHOU',\
                'SANYA', 'LIUZHOU', 'QINHUANGDAO', 'XINING', 'ZHUHAI', 'WEIFANG', 'XUZHOU',\
                'YANCHENG', 'NANTONG', 'JINHUA','CHANGZHOU', 'HUIZHOU', 'ZHONGSHAN', 'YINCHUAN', 'WUHU']


#统计差分量——由于字典不是序列类型，统计顺序随机
num = 0
ls = []
#for city_k,city_v in city_names.items():         #key:city
for city in city_e_seq_ls:    
    #arcpy.GetCount_management()计算差分量
    print city+u' is counting...'
    
    shpfile_GREENURBAN = os.path.join(back_symdiff_dir,version_no)+city_dict2.get(city,"null")+u'绿地差分量.shp'
    try:
        result_GREENURBAN = arcpy.GetCount_management(shpfile_GREENURBAN)
        count_GREENURBAN = str(int(result_GREENURBAN.getOutput(0)))
    except:
        count_GREENURBAN = "null"


    shpfile_WATER = os.path.join(back_symdiff_dir,version_no)+city_dict2.get(city,"null")+u'水系差分量.shp'
    try:
        result_WATER = arcpy.GetCount_management(shpfile_WATER)
        count_WATER = str(int(result_WATER.getOutput(0)))
    except:
        count_WATER = "null"

    #差分量计入ls，ls的60个元素是：[城市名，绿地差分量，水系差分量]——3元素列表    
    ls.append([city,count_GREENURBAN,count_WATER])

    
    #写入csv
for row in ls:       
    f.write(','.join(row)+'\n')  #2      
    print '{} recorded！'.format(row[0])
    num += 1

f.close()        
print '{} cities successed！'.format(num)

#1
##ls = ls.append()错误:
    ##append会修改ls本身，并且返回None。不能把返回值再赋值给ls。
    
    ##count_GREENURBAN需要转成字符串——str(),否则会报错：
    ##f.write(','.join(row)+'\n')    #TypeError: sequence item 0: expected string, list found
    ##TypeError: sequence item 1: expected string or Unicode, int found


#2
#print(row)   row=[city,city,city]
#str.join(seq),seq期望是序列类型数据：字符串或列表
#TypeError: sequence item 0: expected string, list found


