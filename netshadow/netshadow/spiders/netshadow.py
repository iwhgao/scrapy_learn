#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
@version: v1.0.0
@author: deangao 
@license: Apache Licence 
@contact: gaowenhui2012@gmail.com
@site: www.iwhgao.com
@file: netshadow.py
@time: 2016/9/2 21:21
"""

import scrapy
from netshadow.items import NetshadowItem


class NetshadowSpider(scrapy.spiders.Spider):
    def __init__(self):
        pass

    name = "netshadow"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://www.qq.com/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = NetshadowItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
