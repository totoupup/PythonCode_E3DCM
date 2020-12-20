#coding=utf-8
# ---------------------------------------------------------------------------
# Description: 拷贝prj平面坐标文件给导出shp copy .prj to shp
# ---------------------------------------------------------------------------

import os,shutil
from config import from_dir,from_dir_big5,prj_dir,old_vno,new_vno

def CopyPrj(from_dir):
    num = 0
    for city in os.listdir(from_dir):

        print(city)

        from_file = os.path.join(prj_dir, city+".prj")

        prj_V1 = city.upper() + "_" + old_vno + "_LINK.prj"
        prj_V2 = city.upper() + "_" + new_vno + "_LINK.prj"

        to_file_V1 = os.path.join(from_dir, city, prj_V1)
        to_file_V2 = os.path.join(from_dir, city, prj_V2)

        if os.path.exists(to_file_V1) == False:

            shutil.copy(from_file,to_file_V1)
            print(prj_V1 + " copied!")
            num +=1
        else:
            print(prj_V1 + " existed!")
        
        if os.path.exists(to_file_V2) == False:
            
            shutil.copy(from_file,to_file_V2)
            print(prj_V2 + " copied!")
            num +=1
        else:
            print(prj_V1 + " existed!")

    print("Total {} prj copied!".format(str(num)))


if __name__ == "__main__":
    CopyPrj(from_dir)
    CopyPrj(from_dir_big5)
    
    

