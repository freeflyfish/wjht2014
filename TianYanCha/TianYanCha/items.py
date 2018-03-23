# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianyanchaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Tianyan(scrapy.Item):
    link = scrapy.Field()##链接
    name = scrapy.Field()##索引列名称
    company = scrapy.Field()##公司名称
    phone = scrapy.Field()##电话
    mail = scrapy.Field()##邮箱
    weburl = scrapy.Field()##网址
    address = scrapy.Field()##地址
    introduce = scrapy.Field()##简介
    fddbr = scrapy.Field()##法定代表人
    fddbrcompany = scrapy.Field()##法定代表人其他公司
    zczb = scrapy.Field()##注册资本
    zcrq = scrapy.Field()##注册日期
    gszt = scrapy.Field()##公司状态
    gszch = scrapy.Field()##工商注册号
    zzjgdm = scrapy.Field()##组织机构代码
    tyxydm = scrapy.Field()##统一信用代码
    gslx = scrapy.Field()##公司类型
    nsrsbh = scrapy.Field()##纳税人识别号
    hy = scrapy.Field()##行业
    yyqx = scrapy.Field()##营业期限
    hzrq = scrapy.Field()##核准日期
    djjg = scrapy.Field()##登记机关
    ywmc = scrapy.Field()##英文名称
    zcdz = scrapy.Field()##注册地址
    jyfw = scrapy.Field()##经营范围

