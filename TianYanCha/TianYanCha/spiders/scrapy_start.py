#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-19 下午2:55
# @Author  : Gavin
# @Site    : 
# @File    : scrapy_start.py
# @Software: PyCharm


from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    execute(['scrapy','crawl','Tianyan'])

if __name__ == '__main__':
    main()