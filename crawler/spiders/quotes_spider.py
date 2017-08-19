from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.selector import Selector
from crawler.items import ExistItemLoader, ExistItem


class ExistSpider(CrawlSpider):
    name = 'exist_spider'

    allowed_domains = ['exist.ua']
    start_urls = ['https://exist.ua/cat/TecDoc/']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=[
                    '//div[@class="top-r"]'
                ],
                allow=r'https://exist.ua/cat/TecDoc/Cars/\w+$'
            ), callback='parse_models'
        ),
    )

    def parse_models(self, response):
        selector = Selector(response)
        l = ExistItemLoader(ExistItem(), selector)
        l.add_value('url', response.url)
        l.add_xpath('models_href', '//div[@class="car-info__car-name"]//a/@href')

        return l.load_item()
