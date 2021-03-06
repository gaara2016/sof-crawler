# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SofItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    vote = scrapy.Field()
    answer = scrapy.Field()
    view = scrapy.Field()
    asked = scrapy.Field()
    user = scrapy.Field()
