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
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://news.qq.com/",
        "http://tech.qq.com/",
        "http://finance.qq.com/",
        "http://mil.qq.com/",
        "http://sports.qq.com/",
        "http://ent.qq.com/",
        "http://health.qq.com",
        "http://auto.qq.com/"
    ]

    yesterday_date = str(date.today() + timedelta(days=-1)).replace('-', '')

    rules = (
        Rule(LinkExtractor(allow=('a/%s/\d+\.htm' % yesterday_date,)), callback='parse_item', follow=True),
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
                item['date'] = self.yesterday_date
                item['field'] = m[0][1]
                yield item
