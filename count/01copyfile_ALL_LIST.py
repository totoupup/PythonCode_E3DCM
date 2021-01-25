#-*- coding: utf-8 -*-

import os
import shutil
#批量处理的60个城市
city_names=os.listdir(r"D:/PythonCode_E3DCM/01Data/08CreateBagEX2/ROAD_EX2_DATA/copyfrom/02prjROAD")
version_no = "20Q4"#【修改版本号】

#RD_LINK、RD_NODE所有后缀的文件存入列表
link_node_LIST = []
file_type = ['.dbf','.prj','.sbn','.sbx','.shp','.shx']
for type in file_type:
    copy_file_LINK = 'RD_LINK' + type
    link_node_LIST.append(copy_file_LINK)
    copy_file_NODE = 'RD_NODE' + type
    link_node_LIST.append(copy_file_NODE)
        

for city in city_names:
    #【输入】
    #01警示信息路径
    copyfrom_dir_WARNING = 'D:/PythonCode_E3DCM/01Data/08CreateBagEX2/ROAD_EX2_DATA/copyfrom/01WARNING/'
    #02打断前link&node
    copyfrom_dir = 'D:/PythonCode_E3DCM/01Data/08CreateBagEX2/ROAD_EX2_DATA/copyfrom/02prjROAD/' + city.replace("","") +'/'
    #03打断后link&node
    copyfrom_dir_EX2 = 'D:/PythonCode_E3DCM/01Data/08CreateBagEX2/ROAD_EX2_DATA/copyfrom/03prjROAD_EX2/' + city.replace("","") +'/'


    #【输出:成果打断包路径】
    copyto_dir = 'D:/PythonCode_E3DCM/01Data/08CreateBagEX2/ROAD_EX2_DATA/copyto/ROAD_EX2/'+city.replace(version_no,"")+'/'
    #新建打断包文件夹
    #os.mkdir(copyto_dir)

    #01遍历拷贝警示信息文件——不用改名
    warning_files = os.listdir(copyfrom_dir_WARNING)
    for warning in warning_files:
        #路径+文件名
        old_filename_WARNING = copyfrom_dir_WARNING + warning
        new_filename_WARNING = copyto_dir + warning
        shutil.copyfile(old_filename_WARNING,new_filename_WARNING)
        #print(city+'警示信息拷贝完成！')
    print(city+'全部警示信息拷贝完成！')#一个城市的全部警示信息拷贝完才打印

    #02遍历拷贝RD_LINK、RD_NODE文件——并改名为相应打断前、后
# =============================================================================
     for link_node_file in link_node_LIST:
     #——————————————LINK/NODE源数据——copyfrom————————————————————————
         #打断前
         old_filename = copyfrom_dir + link_node_file
         #打断后——#注意拷贝前文件名是否添加了"打断后"
         old_filename_EX2 = copyfrom_dir_EX2 + link_node_file
         #old_filename_EX2 = copyfrom_dir_EX2 + link_node_file[0:2] + '打断后' + link_node_file[-9:]
 
         #——————————————LINK/NODE打断包数据——copyto————————————————————
         #打断前
         new_filename = copyto_dir + link_node_file[0:2] + '打断前' + link_node_file[-9:]
         #打断后
         new_filename_EX2 = copyto_dir + link_node_file[0:2] + '打断后' + link_node_file[-9:]
         
 
         #——————————————拷贝处理———————————————————————————————
         #打断前
         shutil.copyfile(old_filename,new_filename)        
         #打断后
         shutil.copyfile(old_filename_EX2,new_filename_EX2)
         
         #print(city + 'LINK、NODE拷贝完成')
     print(city +'全部LINK、NODE拷贝完成')
# =============================================================================
#    
print('打断数据包已全部生成！')

