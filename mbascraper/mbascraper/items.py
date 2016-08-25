# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MbascraperItem(scrapy.Item):
    # define the fields for your item here like:
    bothy_id = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    gridref = scrapy.Field()
    region = scrapy.Field()
    description = scrapy.Field()
    images = scrapy.Field()
    pass
