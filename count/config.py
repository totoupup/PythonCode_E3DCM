# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Description: 
# 
# 输入、输出数据根目录
# V1\V2版本号等
# 输入、输出文件路径拼接函数
# 城市字典、sql字典、表头、城市统计顺序列表等
# ---------------------------------------------------------------------------
import os

#小城市输入、输出及OUTLINE数据根目录
prj_dir = r"D:\PythonCode_E3DCM\01Data\prjFile"
from_dir = r"D:\PythonCode_E3DCM\01Data\03TodoCount\input_data\CompareExport\V1_V2"   #【修改1】图源软件比对导出的成果
result_dir = r"D:\PythonCode_E3DCM\01Data\03TodoCount\output\Result"
outline_dir = r"D:\PythonCode_E3DCM\01Data\03TodoCount\input_data\Tile"
fix_cityfile_dir = r"D:\PythonCode_E3DCM\01Data\03TodoCount\input_data\chinese_city_sequence.txt"
todo_count_dir = r"D:\PythonCode_E3DCM\01Data\03TodoCount\output\TodoCount.csv"
bus_count_dir = r"D:\PythonCode_E3DCM\01Data\03TodoCount\output\BusCount.csv"  #【修改2】分次统计前csv改名，防覆盖
road_version = u"道路1次"   #【修改3】导出的shp中道路N次

#大城市输入及OUTLINE数据根目录
from_dir_big5 = r"D:\PythonCode_E3DCM\01Data\03TodoCount\input_data\CompareExport\V1_V2_big5"#【修改1】图源软件比对导出的成果
result_dir_big5 = r"D:\PythonCode_E3DCM\01Data\03TodoCount\output\Result_big5"
outline_green_dir = r"D:\PythonCode_E3DCM\01Data\03TodoCount\input_data\Tile_Green"
region_ls = [u"绿区",u"蓝区"]
todo_count_dir_big5 = r"D:\PythonCode_E3DCM\01Data\03TodoCount\output\TodoCount_big5.csv"
bus_count_dir_big5 = r"D:\PythonCode_E3DCM\01Data\03TodoCount\output\BusCount_big5.csv" 

#version_no【修改3】
old_vno = "20Q4M2G2"    #正式
old_vno_altermate1 = "20Q4M2G2" #候补1 ——当上版本号存在多种时备选
old_vno_altermate2 = "20Q4M2G2" #候补2 
new_vno = "21Q1G1"

def FileDirMaker(city_e,old_vno,new_vno,from_dir,result_dir,outline_dir): #英文城市名、版本号，文件夹结构固定
    #from_dir是指比对导出LINK的根目录
    #result_dir是指导出道路N次成果的根目录

    city_c = city_ec_dict[city_e] #city英文城市名，city_c中文城市名
    
    #输入LINK文件名
    input_link_V1_name = city_e + "_" + old_vno + "_Link.shp" 
    input_link_V2_name = input_link_V1_name.replace(old_vno, new_vno)

    #OUTLINE文件名及路径
    outline_name = city_e + "_20Q3_Submit_outline_M.shp"  #【修改3】确认outline名称匹配
    outline_dir = os.path.join(outline_dir, city_e,outline_name)
    
    #输出LINK文件名
    output_link_V1_name = old_vno + city_c + u"道路范围内.shp" 
    output_link_V2_name = output_link_V1_name.replace(old_vno, new_vno)
    
    #V1输入、输出路径
    input_link_V1_dir = os.path.join(from_dir,city_e,input_link_V1_name)    
    output_link_V1_dir = os.path.join(result_dir,city_c,road_version,output_link_V1_name)#输出road_version道路N次
    
    #V2输入、输出路径
    input_link_V2_dir = os.path.join(from_dir,city_e,input_link_V2_name)
    output_link_V2_dir = os.path.join(result_dir,city_c,road_version,output_link_V2_name)#road_version道路N次

    #LINK_COMPARE
    link_compare_dir = os.path.join(from_dir,city_e,"LINK_COMPARE.shp")

    #返回元组（选择框路径，（V1输入、输出路径），（V2输入、输出路径），link_compare输入路径）
    dirs = (outline_dir,\
    (input_link_V1_dir,output_link_V1_dir),\
    (input_link_V2_dir,output_link_V2_dir),\
    link_compare_dir) 

    return dirs




#列名columns与预处理统计表的列名顺序一致
#todo量（含10级路）,新增道路（含10级路）,删除道路,形状几何、挂接变化,道路方向变化,车道数变化,车信变化,属性及其他
columns = ['TODO', 'Add', 'Del', 'Form', 'Direct', 'LaneNum', 'LaneConnexity', 'Status']

#使用《预处理统计表》中除珠澳外62城市顺序 
fix_city_e_ls = ['BEIJING', 'SHANGHAI', 'GUANGZHOU', 'SHENZHEN', 'SHENYANG', 'NANJING', 'HANGZHOU', 
'TIANJIN', 'CHENGDU', 'XIAN', 'SUZHOU', 'ZHENGZHOU', 'WUHAN', 'DALIAN', 'WUXI', 'NINGBO', 
'XIANGGANG', 'CHANGCHUN', 'CHANGSHA', 'WENZHOU', 'JINAN', 'TAIYUAN', 'HEFEI', 'DONGGUAN', 'XIAMEN',
 'HAERBIN', 'KUNMING', 'CHONGQING', 'QINGDAO', 'TANGSHAN', 'FOSHAN', 'FUZHOU', 'AOMEN', 'NANNING',
  'HUHEHAOTE', 'LANZHOU', 'YANGZHOU', 'SHIJIAZHUANG', 'QUANZHOU', 'YANTAI', 'NANCHANG', 'WULUMUQI', 
  'GUIYANG', 'BAODING', 'HAIKOU', 'SHAOXING', 'TAIZHOU', 'SANYA', 'LIUZHOU', 'QINHUANGDAO', 'XINING',
   'ZHUHAI', 'WEIFANG', 'XUZHOU', 'YANCHENG', 'NANTONG', 'JINHUA', 'CHANGZHOU', 'HUIZHOU', 'ZHONGSHAN', 
   'YINCHUAN', 'WUHU'] 

#使用“提交范围TILE”选取对应导出link的shp文件，提取【统计表】统计变化数量时使用如下SQL语句：
sql_dict = {   
    'TODO':"\"Status\" <>''OR \"ToDo\" <>'' ",
    'Add':"\"Status\" like'%增%'OR \"Status\" like'%受影响的%'OR \"ToDo\" like'%新增%'",
    'Del':"\"Status\" like'%删%'  OR \"Status\" like'%受影响%'",
    'Form':"\"Status\" like '%几何修改%'",
    'Direct':"\"ToDo\" like'%方向变化%'",
    'LaneNum':"\"ToDo\" like'%车道数变化%'",
    'LaneConnexity':"\"ToDo\" like'%LaneConnexity%'",
    'Status':"\"Status\" like '%属性%'"   
    }
sql_dict2 = dict(zip(sql_dict.items(),sql_dict.keys()))
# 在有上下游关系的模块中，输入输出是相对的，所以使用绝对名称来定义输入输出的变量名

#62个城市
city_ce_dict={#配合arcpy包使用python2.7，注意语法
u'三亚':'SANYA',
u'东莞':'DONGGUAN',
u'中山':'ZHONGSHAN',
u'乌鲁木齐':'WULUMUQI',
u'佛山':'FOSHAN',
u'保定':'BAODING',
u'兰州':'LANZHOU',
u'南京':'NANJING',
u'南宁':'NANNING',
u'南昌':'NANCHANG',
u'南通':'NANTONG',
u'厦门':'XIAMEN',
u'台州':'TAIZHOU',
u'合肥':'HEFEI',
u'呼和浩特':'HUHEHAOTE',
u'哈尔滨':'HAERBIN',
u'唐山':'TANGSHAN',
u'大连':'DALIAN',
u'天津':'TIANJIN',
u'太原':'TAIYUAN',
u'宁波':'NINGBO',
u'常州':'CHANGZHOU',
u'徐州':'XUZHOU',
u'惠州':'HUIZHOU',
u'成都':'CHENGDU',
u'扬州':'YANGZHOU',
u'无锡':'WUXI',
u'昆明':'KUNMING',
u'杭州':'HANGZHOU',
u'柳州':'LIUZHOU',
u'武汉':'WUHAN',
u'泉州':'QUANZHOU',
u'济南':'JINAN',
u'海口':'HAIKOU',
u'温州':'WENZHOU',
u'潍坊':'WEIFANG',
u'烟台':'YANTAI',
u'珠海':'ZHUHAI',
u'盐城':'YANCHENG',
u'石家庄':'SHIJIAZHUANG',
u'福州':'FUZHOU',
u'秦皇岛':'QINHUANGDAO',
u'绍兴':'SHAOXING',
u'芜湖':'WUHU',
u'苏州':'SUZHOU',
u'西宁':'XINING',
u'西安':'XIAN',
u'贵阳':'GUIYANG',
u'郑州':'ZHENGZHOU',
u'重庆':'CHONGQING',
u'金华':'JINHUA',
u'银川':'YINCHUAN',
u'长春':'CHANGCHUN',
u'长沙':'CHANGSHA',
u'青岛':'QINGDAO',
u'沈阳':'SHENYANG',
u'广州':'GUANGZHOU',
u'上海':'SHANGHAI',
u'深圳':'SHENZHEN',
u'北京':'BEIJING',
u'香港':'XIANGGANG',
u'澳门':'AOMEN'
}

# english-chinese
city_ec_dict = dict(zip(city_ce_dict.values(), city_ce_dict.keys()))

#if __name__ == '__main__':
#  print('chinese-english')
#  for key, value in city_ce_dict.items():
#    print (key, value)
#
#  print('english-chinese')
#  for key, value in city_ec_dict.items():
#    print (key, value)

# def GetCitySequence(fix_cityfile_dir):

