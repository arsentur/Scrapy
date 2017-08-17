from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.selector import Selector
import scrapy
from crawler.items import ExistItemLoader, ExistItem


class ExistSpider(CrawlSpider):
    name = 'exist_spider'

    allowed_domains = ['exist.ua']
    start_urls = ['https://exist.ua']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=[
                    '//div[contains(@id, "carUnChecked")]'
                ],

                allow=r'https://exist.ua/cat/TecDoc/Cars/\w+$'
            ), callback='parse_item'
        ),
    )

    def parse_item(self, response):
        selector = Selector(response)
        l = ExistItemLoader(ExistItem(), selector)
        l.add_value('url', response.url)
        l.add_xpath('brand', '//div[@class="content-page content-page--banner"]//h1')
        l.add_xpath('model', '//div[@id="models"]/div[@class="cell2"]//a')

        return l.load_item()
