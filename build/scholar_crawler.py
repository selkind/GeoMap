import scrapy


class ScholarSpider(scrapy.Spider):
    name = "scholarspider"

    def start_requests(self):
        for i in self.urls:
            yield scrapy.Request(url=i, callback=self.parse_search_results)

    def parse_search_results(self, response):
        cite_id = response.xpath("//div[@class='gs_r gs_or gs_scl']/@data-cid").get()
        citation_url = f"https://scholar.google.com/scholar?q=info:{cite_id}"\
                       ":scholar.google.com/&output=cite&scirp=0&hl=en"
        return scrapy.Request(url=citation_url, callback=self.parse_citation_results)

    def parse_citation_results(self, response):
        plain_mla = response.xpath("//div/table/tr/th[text()='MLA']/parent::tr/td/div/text()").getall()
        italics_mla = response.xpath("//div/table/tr/th[text()='MLA']/parent::tr/td/div/i/text()").get()
        mla = Citation(form="MLA", plain_text=plain_mla, italics=italics_mla)
        bibtex = response.xpath("//div/a[text()='BibTeX']/@href").get()
        print(bibtex)
        return CitationSet(mla=mla, bibtex=bibtex)


class Citation(scrapy.Item):
    form = scrapy.Field()
    plain_text = scrapy.Field()
    italics = scrapy.Field()


class CitationSet(scrapy.Item):
    mla = scrapy.Field()
    bibtex = scrapy.Field()
