from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class MenuSpider(scrapy.Spider):
    name = "Menu Spider"

    def start_requests(self):
        yield scrapy.Request(url="https://www.sweetcowicecream.com/platt/", callback=self.parse)

    def parse(self, response):
        flavors = []
        for flavor in response.xpath("//div[@class='flavor-wrap']//h3[@class='vertalign']/text()").getall():
            flavors.append(flavor.strip().lower())
        print(flavors)
        return flavors


def run():
    configure_logging({'LOG_FORMAT': '%(Levelname)s: %(Message)s'})
    runner = CrawlerRunner()

    d = runner.crawl(MenuSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
