#给文件夹改名
#道路N次文件夹名字写错的情况
import os

dir  = r"D:\PythonCode_E3DCM\01Data\03TodoCount\output\Result_big5"

for city in os.listdir(dir):
    
    oldname_folder = "道路2次"#错误的文件夹名
    newname_folder = "道路1次"#想改成的正确文件夹名

    old_dir = os.path.join(dir,city,oldname_folder)
    new_dir = os.path.join(dir,city,newname_folder)   

    os.rename(old_dir,new_dir)
    print("{} OK!".format(new_dir)) 

print ("ALL OK!")
