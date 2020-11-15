# import os
import geopandas as gpd
# import mdutils
from file_paths import GEOL_PATH, SITE_DIR, BIB_PATH
import urllib

from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scholar_crawler import ScholarSpider


def make_urls():
    geomap = gpd.read_file(GEOL_PATH, layer="ATA_sources_poly")
    published = geomap[geomap["PUBTYPE"].isin(["Published paper", "Published map"])]

    urls = []
    for i in range(published.shape[0] - 1):
        if geomap["PUBTYPE"].iloc[i] in ["Thesis", "GIS dataset", "Unknown", "Unpublished"]:
            continue
        query = f"{geomap['TITLE'].iloc[i]} {geomap['AUTHORS'].iloc[i]} {int(geomap['YEAR'].iloc[i])}"
        components = ("https", "scholar.google.com", "/scholar", "", f"q={query}", "")
        urls.append(urllib.parse.urlunparse(components))
        break
    return urls


def main():
    urls = make_urls()
    print(urls)
    configure_logging({'LOG_FORMAT': '%(Levelname)s: %(Message)s'})
    process = CrawlerProcess(get_project_settings())

    process.crawl(ScholarSpider, urls=urls)
    process.start()


if __name__ == "__main__":
    main()
