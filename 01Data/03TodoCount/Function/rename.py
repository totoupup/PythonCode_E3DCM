#���ļ��и���
#��·N���ļ�������д������
import os

dir  = r"D:\PythonCode_E3DCM\01Data\03TodoCount\output\Result_big5"

for city in os.listdir(dir):
    
    oldname_folder = "��·2��"#������ļ�����
    newname_folder = "��·1��"#��ĳɵ���ȷ�ļ�����

    old_dir = os.path.join(dir,city,oldname_folder)
    new_dir = os.path.join(dir,city,newname_folder)   

    os.rename(old_dir,new_dir)
    print("{} OK!".format(new_dir)) 

print ("ALL OK!")
