#coding=utf-8
#———————————————————————————————————————————————————————————————————————
#
#                   【DAE城市大小数量统计-E3DCM及TL通用】
#                  运行环境Anaconda——spyder——PYthon3.8
#                      统计压缩包对应的压缩前文件大小
#
#———————————————————————————————————————————————————————————————————————
import rarfile
#【输出以MB为单位】

#按照城市统计顺序统计
city_ls = ['BEIJING', 'SHANGHAI', 'GUANGZHOU', 'SHENZHEN', 'SHENYANG', 'XIAN',
 'CHENGDU', 'TIANJIN', 'NANJING', 'HANGZHOU', 'SUZHOU', 'ZHENGZHOU',
 'WUHAN', 'NINGBO', 'WUXI', 'WENZHOU', 'CHANGSHA', 'CHANGCHUN',
 'XIANGGANG', 'DALIAN', 'DONGGUAN', 'TAIYUAN', 'HEFEI', 'JINAN',
 'HAERBIN', 'QINGDAO', 'CHONGQING', 'KUNMING', 'XIAMEN', 'NANNING',
 'FOSHAN', 'FUZHOU', 'TANGSHAN', 'AOMEN', 'HUHEHAOTE', 'YANTAI',
 'WULUMUQI', 'NANCHANG', 'YANGZHOU', 'LANZHOU', 'GUIYANG', 'BAODING',
 'SHIJIAZHUANG', 'QUANZHOU', 'HAIKOU', 'SHAOXING', 'TAIZHOU', 'SANYA',
 'LIUZHOU', 'WEIFANG', 'QINHUANGDAO', 'XINING', 'ZHUHAI', 'XUZHOU',
 'YANCHENG', 'ZHONGSHAN','YINCHUAN', 'WUHU', 'NANTONG', 'JINHUA',
 'HUIZHOU', 'CHANGZHOU']

def unitConvert_MB(size):

    #字节单位换算
    convert_MB = 1024*1024 #1MB对应的字节数

    #计入字符串
    convert_size = '{0:.2F}MB'.format(size/convert_MB)
    return convert_size       


def getSize(city):
    #注意定义在函数外部的变量，内部使用时需声明全局变量global
    sum_S = sum_DAE = sum_XREF = sum_DAY = sum_NIGHT = sum_DAE_file = 0

    rf = rarfile.RarFile(city+'.rar')    
    for f in rf.infolist():
    #print(f.filename, f.file_size)#file_size为字节大小 1KB=1024字节

        #【1】DAE文件(MB)
        #_H、_XREF、_B1、_B2文件合计大小
        if '_S.dae' in f.filename:
            sum_S += f.file_size

        #【2】 XREF纹理库文件(MB)
        #   XREF文件夹
        if 'DAE/XREF' in f.filename:
            sum_XREF += f.file_size
		
        #【3】DAY纹理库文件(MB)
	#   TEXTURES下DAY文件夹 
        if 'DAE/TEXTURES/DAY' in f.filename:
            sum_DAY += f.file_size

        #【4】NIGHT纹理库文件(MB)
        #   TEXTURES下NIGHT文件夹
        if 'DAE/TEXTURES/NIGHT' in f.filename:
            sum_NIGHT += f.file_size

	#【5】小计（MB）
	#   DAE文件夹
        if '/DAE' in f.filename:
            sum_DAE_file += f.file_size

    sum_DAE = sum_DAE_file-sum_XREF-sum_DAY-sum_NIGHT#最新统计时不去除S.dae
    #sum_DAE = sum_DAE_file-sum_S-sum_XREF-sum_DAY-sum_NIGHT
    ls_size = [city,unitConvert_MB(sum_DAE),unitConvert_MB(sum_XREF),unitConvert_MB(sum_DAY),unitConvert_MB(sum_NIGHT),unitConvert_MB(sum_DAE_file)]    
    print(ls_size)
    return ls_size


#统计结果存入CSV
ls_title = ['城市','DAE文件','XREF纹理库文件','DAY纹理库文件','NIGHT纹理库文件','小计']
print(ls_title)
f = open('size_count.csv','w')
f.write(','.join(ls_title)+'\n') 

num = 0
for city in city_ls:
    try:
        f.write(','.join(getSize(city))+'\n')
        num += 1
    except:
        continue
#及时关闭，否则无法写入
f.close()
print('统计完成！共统计了{}个城市'.format(num))



