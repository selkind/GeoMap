import geopandas as gpd
from build_utils import get_layer_names, build_field_glossary

import file_paths as fp


def build_quality_info_field_glossary(quality_info: gpd.GeoDataFrame):
    build_field_glossary(
        quality_info,
        "Quality Information",
        fp.QUALINFO_FIELD_DESCR_PATH,
        fp.QUALINFO_GLOSSARY_PATH,
    )


def main():
    layers = get_layer_names()
    quality_info = gpd.read_file(
        fp.GEOL_PATH, layer=layers["quality_info_layer"]
    ).fillna("")
    build_quality_info_field_glossary(quality_info)


if __name__ == "__main__":
    main()
