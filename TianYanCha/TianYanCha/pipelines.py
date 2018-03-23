# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class TianyanchaPipeline(object):
#     def process_item(self, item, spider):
#         return item

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item

import json
import pymysql


class TianyanchaPipeline(object):
    def __init__(self):
        self.file=open('item','w',encoding='utf-8')

    def process_item(self,item,spider):
        line=json.dumps(dict(item), ensure_ascii=False)

        self.file.write(line +"\r\n" )
        return item

    def close_spider(self, spider):
        self.file.close()



class MysqlPipeline(object):
    def __init__(self):
        config = {
            'host': '192.168.1.200',
            'port': 3308,
            'user': 'root',
            'password': '1qaz@WSX',
            'db': 'data_department',
            'charset':'utf8',

        }
        self.connect = pymysql.connect(**config)
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        link = item['link']
        name = item['name']
        company = item['company']
        phone = item['phone']
        mail = item['mail']
        weburl = item['weburl']
        address = item['address']
        introduce = item['introduce']
        fddbr = item['fddbr']
        fddbrcompany = item['fddbrcompany']
        zczb = item['zczb']
        zcrq = item['zcrq']
        gszt = item['gszt']
        gszch = item['gszch']
        zzjgdm = item['zzjgdm']
        tyxydm = item['tyxydm']
        gslx = item['gslx']
        nsrsbh = item['nsrsbh']
        hy = item['hy']
        yyqx = item['yyqx']
        hzrq = item['hzrq']
        djjg = item['djjg']
        ywmc = item['ywmc']
        zcdz = item['zcdz']
        jyfw = item['jyfw']

        insert_sql = """
            insert into gsxx(link,name,company,phone,mail,weburl,address,introduce,fddbr,fddbrcompany,zczb,zcrq,gszt,gszch,zzjgdm,tyxydm,gslx,nsrsbh,hy,yyqx,hzrq,djjg,ywmc,zcdz,jyfw)
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """
        para = (link,name,company,phone,mail,weburl,address,introduce,fddbr,fddbrcompany,zczb,zcrq,gszt,gszch,zzjgdm,tyxydm,gslx,nsrsbh,hy,yyqx,hzrq,djjg,ywmc,zcdz,jyfw)

        self.cursor.execute(insert_sql,para)
        self.connect.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
