import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join


class ExistItem(scrapy.Item):
    url = scrapy.Field()
    models_href = scrapy.Field()


class ExistItemLoader(ItemLoader):
    url_out = TakeFirst()
    models_href_in = Join()
    models_href_out = TakeFirst()
