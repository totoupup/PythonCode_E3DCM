#coding=utf-8
#————————————————————————————————
#                   打印出切图log中未“已修正”的数据行
#                           在python3运行
#                   把log文件放在.py程序同一目录下
#————————————————————————————————

log = u'SHENZHEN_蓝_19Q2_Collada(19-04-16).log' #log文件名 【运行前自行修改！】
f = open(log,'rt',encoding='UTF-8')
log = f.readlines()
num = 0
for line in log:
    if '已修正' not in line:
        print(line)
        num += 1
       
print("检查完成：共以上{}行数据未提示“已修正”，请确认！".format(num))        
