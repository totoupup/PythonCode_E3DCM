#——————————————————————————————————————————————————————————————————————
#
#                   修正POI的cpg编码文件内容:从UTF-8转为936
#
#——————————————————————————————————————————————————————————————————————
import os,shutil

root = r"D:\00通用工具\00FME\背景POI提取_上海outline扩面积更新\20Q4_BACK&POI_catch\data2"#POI所在路径【运行前确认修改！】
correct_cpg = r"D:\PythonCode_E3DCM\01Data\04BackPoiProcess\02POI\correct_cpg\IX_POI.cpg"#正确cpg文件所在路径

num = 0
for file in os.listdir(root):

    des = os.path.join(root,file,'IX_POI.cpg')
    shutil.copy(correct_cpg,des)
    
    num += 1
    print("{}的cpg更新完成！".format(file))

print("{} all OK!".format(str(num)))
