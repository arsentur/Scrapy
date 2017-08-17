# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join


class ExistItem(scrapy.Item):
    url = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()


class ExistItemLoader(ItemLoader):
    url_out = TakeFirst()
    brand_out = TakeFirst()
    model_in = Join()
    model_out = TakeFirst()
