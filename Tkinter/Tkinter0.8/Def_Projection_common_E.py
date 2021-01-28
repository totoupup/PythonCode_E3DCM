# coding=utf-8

# ---------------------------------------------------------------------------
# 为文件夹内所有经纬度shp生成对应的平面投影
# ---------------------------------------------------------------------------
import arcpy
import os,re
import time
#os、arcpy文件覆盖写
arcpy.env.overwriteOutput = True  #启用覆盖地理处理操作的输出

inWorkspace = u'D:/00通用工具/00FME/背景POI提取FME_20Q3G1/背景POI提取_上海outline扩面积更新/20Q3_BACK&POI_catch/result_BACK3'#根目录
prjdir = r'D:/PythonCode_inWork/prjFile'#投影文件所在路径


##判断是否为shp文件
def isShapefile(file_name):
    if ".shp" in file_name and ".xml" not in file_name:
        flag = True
    else:
        flag = False
    return flag

##建立对应投影成果文件夹——绝对路径中【叶子节点】文件夹前加"add_str"
def createPrjFile(file_dir,add_str):
    dir_name,base_name = os.path.split(file_dir)#如果路径末有//，则输出路径和为空文件名
    #print dir_name
    #print base_name
    prj_file_dir = os.path.join(dir_name,add_str + base_name)
    if os.path.exists(prj_file_dir) == False:
        os.mkdir(prj_file_dir)
    print prj_file_dir + u" 文件夹新建成功！"
    return prj_file_dir

#返回一个文件在投影文件列表中匹配的投影文件
def prjMatch(shp_dir,prjdir):#shp_dir最好为绝对路径，1文件夹或2文件名匹配投影文件均可行
    prjfile_ls = os.listdir(prjdir)
    for prjfile in prjfile_ls:

        suffix = ".prj"
        city = prjfile.replace(suffix,"")
        #print city
        if (city.upper() in shp_dir) or (city.lower() in shp_dir):#忽略shp中城市名大小写
            prjfile_dir = os.path.join(prjdir,prjfile)
            return prjfile_dir
            break#退出最内层循环
        
#如果列表中的元素是字符串，判断任一元素不被包含在其他元素中

num_shp = 0
num_shp_ok = 0
num_shp_fail = 0
##针对文件夹内shp,建立对应所在投影文件夹、并投影
#参数：inWorkspace待投影成果根目录,ini_root(=inWorkspace)新建投影文件夹替换字符用
def projection(inWorkspace,prjdir,prjWorkspace):#递归函数的参数只能是变量参数
    
    global num_shp
    global num_shp_ok
    global num_shp_fail

    file_names = os.listdir(inWorkspace)

    for file_name in file_names:#文件或文件夹名，不是绝对路径
        file_dir = os.path.join(inWorkspace,file_name)#待投影文件的绝对路径

        if os.path.isdir(file_dir):#判断是否为文件夹

            #建立对应投影成果文件夹
            prjSubfolder= file_dir.replace(inWorkspace,prjWorkspace)
            os.mkdir(prjSubfolder)

            #inWorkspace = file_dir#将当前文件夹当作根目录

            projection(file_dir,prjdir,prjSubfolder)#递归

        else:
            if isShapefile(file_name):
                #投影成果shp的绝对路径
                prj_file_dir = file_dir.replace(inWorkspace,prjWorkspace)
                #print prj_file_dir
                
                #投影文件prj的绝对路径                
                prjfile_dir = prjMatch(file_dir,prjdir)
                print prjfile_dir
                
                try:
                    arcpy.Project_management(file_dir, prj_file_dir, prjfile_dir)
                    #prj_file_dir投影成果shp文件的路径,prjfile_dir投影文件的路径
                    num_shp_ok += 1
                    print file_dir + u"投影成功！"
                except:
                    num_shp_fail += 1
                    print file_dir + u"投影失败！"

            else:
                pass
                #print "Srange ERROR in: "+file_dir

    print inWorkspace + " 文件夹投影完成！"#注意不是局部变量inWorkspace
    print str(num_shp_ok) + "shp文件投影成功！"
    print str(num_shp_ok) + "shp文件投影失败！"

##    return paths
if __name__ == '__main__':
    time_start=time.time()
    prjWorkspace = createPrjFile(inWorkspace,add_str="prj_")#新建投影成果根目录prjWorkspace
    projection(inWorkspace,prjdir,prjWorkspace)
    time_end=time.time()
    print u'投影耗时：{:.2f}min'.format((time_end-time_start)/60)
