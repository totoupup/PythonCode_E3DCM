# -*- coding: utf-8 -*-
#MIF格式文件合并——含读写相关计数
#【写完后注意检查MIF第9行——DataNONE！！！改为2行】

import os
#import shutil

#city_ls = ['TIANJIN','XIANGGANG']
#01输入——待合并的城市租户文件，包含mif和mid格式的文件
MIF_path = r"D:\PythonCode_E3DCM\01Data\06TenantMerge\TENANT\\"
#02输出——合并成果的租户文件
MERGE_path = r"D:\PythonCode_E3DCM\01Data\06TenantMerge\TENANT_MERGE"
mif_merge = MERGE_path + "\\CN_TENANT.mif"#02-1带前9行头文件的待写入mif文件
mid_merge = MERGE_path + "\\CN_TENANT.mid"#02-2待写入的空mid文件
#03输出——租户统计文件
merge_csv = MERGE_path + "\\Tenant_Merge.csv"


#待合并的城市租户文件列表
MIF_ls = os.listdir(MIF_path)
#输入mif文件中需要跳过的字符串（待写入mif文件已含此头文件）
forbid_txt = 'Version 300\
Charset "Neutral"\
Delimiter ","\
CoordSys Earth Projection 1, 104\
Columns 3\
  PID Char(10)\
  FEATURETYPE Char(1)\
  PARENTPOIID Char(10)\
Data'

#mif、mid写入行数
sum_mif = 0
sum_mid = 0
#mif、mid写入的文件个数
mif_file = 0
mid_file = 0

for file in MIF_ls:
    #读所有的mif、mid文件
    #print(file)
    cnt_mif = 0
    cnt_mid = 0
    f1 = open(MIF_path + file,"rt")
    write_txt_ls = f1.readlines()
    #print(write_txt_ls)

    #分别写mif和mid文件
    f_mif = open(mif_merge,"a")#追加写模式
    f_mid = open(mid_merge,"a")
    f_csv = open(merge_csv,"a")
    

    #mif文件的行写入txt
    if '.mif' in  file:
        mif_file += 1
        for line in write_txt_ls:
            #print('line[:-1]'+line[:-1])
            if line[:-1] not in forbid_txt:#['Version 300\n', 'Charset "Neutral"\n'...]
                f_mif.write(line)
                cnt_mif += 1
                #print("mif:"+line)
        record_line_mif = file + ':写入'+ str(cnt_mif) + '行！'#记录写入信息
        print(record_line_mif)
        f_csv.write(record_line_mif+"\n")

    #mid文件的行写入txt
    if '.mid' in  file:
        mid_file += 1
        for line in write_txt_ls:
            f_mid.write(line)
            cnt_mid += 1
            #print("mid:"+line)
        record_line_mid = file + ':写入'+ str(cnt_mid) + '行！'
        print(record_line_mid)
        f_csv.write(record_line_mid+"\n")

    #记mif、mid总写入行数
    sum_mif += cnt_mif
    sum_mid += cnt_mid

#关闭文件
f1.close()
f_mif.close()
f_mid.close()

#mif写入文件数，写入总行数
sum_record_line_mif = "MIF merge OK!"+' 共写入'+str(mif_file) + '文件！ '+ str(sum_mif) + '行！'
print(sum_record_line_mif)
f_csv.write(sum_record_line_mif+"\n")

#mid写入文件数，写入总行数
sum_record_line_mid = "MID merge OK!"+' 共写入'+str(mid_file) + '文件！ '+ str(sum_mid) + '行！'
print(sum_record_line_mid)
f_csv.write(sum_record_line_mid+"\n")


f_csv.close()
