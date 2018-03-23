#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-19 下午3:29
# @Author  : Gavin
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from scrapy.selector import Selector
import requests

from scrapy import http
from scrapy import http
# header = {
# 'Host': 'www.tianyancha.com',
# 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Tyc-From': 'normal',
# 'CheckError': 'check',
# 'Connection': 'keep-alive',
# 'Referer': 'https://www.tianyancha.com/company/2337540891',
# 'Cookie': 'TYCID=6eaa7e70281d11e886c4e3e6089348bd; undefined=6eaa7e70281d11e886c4e3e6089348bd; ssuid=9535358242; aliyungf_tc=AQAAAIrCKXpu/AUAjhpad/l8U0gI7K4u; csrfToken=7at1nnS0fGNQqbT0JMI1ARk8; RTYCID=57573a12cf2d430a8d369dba04dbf5e9; bannerFlag=true; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTQ0NTgyOCwiZXhwIjoxNTM2OTk3ODI4fQ.GXErnVAL3h0Hx8A5vw3NpQZSqTCcQkcctvZAxXSCfwpc6fDpgPqlBDYILZp-csZS6QpjYRuQPseVndJ9Lil4nw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213693391722%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTQ0NTgyOCwiZXhwIjoxNTM2OTk3ODI4fQ.GXErnVAL3h0Hx8A5vw3NpQZSqTCcQkcctvZAxXSCfwpc6fDpgPqlBDYILZp-csZS6QpjYRuQPseVndJ9Lil4nw; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1521096752,1521442110; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1521446995'
# }

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en',
    'Tyc-From': 'normal',
    'CheckError': 'check',
    'Connection': 'keep-alive',
    'Cookie': 'TYCID=6eaa7e70281d11e886c4e3e6089348bd; undefined=6eaa7e70281d11e886c4e3e6089348bd; ssuid=9535358242; aliyungf_tc=AQAAAIrCKXpu/AUAjhpad/l8U0gI7K4u; csrfToken=7at1nnS0fGNQqbT0JMI1ARk8; bannerFlag=true; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTU5NzI3MCwiZXhwIjoxNTM3MTQ5MjcwfQ.ZhFj4YSsSayxN5pIaz8nfJgqey--5N17PFmFmTRZrh403bxKJtn1nsPIvOdxQaPggNawDpRb8_yZkLKLr78xyA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213693391722%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTU5NzI3MCwiZXhwIjoxNTM3MTQ5MjcwfQ.ZhFj4YSsSayxN5pIaz8nfJgqey--5N17PFmFmTRZrh403bxKJtn1nsPIvOdxQaPggNawDpRb8_yZkLKLr78xyA; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1521096752,1521442110; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1521624571; RTYCID=6f75ee2442d84840b8863557dd390349'
}



index =requests.get('https://baoding.tianyancha.com/search?key=%E4%BF%9D%E5%AE%9A',headers=header)
selector = Selector(index)
nextPage = selector.xpath('//div[@class="search_pager human_pager in-block"]/ul/li[@class="pagination-next ng-scope "]/a/@href').extract()[0]
print(nextPage)
r=requests.get('https://www.tianyancha.com/company/2337540891',headers=header)

rr=Selector(r)
#
# a=rr.xpath('//div[@class="search_right_item ml10"]/div/a')
# print(a)
# for site in a:
#     print(site.xpath('@href').extract()[0] + site.xpath('span/text()').extract()[0])
# print(r.status_code)

# next_page= rr.xpath('//div[@class="search_pager human_pager in-block"]/ul/li[@class="pagination-next ng-scope "]/a/@href')
#
# print(next_page.extract()[0])

print(r.status_code)

#################基本信息
info = rr.xpath('//div[@class="company_header_width ie9Style position-rel"]')
# print(rr.extract())
##company
print(info.xpath('div[@class="position-rel"]/span/text()').extract()[0])

##phone
print(info.xpath('div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[@class="in-block vertical-top overflow-width mr20"]/span[2]/text()').extract()[0])

##mail
print(info.xpath('div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[@class="in-block vertical-top"]/span[@class="in-block vertical-top overflow-width"]/text()').extract()[0])

##weburl
print(info.xpath('div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[@class="in-block vertical-top overflow-width mr20"]/span[2]/text()').extract()[1])

##address
print(info.xpath('div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[@class="in-block vertical-top"]/span[@class="in-block overflow-width vertical-top"]/text()').extract()[0])


##introduce
print(info.xpath('div[@class="company_header_interior new-border pl10 pt10 pb10 position-rel  mt15"]/div[@class="f14 sec-c2"]/div[@class="sec-c2 over-hide"]/script/text()').extract()[0])

##################公司背景
baseInfo = rr.xpath('//div[@id="_container_baseInfo"]/div')

#####法人信息
frxx = baseInfo.xpath('div[@class="baseInfo_model2017"]/table[@class="table companyInfo-table text-center f14"]/tbody/tr/td[@style="padding: 0px"]')
###法人代表
print(frxx.xpath('div/div[@class="human-top"]/div[@class="in-block vertical-top pl15"]/div/a/text()').extract()[0])
###法人其他公司
print(frxx.xpath('div/div[@class="human-bottom sec-c4 pt10"]/div/div[@class="pull-right f14 sec-c2"]/span/@title').extract()[0])

######注册信息
zcxx = baseInfo.xpath('div[@class="baseInfo_model2017"]/table[@class="table companyInfo-table text-center f14"]/tbody/tr/td[@style="padding: 0;"]')

###注册资本
print(zcxx.xpath('div[@class="new-border-bottom"]/div[@class="pb10"]/div/text/text()').extract()[0])

###注册时间
print(zcxx.xpath('div[@class="new-border-bottom pt10"]/div[@class="pb10"]/div/text/text()').extract()[0])
###公司状态
print(zcxx.xpath('div[@class="pt10"]/div[2]/div/text()').extract()[0])

################################公司信息
baseInfo1 = baseInfo.xpath('div[@class="base0910"]/table[@class="table companyInfo-table f14"]/tbody')

###工商注册号

print(baseInfo1.xpath('tr[1]/td[2]/text()').extract()[0])

###组织机构代码
print(baseInfo1.xpath('tr[1]/td[4]/text()').extract()[0])

###统一信用代码
print(baseInfo1.xpath('tr[2]/td[2]/text()').extract()[0])

###公司类型
print(baseInfo1.xpath('tr[2]/td[4]/text()').extract()[0])

###纳税人识别号
print(baseInfo1.xpath('tr[3]/td[2]/text()').extract()[0])

###行业
print(baseInfo1.xpath('tr[3]/td[4]/text()').extract()[0])


###营业期限
print(baseInfo1.xpath('tr[4]/td[2]/span/text()').extract()[0])

###核准日期
print(baseInfo1.xpath('tr[4]/td[4]/text/text()').extract()[0])

###登记机关
print(baseInfo1.xpath('tr[5]/td[2]/text()').extract()[0])

###英文名称
print(baseInfo1.xpath('tr[5]/td[4]/text()').extract()[0])

###注册地址
print(baseInfo1.xpath('tr[6]/td[2]/text()').extract()[0])

###经营范围
print(baseInfo1.xpath('tr[7]/td[2]/span/span/span[@class="js-full-container hidden"]/text()').extract()[0])

'''<a href="https://baoding.tianyancha.com/search/p3?key=%E4%BF%9D%E5%AE%9A" class="ng-binding">&gt;</a>'''

'''
<div class="company_header_width ie9Style position-rel xh-highlight" style="margin-left:20px;"><div class="position-rel"><span class="f18 in-block vertival-middle sec-c2" style="font-weight: 600">保定市保北医药连锁有限责任公司</span><!--曾用名--><div class="c-white claim_yel ml10" onclick="claimCompany(2337540891)">我要认证</div><a class="c2" target="_blank" onclick="claimGate()"><span class="tic tic-circle-question-o point ml5"></span></a><p class="f14 mt10" style="line-height: 1.42857143;"><!--公司性质--><!--1，公司，2香港，3社会组织，4律所--><!--上市信息--></p></div><div class="company_header_interior new-border pl10 pt10 pb10 position-rel mt15"><div class="position-abs claim_home_slogan f12"><span class="ml10 hover_underline c19 point" onclick="claimPopGate(2337540891)">完成认证</span>可编辑该模块</div><!--联系方式等--><div class="f14 sec-c2" style="line-height: 26px;"><div class="in-block vertical-top overflow-width mr20" style="width: 280px;"><span class="sec-c3">电话：</span><span>03127550231</span><span class="ml10 c9 hover_underline point" onclick="claimPopGate(2337540891)">编辑</span><span class="pl10"><script type="text/html">["03127550231","0312-5097581","03125097621"]</script><span class="c9 hover_underline point" onclick="openPhonePopup(this)">查看更多</span></span></div><div class="in-block vertical-top" style="width:620px;"><span class="in-block vertical-top sec-c3">邮箱：</span><span class="in-block vertical-top overflow-width" style="max-width: 360px;" title="bbyyls@126.com">bbyyls@126.com</span><span class="ml10 c9 hover_underline point" onclick="claimPopGate(2337540891)">编辑</span></div></div><div class="f14 sec-c2" style="line-height: 26px;"><div class="in-block vertical-top overflow-width mr20" style="width: 280px;"><span class="sec-c3">网址：</span><span class=" c9 hover_underline point" onclick="claimPopGate(2337540891)">添加</span></div><div class="in-block vertical-top" style="width: 620px;"><span class="in-block vertical-top sec-c3">地址：</span><span class="in-block overflow-width vertical-top" style="max-width: 530px;" title="保定市长城北大街2353号">保定市长城北大街2353号</span><span class="ml10 c9 hover_underline point" onclick="claimPopGate(2337540891)">编辑</span></div></div><div class="f14 sec-c2" style="line-height: 26px;"><div class="sec-c2 over-hide" style="line-height: 24px;"><span class="sec-c3">简介：</span><span>保定市保北医药连锁有限责任公司成立于2004年10月19日，主要经营范围为中成药、化学药制剂、抗生素制剂、生物制品、生化...</span><script type="text/html" id="company_base_info_detail">
                      保定市保北医药连锁有限责任公司成立于2004年10月19日，主要经营范围为中成药、化学药制剂、抗生素制剂、生物制品、生化药品、中药饮片零售连锁（药品经营许可证期限至2019年8月25日）等。
                    </script><span class="c9 point hover_underline" onclick="companyDetail()">详情</span><span class="ml10 c9 hover_underline point" onclick="claimPopGate(2337540891)">编辑</span></div></div></div></div>
'''

