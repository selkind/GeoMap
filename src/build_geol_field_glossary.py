import geopandas as gpd

import file_paths as fp
from build_utils import configure_logger, build_field_glossary, get_layer_names


logger = configure_logger(__name__)


def build_geol_field_glossary(geol_units: gpd.GeoDataFrame) -> None:
    build_field_glossary(
        geol_units, "Geological Units", fp.GEOL_FIELD_DESCR_PATH, fp.GEOL_GLOSSARY_PATH
    )


def main():
    layers = get_layer_names()
    geol_units = gpd.read_file(fp.GEOL_PATH, layer=layers["geol_layer"]).fillna("")
    build_geol_field_glossary(geol_units)


if __name__ == "__main__":
    main()
