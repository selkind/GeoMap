# import os
import geopandas as gpd
# import mdutils
from file_paths import GEOL_PATH
import urllib


def make_urls():
    geomap = gpd.read_file(GEOL_PATH, layer="ATA_sources_poly")
    published = geomap[geomap["PUBTYPE"].isin(["Published paper", "Published map"])]

    urls = []
    for i in range(published.shape[0]):
        if geomap["PUBTYPE"].iloc[i] in ["Thesis", "GIS dataset", "Unknown", "Unpublished"]:
            continue
        query = f"{geomap['TITLE'].iloc[i]} {geomap['AUTHORS'].iloc[i]} {int(geomap['YEAR'].iloc[i])}"
        components = ("https", "scholar.google.com", "/scholar", "", f"q={query}", "")
        urls.append(urllib.parse.urlunparse(components))
    return urls


def main():
    pass


if __name__ == "__main__":
    main()
