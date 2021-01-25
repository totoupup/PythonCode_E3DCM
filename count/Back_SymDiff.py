#coding = utf-8
#——————————————————————————————————————————————————————————————————————
#
#                       对两版本平面坐标的绿地、水系.shp
#                            做交集取反（差分）
#                         生成绿地、水系差分量.shp成果
#       
#——————————————————————————————————————————————————————————————————————

import arcpy
import os,time
from City_Dictionary_u import city_names,city_dict2#中英，英中
time_start = time.time()

#Workspace
inWorkspace = r'D:\PythonCode_E3DCM\01Data\04BackPoiProcess\01BACK\prjBack_V1'#上版本平面背景（绿地&水系）数据
updateWorkspace = r'D:\PythonCode_E3DCM\01Data\04BackPoiProcess\01BACK\prjBack_V2'#本版本平面背景（绿地&水系）数据
outWorkspace = r'D:\PythonCode_E3DCM\01Data\04BackPoiProcess\01BACK\prjBack_Symdiff'#差分成果
version_no = '20Q4M2'#【<————修改为本版版本号！】

#City List
file_names_ls = os.listdir(updateWorkspace)
#print(file_names_ls)
city_ls = []
for file in file_names_ls:
    city = file.split('_')[0]
    if city not in city_ls:
        city_ls.append(city)
print(city_ls)

dict = {u'绿地':'_GREENURBAN.shp',u'水系':'_WATER.shp'}

num_ok = 0
num_fail = 0
for city in city_ls:
    cnt = 0 #计数器
    for key in dict:
        inFeatures = inWorkspace + '//' + city+ dict[key]
        print inFeatures

        updateFileName = city + ""+dict[key]#"_OUTLINE"
        updateFeatures = updateWorkspace + '//' + updateFileName
        print updateFeatures

        outFeatureClass = os.path.join(outWorkspace,version_no) + city_dict2[city] + key +  u'差分量.shp'#【修改版本号使输出成果命名正确】
        print outFeatureClass
        clusterTolerance = ".0001 Meters"    
        # Execute SymDiff
        try:
            #注意！差分前后数据坐标必须一致！！！
            arcpy.SymDiff_analysis(inFeatures, updateFeatures, outFeatureClass, "ALL", clusterTolerance)
            print(city + key + u'差分成功！')
            cnt += 1
        except:
            print(city + key + u'差分失败！请确认！')
            num_fail += 1
    if cnt==2:
        num_ok += 1
print(u'差分完成!共{0}城市成功，{1}差分失败项，请确认！'.format(num_ok,num_fail))

time_end=time.time()
last = round((time_end-time_start)/60,2)
print u'绿地水系差分处理耗时：{}min'.format(last)
