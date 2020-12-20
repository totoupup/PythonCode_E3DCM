#-*- coding: utf-8 -*-
import os,time
import shutil
time_start=time.time()

#批量处理的60个城市——城市不全亦可使用

#将打断包拷贝到对应作业组下
copyFromRoot = r"D:\PythonCode_E3DCM\01Data\08CreateBagEX2\ROAD_EX2_DATA\copyto\ROAD_EX2\\" 
copyToRoot = r"D:\PythonCode_E3DCM\01Data\08CreateBagEX2\ROAD_EX2_GROUP\\"     

#city_names=os.listdir(r"")
ls_TY=['ZHONGSHAN', 'FOSHAN', 'BEIJING', 'NANJING', 'DALIAN', 'XUZHOU',
       'CHENGDU', 'WUXI', 'WUHAN', 'SHENYANG', 'QUANZHOU', 'SHENZHEN', 
       'ZHUHAI', 'YANCHENG', 'SHIJIAZHUANG', 'FUZHOU', 'QINHUANGDAO', 
       'WUHU', 'XINING', 'CHONGQING', 'YINCHUAN', 'CHANGCHUN']
ls_HZ=['LANZHOU', 'NANTONG', 'HUHEHAOTE', 'HUIZHOU', 'YANGZHOU', 
       'SUZHOU', 'XIAN', 'JINHUA', 'JINAN', 'SHAOXING']
ls_TJ=['SANYA', 'SHANGHAI', 'WULUMUQI', 'BAODING', 'NANCHANG', 
       'XIAMEN', 'TAIZHOU', 'HEFEI', 'HAERBIN', 'TANGSHAN', 'TIANJIN',
       'TAIYUAN', 'WENZHOU', 'YANTAI', 'GUIYANG', 'ZHENGZHOU', 'QINGDAO']
ls_CS=['DONGGUAN', 'NANNING', 'NINGBO', 'CHANGZHOU', 'GUANGZHOU', 
       'KUNMING', 'HANGZHOU', 'LIUZHOU', 'WEIFANG', 'CHANGSHA']
ls_YS=['HAIKOU']

groupDict = {'图源组':ls_TY,'杭州组':ls_HZ,'天津组':ls_TJ,'长沙组':ls_CS,'验收组':ls_YS}
#num城市数，groupCityLs作业组城市列表，Root根目录,groupName作业组名称
def CopyBag(groupCityLs,copyFromRoot,copyToRoot,groupName):
    num = 0
    for city in groupCityLs:#作业组城市列表  
        #注意分组的文件是文件夹还是文件，注意修改
        copyFromDir = os.path.join(copyFromRoot, city.lower()  + '.rar')
        #print(copyFromDir)
        copyToDir = os.path.join(copyToRoot, groupName, city.lower() + '.rar')
        #print(copyToDir)
        try:
            #文件夹copytree，文件copyfile
            shutil.copyfile(copyFromDir,copyToDir)
            num += 1
        except:
            pass
    print(groupName + str(num) + '城市打断包拷贝完成！')
    return num


num_ALL = 0
for groupName in groupDict:
    print(groupName)
    os.mkdir(copyToRoot + groupName)
    #注意接收函数返回之时，函数执行一次

    num = CopyBag(groupDict[groupName],copyFromRoot,copyToRoot,groupName)
    num_ALL += num

print(str(num_ALL)+'城市打断包已拷贝完成！')

time_end=time.time()
print (u'分组耗时：{:.2f}min'.format((time_end-time_start)/60))
