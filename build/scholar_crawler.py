import scrapy


class ScholarSpider(scrapy.Spider):
    name = "scholarspider"

    def start_requests(self):
        for i in self.urls:
            yield scrapy.Request(url=i, callback=self.parse_search_results)

    def parse_search_results(self, response):
        citation_link = response.xpath("//div[@class='gs_r gs_or gs_scl']/@data-cid").get()
        return citation_link
