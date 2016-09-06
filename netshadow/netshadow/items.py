# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NetshadowItem(scrapy.Item):
    """Item类"""

    # 文章的标题
    title = scrapy.Field()

    # 文章的链接
    link = scrapy.Field()

    # 文章的内容
    content = scrapy.Field()
