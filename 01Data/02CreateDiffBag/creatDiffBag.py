#———————————————————————————————————————————————————————————————————————————————————
#                                   1新建城市名大写文件夹
#                   2剪切两版本的升级包到城市文件夹内，注意剪切前做好备份！
#                       运行前注意修改或确认——输入/输出路径、版本号
#———————————————————————————————————————————————————————————————————————————————————

import os,shutil
import time
time_start = time.time()
#【输入路径】
from_dir_v1 = r"D:\PythonCode_E3DCM\01Data\02CreateDiffBag\bag_V1"#比对升级包V1路径【修改1】
from_dir_v2 = r"D:\PythonCode_E3DCM\01Data\02CreateDiffBag\bag_V2"#比对升级包V2路径【修改2】
#【输出路径】
to_dir = r"D:\PythonCode_E3DCM\01Data\02CreateDiffBag\Diffbag"#升级包比对文件夹根目录
#【版本号】
v1_no = "20Q4M2G2"#比对升级包V1版本号【修改3】
v2_no = "21Q1G1"#比对升级包V2版本号【修改4】

num = 0
for i in os.listdir(from_dir_v2):##注意from_dir_v2里只能有升级城市文件夹
    #print(i)
    
    city = i.split("_")[0]#城市名
    print(city)
    
    #新建城市文件夹
    mkdir_city = os.path.join(to_dir,city)
    if os.path.exists(mkdir_city) == False:
        os.mkdir(mkdir_city)
        print(city + "文件夹新建完成！")
    else:
        print(city + "文件夹已存在！")
        

    des = os.path.join(to_dir,city)

    #剪切V1升级包
    v1_name = city + "_" + v1_no
    v1_dir_old = os.path.join(from_dir_v1,v1_name)
    
    shutil.move(v1_dir_old,des)
    print(v1_name + "拷贝完成！")

    #剪切V2升级包
    v2_name = city + "_" + v2_no
    v2_dir_old = os.path.join(from_dir_v2,v2_name)
    
    shutil.move(v2_dir_old,des)
    print(v2_name + "拷贝完成！")

    num += 1

time_end = time.time()
print(str(num)+"城市拷贝完成！")
print('拷贝耗时：{:.2f}min'.format((time_end-time_start)/60))
