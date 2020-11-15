import scrapy


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
