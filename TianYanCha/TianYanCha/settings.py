# -*- coding: utf-8 -*-

# Scrapy settings for TianYanCha project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'TianYanCha'

SPIDER_MODULES = ['TianYanCha.spiders']
NEWSPIDER_MODULE = 'TianYanCha.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'TianYanCha (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#   'Connection': 'keep - alive',  # 保持链接状态
#   'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
#   'Cookie': "TYCID=6eaa7e70281d11e886c4e3e6089348bd; undefined=6eaa7e70281d11e886c4e3e6089348bd; ssuid=9535358242; aliyungf_tc=AQAAAIrCKXpu/AUAjhpad/l8U0gI7K4u; csrfToken=7at1nnS0fGNQqbT0JMI1ARk8; RTYCID=57573a12cf2d430a8d369dba04dbf5e9; bannerFlag=true; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTQ0NTgyOCwiZXhwIjoxNTM2OTk3ODI4fQ.GXErnVAL3h0Hx8A5vw3NpQZSqTCcQkcctvZAxXSCfwpc6fDpgPqlBDYILZp-csZS6QpjYRuQPseVndJ9Lil4nw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213693391722%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTQ0NTgyOCwiZXhwIjoxNTM2OTk3ODI4fQ.GXErnVAL3h0Hx8A5vw3NpQZSqTCcQkcctvZAxXSCfwpc6fDpgPqlBDYILZp-csZS6QpjYRuQPseVndJ9Lil4nw; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1521096752,1521442110; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1521446995"
# }

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en',
    'Tyc-From': 'normal',
    'CheckError': 'check',
    'Connection': 'keep-alive',
    'Cookie': 'TYCID=6eaa7e70281d11e886c4e3e6089348bd; undefined=6eaa7e70281d11e886c4e3e6089348bd; ssuid=9535358242; aliyungf_tc=AQAAAIrCKXpu/AUAjhpad/l8U0gI7K4u; csrfToken=7at1nnS0fGNQqbT0JMI1ARk8; RTYCID=57573a12cf2d430a8d369dba04dbf5e9; bannerFlag=true; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTQ0NTgyOCwiZXhwIjoxNTM2OTk3ODI4fQ.GXErnVAL3h0Hx8A5vw3NpQZSqTCcQkcctvZAxXSCfwpc6fDpgPqlBDYILZp-csZS6QpjYRuQPseVndJ9Lil4nw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213693391722%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTQ0NTgyOCwiZXhwIjoxNTM2OTk3ODI4fQ.GXErnVAL3h0Hx8A5vw3NpQZSqTCcQkcctvZAxXSCfwpc6fDpgPqlBDYILZp-csZS6QpjYRuQPseVndJ9Lil4nw; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1521096752,1521442110; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1521446995'
}


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'TianYanCha.middlewares.TianyanchaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'TianYanCha.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# DOWNLOADER_MIDDLEWARES = { 'TianYanCha.middlewares.ProxyMiddleWare':400 }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'TianYanCha.pipelines.TianyanchaPipeline': 300,
   'TianYanCha.pipelines.MysqlPipeline':400
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
