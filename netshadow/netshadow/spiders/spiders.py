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

from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from netshadow.items import NetshadowItem
from datetime import date, timedelta


class NetshadowSpider(CrawlSpider):

    name = "netshadow"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://news.qq.com/",
    ]

    yesterday_date = str(date.today() + timedelta(days=-1))

    rules = (
        Rule(LinkExtractor(allow=('a/%s/\d+\.htm$' % yesterday_date,)), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = NetshadowItem()
        sel = Selector(response)
        link = str(response.url)
        title = sel.xpath('//div[@class="hd"]/h1/text()').extract()
        content = sel.xpath('//div[@id="Cnt-Main-Article-QQ"]/p/text()').extract()

        item['content'] = [n.encode('utf-8') for n in content]
        item['title'] = [n.encode('utf-8') for n in title]
        item['link'] = link.encode('utf-8')
        yield item
