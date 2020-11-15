import os
import geopandas as gpd
import mdutils
from file_paths import GEOL_PATH, SITE_DIR, BIB_PATH
import urllib


def main():
    geomap = gpd.read_file(GEOL_PATH, layer="ATA_sources_poly")

    for i in range(10):
        query = f"{geomap['TITLE'].iloc[i]} {geomap['AUTHORS'].iloc[i]} {int(geomap['YEAR'].iloc[i])}"
        components = ("https", "scholar.google.com", "/scholar", "", f"q={query}", "")
        url = urllib.parse.urlunparse(components)
        print(url, geomap["PUBTYPE"].iloc[i])


if __name__ == "__main__":
    main()