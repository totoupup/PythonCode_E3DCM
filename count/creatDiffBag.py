#����������������������������������������������������������������������������������������������������������������������������������������������������������������������
#                                   1�½���������д�ļ���
#                   2�������汾���������������ļ����ڣ�ע�����ǰ���ñ��ݣ�
#                       ����ǰע���޸Ļ�ȷ�ϡ�������/���·�����汾��
#����������������������������������������������������������������������������������������������������������������������������������������������������������������������

import os,shutil
import time
time_start = time.time()
#������·����
from_dir_v1 = r"D:\PythonCode_E3DCM\01Data\02CreateDiffBag\bag_V1"#�ȶ�������V1·�����޸�1��
from_dir_v2 = r"D:\PythonCode_E3DCM\01Data\02CreateDiffBag\bag_V2"#�ȶ�������V2·�����޸�2��
#�����·����
to_dir = r"D:\PythonCode_E3DCM\01Data\02CreateDiffBag\Diffbag"#�������ȶ��ļ��и�Ŀ¼
#���汾�š�
v1_no = "20Q4M2G2"#�ȶ�������V1�汾�š��޸�3��
v2_no = "21Q1G1"#�ȶ�������V2�汾�š��޸�4��

num = 0
for i in os.listdir(from_dir_v2):##ע��from_dir_v2��ֻ�������������ļ���
    #print(i)
    
    city = i.split("_")[0]#������
    print(city)
    
    #�½������ļ���
    mkdir_city = os.path.join(to_dir,city)
    if os.path.exists(mkdir_city) == False:
        os.mkdir(mkdir_city)
        print(city + "�ļ����½���ɣ�")
    else:
        print(city + "�ļ����Ѵ��ڣ�")
        

    des = os.path.join(to_dir,city)

    #����V1������
    v1_name = city + "_" + v1_no
    v1_dir_old = os.path.join(from_dir_v1,v1_name)
    
    shutil.move(v1_dir_old,des)
    print(v1_name + "������ɣ�")

    #����V2������
    v2_name = city + "_" + v2_no
    v2_dir_old = os.path.join(from_dir_v2,v2_name)
    
    shutil.move(v2_dir_old,des)
    print(v2_name + "������ɣ�")

    num += 1

time_end = time.time()
print(str(num)+"���п�����ɣ�")
print('������ʱ��{:.2f}min'.format((time_end-time_start)/60))
