import os
import geopandas as gpd
# import mdutils
from file_paths import GEOL_PATH, SCRAPE_OUTPUT_PATH
import urllib

from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.settings import Settings
from scholar_crawler import ScholarSpider


def make_urls():
    geomap = gpd.read_file(GEOL_PATH, layer="ATA_sources_poly")
    published = geomap[geomap["PUBTYPE"].isin(["Published paper", "Published map"])]

    urls = []
    # for i in range(published.shape[0]):
    for i in range(2):
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

    configure_logging({'LOG_FORMAT': '%(Levelname)s: %(Message)s'})
    process = CrawlerProcess(process_settings)

    process.crawl(ScholarSpider, urls=urls)
    process.start()


if __name__ == "__main__":
    main()
