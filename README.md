# scrapy 爬虫框架学习

## 环境要求

* python 3
* scrapy 1.7

## 开启代理

项目中使用的是免费代理，代理工具用的是@Gavin写的 proxy_list 项目。[项目地址](https://github.com/gavin66/proxy_list)

```python
# settings.py 中启用
SPIDER_MIDDLEWARES = {
    'liangzilinSpider.middlewares.RandomProxyMiddleware': 100
}

DOWNLOADER_MIDDLEWARES = {
    'liangzilinSpider.middlewares.RandomProxyMiddleware': 100
}
```
