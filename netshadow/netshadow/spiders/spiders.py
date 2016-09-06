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

from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import CrawlSpider, Rule
from scrapy.selector import Selector
from netshadow.items import NetshadowItem


class NetshadowSpider(CrawlSpider):
    def __init__(self, *a, **kw):
        super(NetshadowSpider, self).__init__(*a, **kw)

    name = "netshadow"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://www.qq.com/",
    ]

    rules = [
        Rule(SgmlLinkExtractor(allow=('a/[0-9]+/[0-9]+\.htm'),
                               restrict_xpaths=('//div[@class="C-Main-Article-QQ"]')),
             callback='parse_item',
             follow=True)
    ]

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

