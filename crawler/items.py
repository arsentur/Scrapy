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


class ModelItem(scrapy.Item):
    url = scrapy.Field()
    modification = scrapy.Field()
    modification_href = scrapy.Field()
    code = scrapy.Field()
    type_engine = scrapy.Field()
    model_engine = scrapy.Field()
    v_engine = scrapy.Field()
    power = scrapy.Field()
    date = scrapy.Field()


class ModelItemLoader(ItemLoader):
    url_out = TakeFirst()
    modification_in = Join()
    modification_out = TakeFirst()
    modification_href_in = Join()
    modification_href_out = TakeFirst()
    code_in = Join()
    code_out = TakeFirst()
    type_engine_in = Join()
    type_engine_out = TakeFirst()
    model_engine_in = Join()
    model_engine_out = TakeFirst()
    v_engine_in = Join()
    v_engine_out = TakeFirst()
    power_in = Join()
    power_out = TakeFirst()
    date_in = Join()
    date_out = TakeFirst()
