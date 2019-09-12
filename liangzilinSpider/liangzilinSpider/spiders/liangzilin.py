# -*- coding: utf-8 -*-
import scrapy
from liangzilinSpider.items import LiangzilinspiderItem
import os


class LiangzilinSpider(scrapy.Spider):
    name = 'liangzilin'
    allowed_domains = ['www.demo.me']
    start_urls = ['http://www.demo.me/']

    def parse(self, response):
        list = response.xpath('//*[@id="posts"]/article')
        for item in list:
            title = item.xpath('div/header/h1/a/text()').get().strip()
            link = item.xpath('div/header/h1/a/@href').get()
            yield scrapy.Request(url=response.urljoin(link), callback=self.parseItem, meta={"title": title})

        # 下一页
        next_page = response.xpath('//*[@id="content"]/nav/a[@class="extend next"]/@href').get()
        if next_page is not None:
            yield scrapy.Request(url=response.urljoin(next_page))

    def parseItem(self, response):
        time = response.xpath('//span[@class="post-time"]/time/text()').get().strip()
        category = response.xpath('//span[@class="post-category"]/span[@itemprop="about"]//span/text()').get().strip()
        content = response.xpath('//*[@id="posts"]/article/div/div[1]').get().strip()
        title = response.meta.get('title', '')

        # 打开文件
        # self.save_file(title + ".html", content)
        # os.system("start " + title.replace(" ", "\ ") + ".html")

        article = LiangzilinspiderItem()
        article['title'] = title
        article['category'] = category
        article['time'] = time
        article['content'] = content

        yield article

    def save_file(self, file_name, context):
        fh = open(file_name, 'wb')
        fh.write(context.encode(encoding="utf-8"))
        fh.close()
        pass