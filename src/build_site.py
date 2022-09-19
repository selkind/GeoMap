import os

import geopandas as gpd
import pandas as pd

from build_bibliography import build_bibliography
from build_faults_field_glossary import build_faults_field_glossary
from build_field_value_files import build_field_values
from build_geol_field_glossary import build_geol_field_glossary
from build_qualityinfo_field_glossary import build_quality_info_field_glossary
from build_source_field_glossary import build_source_field_glossary
from build_utils import configure_logger, download_data, get_layer_names
from build_restricted_lists import build_restricted_lists
import file_paths as fp

logger = configure_logger(__name__)


def main():
    os.system("make clean")
    download_data()

    layers = get_layer_names()

    # geol_units = gpd.read_file(fp.GEOL_PATH, layer=layers["geol_layer"], ignore_geometry=True).fillna("")
    geol_units = gpd.read_file(os.path.join(fp.DATA_DIR, "date_edited_geol.shp"), ignore_geometry=True)
    sources = gpd.read_file(fp.GEOL_PATH, layer=layers["sources_layer"]).fillna("")
    faults = gpd.read_file(fp.GEOL_PATH, layer=layers["faults_layer"]).fillna("")
    quality_info = gpd.read_file(
        fp.GEOL_PATH, layer=layers["quality_info_layer"], date_parser=lambda x: pd.datetime.strptime(x, "%Y/%m/%d")
    ).fillna("")

    build_restricted_lists()

    build_bibliography(sources)
    build_faults_field_glossary(faults)

    # order matters here, field_glossary depends on field value file existence
    build_field_values(geol_units)
    build_geol_field_glossary(geol_units)

    build_quality_info_field_glossary(quality_info)
    build_source_field_glossary(sources)

    os.system("make html")
    os.system("make latexpdf")


if __name__ == "__main__":
    main()
