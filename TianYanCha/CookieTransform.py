#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-16 上午8:36
# @Author  : Gavin
# @Site    : 
# @File    : CookieTransform.py
# @Software: PyCharm

# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "TYCID=6eaa7e70281d11e886c4e3e6089348bd; undefined=6eaa7e70281d11e886c4e3e6089348bd; ssuid=9535358242; aliyungf_tc=AQAAAIrCKXpu/AUAjhpad/l8U0gI7K4u; csrfToken=7at1nnS0fGNQqbT0JMI1ARk8; bannerFlag=true; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTU5NzI3MCwiZXhwIjoxNTM3MTQ5MjcwfQ.ZhFj4YSsSayxN5pIaz8nfJgqey--5N17PFmFmTRZrh403bxKJtn1nsPIvOdxQaPggNawDpRb8_yZkLKLr78xyA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213693391722%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTU5NzI3MCwiZXhwIjoxNTM3MTQ5MjcwfQ.ZhFj4YSsSayxN5pIaz8nfJgqey--5N17PFmFmTRZrh403bxKJtn1nsPIvOdxQaPggNawDpRb8_yZkLKLr78xyA; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1521096752,1521442110; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1521624571; RTYCID=6f75ee2442d84840b8863557dd390349"
    trans = transCookie(cookie)
    print(trans.stringToDict())

