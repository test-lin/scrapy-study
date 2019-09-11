# -*- coding: utf-8 -*-

# Scrapy settings for liangzilinSpider project
# liangzilinSpider 项目Scrapy设置
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
# 为简单起见，此文件仅包含被认为重要或常用的设置。您可以在参考文档中找到更多设置：
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'liangzilinSpider'

SPIDER_MODULES = ['liangzilinSpider.spiders']
NEWSPIDER_MODULE = 'liangzilinSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 通过在用户代理上标识你自己（和你的网站）负责任地爬行
#USER_AGENT = 'liangzilinSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 服从 robots.txt 规则
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 配置scrapy执行的最大并发请求数（默认值：16）
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 为同一网站的请求配置延迟（默认值：0）
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 下载延迟设置将仅支持以下选项之一：
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 禁用 cookies (默认开启)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 禁用telnet控制台（默认启用）
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 重写默认请求头
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# 启用或禁用爬虫中间件
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'liangzilinSpider.middlewares.LiangzilinspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# 启用或禁用下载中间件
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'liangzilinSpider.middlewares.LiangzilinspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# 启用或禁用扩展
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# 配置管道项
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'liangzilinSpider.pipelines.LiangzilinspiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# 启用并配置自动限速扩展（默认禁用）
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 在高延迟情况下设置的最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# scrapy应并行发送到每个远程服务器的平均请求数
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 启用显示收到的每个响应的限制状态：
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# 启用和配置http缓存（默认禁用）
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
