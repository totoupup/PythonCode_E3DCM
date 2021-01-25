# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:14:58 2021

@author: zhutong
"""

import os,shutil
root = r"D:\20Q4M1\03spline理论检查"


city_ls = os.listdir(root)

for city in city_ls:
    print(city + " is coping...")
    
    from_dir = os.path.join(root, city, "目录模板\MIDDLEDATA\MID_4\MID_4全部")
    to_dir = os.path.join(root, city, "目录模板\MIDDLEDATA\MID_4")
    
    file_ls =  os.listdir(from_dir)
    
    for file in file_ls:
        
        from_file = os.path.join(from_dir, file)
        to_file = os.path.join(to_dir, file)
        
        if os.path.exists(to_file):
            os.unlink(to_file)#删除文件
            shutil.copy(from_file, to_dir)
            print(from_file + " copied!")
    
    print(from_dir + " all copied!") 

print("All copied!")