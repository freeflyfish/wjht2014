#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-19 下午2:40
# @Author  : Gavin
# @Site    : 
# @File    : tianyan.py
# @Software: PyCharm

import sys
sys.path.append('/home/gavin/PycharmProjects/scrapy/TianYanCha')
from scrapy.spiders import Spider
from scrapy.selector import Selector
from TianYanCha.items import Tianyan
from scrapy import http
import scrapy

class TianyanSpider(Spider):
    name = "Tianyan"

    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en',
        'Tyc-From': 'normal',
        'CheckError': 'check',
        'Connection': 'keep-alive'
    }
    cookie = {'Hm_lvt_e92c8d65d92d534b0fc290df538b4758': '1521096752,1521442110', 'TYCID': '6eaa7e70281d11e886c4e3e6089348bd', 'aliyungf_tc': 'AQAAAIrCKXpu/AUAjhpad/l8U0gI7K4u', 'RTYCID': '6f75ee2442d84840b8863557dd390349', 'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758': '1521624571', 'bannerFlag': 'true', 'csrfToken': '7at1nnS0fGNQqbT0JMI1ARk8', 'ssuid': '9535358242', 'tyc-user-info': '%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTU5NzI3MCwiZXhwIjoxNTM3MTQ5MjcwfQ.ZhFj4YSsSayxN5pIaz8nfJgqey--5N17PFmFmTRZrh403bxKJtn1nsPIvOdxQaPggNawDpRb8_yZkLKLr78xyA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213693391722%2522%257D', 'undefined': '6eaa7e70281d11e886c4e3e6089348bd', 'auth_token': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTU5NzI3MCwiZXhwIjoxNTM3MTQ5MjcwfQ.ZhFj4YSsSayxN5pIaz8nfJgqey--5N17PFmFmTRZrh403bxKJtn1nsPIvOdxQaPggNawDpRb8_yZkLKLr78xyA'}









    def start_requests(self):

        citys = ['baoding', ]
        base_url = 'tianyancha.com/search'
        for city in citys:
            start_url='https://{0}.{1}'.format(city, base_url)
            # start_url = 'https://baoding.tianyancha.com/search'
            yield scrapy.Request(url=start_url,headers=self.header,cookies=self.cookie)

    def parse(self, response):
        sel = Selector(response)
        # print(response.body)
        sites = sel.xpath('//div[@class="search_right_item ml10"]/div/a')
        # print(sites.extract())
        items = []
        for site in sites:
            item = Tianyan()
            link = site.xpath('@href').extract()[0]
            name = site.xpath('span/text()').extract()[0]
            print(name)
        #
            item['link'] = link
            item['name'] = name
            items.append(item)
            yield http.Request(url=item["link"], meta={'item': item},headers= self.header,cookies=self.cookie,callback=self.parseDetail, dont_filter=True)
            # yield item
        print(sel.xpath('//div[@class="search_pager human_pager in-block"]/ul/li[@class="pagination-next ng-scope "]/a').extract())
        nextPage = sel.xpath('//div[@class="search_pager human_pager in-block"]/ul/li[@class="pagination-next ng-scope "]/a/@href').extract()
        if nextPage:
            next = nextPage[0]
            yield http.Request(next, callback=self.parse)


    def  parseDetail(self,response):
        item = response.meta['item']


        selector = Selector(response)
        info = selector.xpath('//div[@class="company_header_width ie9Style position-rel"]')
        # print(rr.extract())
        ##company
        company=info.xpath('div[@class="position-rel"]/span/text()').extract()

        if company:
            company = company[0]
        else:
            company=''

        ##phone
        phone= info.xpath(
            'div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[@class="in-block vertical-top overflow-width mr20"]/span[2]/text()').extract()
        if phone:
            phone = phone[0]
        else:
            phone=''
        ##mail####
        mail = info.xpath(
            # 'div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[@class="in-block vertical-top"]/span[@class="in-block vertical-top overflow-width"]/text()').extract()[
            'div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[2]/span[2]/text()').extract()

        if mail:
            mail = mail[0]
        else:
            mail = ''

        ##weburl
        weburl = info.xpath(
            'div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[@class="in-block vertical-top overflow-width mr20"]/a/@href').extract()

        if weburl:
            weburl = weburl[0]
        else:
            weburl = ''

        ##address
        address = info.xpath(
            'div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[@class="in-block vertical-top"]/span[@class="in-block overflow-width vertical-top"]/text()').extract()

        if address:
            address = address[0]
        else:
            address = ''

        ##introduce
        # introduce = info.xpath(
        #     'div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[@class="sec-c2 over-hide"]/script/text()').extract()[
        #           0]
        introduce = info.xpath(
            'div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[@class="sec-c2 over-hide"]/span[2]/text()').extract()

        if introduce:
            introduce = address[0]
        else:
            introduce = ''

        ##################公司背景
        baseInfo = selector.xpath('//div[@id="_container_baseInfo"]/div')

        #####法人信息
        frxx = baseInfo.xpath(
            'div[@class="baseInfo_model2017"]/table[@class="table companyInfo-table text-center f14"]/tbody/tr/td[@style="padding: 0px"]')
        ###法人代表
        fddbr = frxx.xpath('div/div[@class="human-top"]/div[@class="in-block vertical-top pl15"]/div/a/text()').extract()
        if fddbr:
            fddbr = fddbr[0]
        else:
            fddbr = ''

        ###法人其他公司
        fddbrcompany = frxx.xpath(
            'div/div[@class="human-bottom sec-c4 pt10"]/div/div[@class="pull-right f14 sec-c2"]/span/@title').extract()

        if fddbrcompany:
            fddbrcompany = fddbrcompany[0]
        else:
            fddbrcompany = ''


        ######注册信息
        zcxx = baseInfo.xpath(
            'div[@class="baseInfo_model2017"]/table[@class="table companyInfo-table text-center f14"]/tbody/tr/td[@style="padding: 0;"]')

        ###注册资本
        zczb= zcxx.xpath('div[@class="new-border-bottom"]/div[@class="pb10"]/div/text/text()').extract()


        if zczb:
            zczb = zczb[0]
        else:
            zczb = ''

        ###注册时间
        zcsjj = zcxx.xpath('div[@class="new-border-bottom pt10"]/div[@class="pb10"]/div/text/text()').extract()

        if zcsjj:
            zcsjj = zcsjj[0]
        else:
            zcsjj = ''
        ###公司状态
        gszt = zcxx.xpath('div[@class="pt10"]/div[2]/div/text()').extract()

        if gszt:
            gszt = gszt[0]
        else:
            gszt = ''

        ################################公司信息
        baseInfo1 = baseInfo.xpath('div[@class="base0910"]/table[@class="table companyInfo-table f14"]/tbody')

        ###工商注册号

        gszch = baseInfo1.xpath('tr[1]/td[2]/text()').extract()
        if gszch:
            gszch = gszch[0]
        else:
            gszch = ''

        ###组织机构代码
        zzjgdm = baseInfo1.xpath('tr[1]/td[4]/text()').extract()
        if zzjgdm:
            zzjgdm = zzjgdm[0]
        else:
            zzjgdm = ''

        ###统一信用代码
        tyxydm = baseInfo1.xpath('tr[2]/td[2]/text()').extract()
        if tyxydm:
            tyxydm = tyxydm[0]
        else:
            tyxydm = ''

        ###公司类型
        gslx = baseInfo1.xpath('tr[2]/td[4]/text()').extract()
        if gslx:
            gslx = gslx[0]
        else:
            gslx = ''

        ###纳税人识别号
        nsrsbh = baseInfo1.xpath('tr[3]/td[2]/text()').extract()
        if nsrsbh:
            nsrsbh = nsrsbh[0]
        else:
            nsrsbh = ''

        ###行业
        hy = baseInfo1.xpath('tr[3]/td[4]/text()').extract()
        if hy:
            hy = hy[0]
        else:
            hy = ''

        ###营业期限
        yyqx = baseInfo1.xpath('tr[4]/td[2]/span/text()').extract()
        if yyqx:
            yyqx = yyqx[0]
        else:
            yyqx = ''

        ###核准日期
        hzrq = baseInfo1.xpath('tr[4]/td[4]/text/text()').extract()
        if hzrq:
            hzrq = hzrq[0]
        else:
            hzrq = ''

        ###登记机关
        djjg = baseInfo1.xpath('tr[5]/td[2]/text()').extract()
        if djjg:
            djjg = djjg[0]
        else:
            djjg = ''

        ###英文名称
        ywmc = baseInfo1.xpath('tr[5]/td[4]/text()').extract()
        if ywmc:
            ywmc = ywmc[0]
        else:
            ywmc = ''

        ###注册地址
        zcdz = baseInfo1.xpath('tr[6]/td[2]/text()').extract()
        if zcdz:
            zcdz = zcdz[0]
        else:
            zcdz = ''

        ###经营范围####
        jyfw = baseInfo1.xpath('tr[7]/td[2]/span/span/span[1]/text()').extract()
        if jyfw:
            jyfw= jyfw[0]
        else:
            jyfw = ''



        item['company'] = company
        item['phone'] = phone
        item['mail'] = mail
        item['weburl'] = weburl
        item['address'] = address
        item['introduce'] = introduce
        item['fddbr'] = fddbr
        item['fddbrcompany'] = fddbrcompany
        item['zczb'] = zczb
        item['zcrq'] = zcsjj
        item['gszt'] = gszt
        item['gszch'] = gszch
        item['zzjgdm'] = zzjgdm
        item['tyxydm'] = tyxydm
        item['gslx'] = gslx
        item['nsrsbh'] = nsrsbh
        item['hy'] = hy
        item['yyqx'] = yyqx
        item['hzrq'] = hzrq
        item['djjg'] = djjg
        item['ywmc'] = ywmc
        item['zcdz'] = zcdz
        item['jyfw'] = jyfw

        yield item



