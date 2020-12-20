# -*- coding: utf-8 -*-

#62个城市
city_ce_dict={#配合arcpy包使用python2.7，注意语法
u'三亚':'SANYA',
u'东莞':'DONGGUAN',
u'中山':'ZHONGSHAN',
u'乌鲁木齐':'WULUMUQI',
u'佛山':'FOSHAN',
u'保定':'BAODING',
u'兰州':'LANZHOU',
u'南京':'NANJING',
u'南宁':'NANNING',
u'南昌':'NANCHANG',
u'南通':'NANTONG',
u'厦门':'XIAMEN',
u'台州':'TAIZHOU',
u'合肥':'HEFEI',
u'呼和浩特':'HUHEHAOTE',
u'哈尔滨':'HAERBIN',
u'唐山':'TANGSHAN',
u'大连':'DALIAN',
u'天津':'TIANJIN',
u'太原':'TAIYUAN',
u'宁波':'NINGBO',
u'常州':'CHANGZHOU',
u'徐州':'XUZHOU',
u'惠州':'HUIZHOU',
u'成都':'CHENGDU',
u'扬州':'YANGZHOU',
u'无锡':'WUXI',
u'昆明':'KUNMING',
u'杭州':'HANGZHOU',
u'柳州':'LIUZHOU',
u'武汉':'WUHAN',
u'泉州':'QUANZHOU',
u'济南':'JINAN',
u'海口':'HAIKOU',
u'温州':'WENZHOU',
u'潍坊':'WEIFANG',
u'烟台':'YANTAI',
u'珠海':'ZHUHAI',
u'盐城':'YANCHENG',
u'石家庄':'SHIJIAZHUANG',
u'福州':'FUZHOU',
u'秦皇岛':'QINHUANGDAO',
u'绍兴':'SHAOXING',
u'芜湖':'WUHU',
u'苏州':'SUZHOU',
u'西宁':'XINING',
u'西安':'XIAN',
u'贵阳':'GUIYANG',
u'郑州':'ZHENGZHOU',
u'重庆':'CHONGQING',
u'金华':'JINHUA',
u'银川':'YINCHUAN',
u'长春':'CHANGCHUN',
u'长沙':'CHANGSHA',
u'青岛':'QINGDAO',
u'沈阳':'SHENYANG',
u'广州':'GUANGZHOU',
u'上海':'SHANGHAI',
u'深圳':'SHENZHEN',
u'北京':'BEIJING',
u'香港':'XIANGGANG',
u'澳门':'AOMEN'
}

# english-chinese
city_ec_dict = dict(zip(city_ce_dict.values(), city_ce_dict.keys()))

if __name__ == '__main__':
  print 'chinese-english'
  for key, value in city_ce_dict.items():
    print key, value

  print 'english-chinese'
  for key, value in city_ec_dict.items():
    print key, value
