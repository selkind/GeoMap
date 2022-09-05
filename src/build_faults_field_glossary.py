import geopandas as gpd

import file_paths as fp
from build_utils import (
    configure_logger,
    get_layer_names,
    build_field_glossary,
)

logger = configure_logger(__name__)


def build_faults_field_glossary(faults: gpd.GeoDataFrame):
    build_field_glossary(
        faults, "Faults", fp.FAULTS_FIELD_DESCR_PATH, fp.FAULTS_GLOSSARY_PATH
    )


def main():
    layers = get_layer_names()
    faults = gpd.read_file(fp.GEOL_PATH, layer=layers["faults_layer"]).fillna("")
    build_faults_field_glossary(faults)


if __name__ == "__main__":
    main()
