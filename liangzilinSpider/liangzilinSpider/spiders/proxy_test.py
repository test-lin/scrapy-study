# -*- coding: utf-8 -*-
import scrapy


class ProxyTestSpider(scrapy.Spider):
    name = 'proxy_test'
    allowed_domains = ['http://log.liangzilin.club']
    start_urls = ['https://log.liangzilin.club/api/login/spider']

    def parse(self, response):
        print(response.text)
