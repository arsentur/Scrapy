from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.selector import Selector
from crawler.items import ExistItemLoader, ExistItem, ModelItem, ModelItemLoader
import json


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
        l.add_xpath('brand', '//div[@class="content-page content-page--banner"]//h1/text()')
        l.add_xpath('model', '//div[@id="models"]/div[@class="cell2"]//a/@href')

        return l.load_item()


data = dict()

urls = []

with open('exist.json') as data_file:
    for line in data_file:
        js = json.loads(line)

        data['brand'] = js['brand'].replace('Автозапчасти для ', '')
        data['url'] = js['url']

        models = js['model'].split(' ')
        data['model'] = []

        for model in models:
            # print('https://exist.ua' + model)
            data['model'].append('https://exist.ua' + model)
            urls.append('https://exist.ua' + model)


class ModelCarSpider(CrawlSpider):
    name = 'exist_model_spider'

    allowed_domains = ['exist.ua']
    start_urls = urls

    def parse(self, response):
        for quote in response.css('table.tbl'):
            yield {
                'url': response.url,
                'modification': quote.xpath('//tr[not(@class)]/td/a/text()').extract(),
                'modification_href': quote.xpath('//tr[not(@class)]/td/a/@href').extract(),
                'code': quote.xpath('//tr[not(@class)]/td[2]/text()').extract(),
                'type_engine': quote.xpath('//tr[not(@class)]/td[3]/text()').extract(),
                'model_engine': quote.xpath('//tr[not(@class)]/td[4]/text()').extract(),
                'v_engine': quote.xpath('//tr[not(@class)]/td[5]/text()').extract(),
                'power': quote.xpath('//tr[not(@class)]/td[6]/text()').extract(),
                'date': quote.xpath('//tr[not(@class)]/td[7]/b/text()').extract(),
            }

    # rules = (
    #     Rule(
    #         LinkExtractor(
    #             restrict_css=['table.tbl'],
    #             allow=r'https://exist.ua/cat/TecDoc/Cars/\w+/\d+/$'
    #         ), callback='parse_item'
    #     ),
    # )
    #
    # def parse_item(self, response):
    #     selector = Selector(response)
    #     l = ModelItemLoader(ModelItem(), selector)
    #     l.add_value('url', response.url)
    #     l.add_xpath('modification', '//tr[not(@class)]/td/a/text()')
    #     l.add_xpath('modification_href', '//tr[not(@class)]/td/a/@href')
    #     l.add_xpath('code', '//tr[not(@class)]/td[2]/text()')
    #     l.add_xpath('type_engine', '//tr[not(@class)]/td[3]/text()')
    #     l.add_xpath('model_engine', '//tr[not(@class)]/td[4]/text()')
    #     l.add_xpath('v_engine', '//tr[not(@class)]/td[5]/text()')
    #     l.add_xpath('power', '//tr[not(@class)]/td[6]/text()')
    #     l.add_xpath('date', '//tr[not(@class)]/td[7]/b/text()')

        # return l.load_item()
