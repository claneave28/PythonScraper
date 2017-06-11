# -*- coding: utf-8 -*-

BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'

# maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32
# timeout for processing DNS queries in seconds(float) (default: 60)
DNS_TIMEOUT = 10
# time(sec) that the downloader will wait before timing out
DOWNLOAD_TIMEOUT = 24

# use telnet console
TELNETCONSOLE_ENABLED = False

# to avoid getting loss data response set to false
DOWNLOAD_FAIL_ON_DATALOSS = False

# delay for requests for the same website (default: 0)
# DOWNLOAD_DELAY = 3
# download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 2

# maximum number of times to retry
RETRY_TIMES = 2
# HTTP response codes to retry
RETRY_HTTP_CODES = [500, 502, 503, 504]

# disable cookies
COOKIES_ENABLED = False

# TOR SETTINGS
HTTP_PROXY = 'http://127.0.0.1:8118'
AUTH_PASSWORD = 'scr@pethis!'
CONTROL_PORT = 9051
# number of HTTTP request before the IP change
# delete or set to None if you don't want to use it
MAX_REQ_PER_IP = 1000

# downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'amazon.middlewares.user_agent.RandomUserAgentMiddleware': 400,
    'amazon.middlewares.proxy.HttpProxyMiddleware': 410,
    # 'amazon.middlewares.proxy.TorProxyMiddleware': 410
}

ITEM_PIPELINES = {
    'amazon.pipelines.AmazonPipeline': 300
}