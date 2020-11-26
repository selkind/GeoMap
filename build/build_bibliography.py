# import os
import geopandas as gpd
# import mdutils
from file_paths import GEOL_PATH, SCRAPE_OUTPUT_PATH
import urllib

from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.settings import Settings, overridden_settings
from scholar_crawler import ScholarSpider


def make_urls():
    geomap = gpd.read_file(GEOL_PATH, layer="ATA_sources_poly")
    published = geomap[geomap["PUBTYPE"].isin(["Published paper", "Published map"])]

    urls = []
    # for i in range(published.shape[0]):
    for i in range(1,3):
        if geomap["PUBTYPE"].iloc[i] in ["Thesis", "GIS dataset", "Unknown", "Unpublished"]:
            continue
        query = f"{geomap['TITLE'].iloc[i]} {geomap['AUTHORS'].iloc[i]} {int(geomap['YEAR'].iloc[i])}"
        components = ("https", "scholar.google.com", "/scholar", "", f"q={query}", "")
        urls.append(urllib.parse.urlunparse(components))
    return urls


def main():
    urls = make_urls()
    print(urls)
    process_settings = Settings()
    process_settings.set("FEEDS", {SCRAPE_OUTPUT_PATH:
                                   {"format": 'json',
                                   "encoding": 'utf-8',
                                   "indent": 4}})
    process_settings.set('USER_AGENT', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9')
    process_settings.set('COOKIES_ENABLED', False)
    process_settings.set('DOWNLOAD_DELAY', 2)
    process_settings.set('DOWNLOADER_MIDDLEWARES', {'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,})
    configure_logging({'LOG_FORMAT': '%(Levelname)s: %(Message)s'})
    process = CrawlerProcess(process_settings)

    process.crawl(ScholarSpider, urls=urls)
    process.start()


if __name__ == "__main__":
    main()
