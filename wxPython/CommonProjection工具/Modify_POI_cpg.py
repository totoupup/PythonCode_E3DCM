#��������������������������������������������������������������������������������������������������������������������������������������������
#
#                   ����POI��cpg�����ļ�����:��UTF-8תΪ936
#
#��������������������������������������������������������������������������������������������������������������������������������������������
import os,shutil

root = r"D:\00ͨ�ù���\00FME\����POI��ȡ_�Ϻ�outline���������\20Q4_BACK&POI_catch\data2"#POI����·��������ǰȷ���޸ģ���
correct_cpg = r"D:\PythonCode_E3DCM\01Data\04BackPoiProcess\02POI\correct_cpg\IX_POI.cpg"#��ȷcpg�ļ�����·��

num = 0
for file in os.listdir(root):

    des = os.path.join(root,file,'IX_POI.cpg')
    shutil.copy(correct_cpg,des)
    
    num += 1
    print("{}��cpg������ɣ�".format(file))

print("{} all OK!".format(str(num)))
