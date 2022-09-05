import os

import geopandas as gpd
from build_bibliography import build_bibliography
from build_faults_field_glossary import build_faults_field_glossary
from build_field_value_files import build_field_values
from build_field_glossary import build_field_glossary
from build_qualityinfo_field_glossary import build_quality_info_field_glossary
from build_source_field_glossary import build_source_field_glossary
from build_utils import configure_logger, download_data
import file_paths as fp
import fiona

logger = configure_logger(__name__)


layer_name_modifier = "GeoMAP_"


def main():
    os.system("make clean")
    download_data()

    if any([layer_name_modifier in i for i in fiona.listlayers(fp.GEOL_PATH)]):
        geol_layer = "ATA_GeoMAP_geological_units"
        sources_layer = "ATA_GeoMAP_sources"
        faults_layer = "ATA_GeoMAP_faults"
        quality_info_layer = "ATA_GeoMAP_quality"
    else:
        geol_layer = "ATA_geological_units"
        sources_layer = "ATA_sources_poly"
        faults_layer = "ATA_faults"
        quality_info_layer = "ATA_GeoMAP_qualityinformation"

    geol_units = gpd.read_file(
        fp.GEOL_PATH, layer=geol_layer, ignore_fields=["CAPTDATE"]
    ).fillna("")
    sources = gpd.read_file(fp.GEOL_PATH, layer=sources_layer)
    faults = gpd.read_file(fp.GEOL_PATH, layer=faults_layer).fillna("")
    quality_info = gpd.read_file(fp.GEOL_PATH, layer=quality_info_layer).fillna("")

    build_bibliography(sources)
    build_faults_field_glossary(faults)

    # order matters here, field_glossary depends on field value file existence
    build_field_values(geol_units)
    build_field_glossary(geol_units)

    build_quality_info_field_glossary(quality_info)
    build_source_field_glossary(sources)

    os.system("make html")
    os.system("make latexpdf")


if __name__ == "__main__":
    main()
