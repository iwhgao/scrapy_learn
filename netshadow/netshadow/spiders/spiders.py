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

import re
from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from netshadow.items import NetshadowItem
from datetime import date, timedelta


class NetshadowSpider(CrawlSpider):

    name = "netshadow"
    allowed_domains = ["news.qq.com",
                       "tech.qq.com",
                       "finance.qq.com",
                       "mil.qq.com",
                       "sports.qq.com",
                       "edu.qq.com",
                       "ent.qq.com",
                       "health.qq.com",
                       "auto.qq.com"]

    start_urls = [
        "http://news.qq.com/",
        "http://tech.qq.com/",
        "http://finance.qq.com/",
        "http://mil.qq.com/",
        "http://sports.qq.com/",
        "http://edu.qq.com",
        "http://ent.qq.com/",
        "http://health.qq.com",
        "http://auto.qq.com/"
    ]

    today = str(date.today()).replace('-', '')

    rules = (
        Rule(LinkExtractor(allow=('a/%s/\d+\.htm' % today,)), callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):
        for sel in response.xpath('//div[@id="C-Main-Article-QQ"]'):
            item = NetshadowItem()
            link = str(response.url)
            title = sel.xpath('.//div[@class="hd"]/h1/text()').extract()
            content = sel.xpath('.//div[@id="Cnt-Main-Article-QQ"]/p/text()').extract()

            m = re.findall(r'://(www)?\.?(.*?)\.qq\.com', link)

            if m and m[0][1] != '':
                item['content'] = " ".join([n.encode('utf-8') for n in content])
                item['title'] = " ".join([n.encode('utf-8') for n in title])
                item['link'] = link.encode('utf-8')
                item['date'] = self.today
                item['field'] = m[0][1]
                if item['content'].strip() != '':
                    yield item
