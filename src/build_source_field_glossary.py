import geopandas as gpd
from build_utils import get_layer_names, build_field_glossary

import file_paths as fp


def build_source_field_glossary(sources: gpd.GeoDataFrame):
    build_field_glossary(
        sources, "Sources", fp.SOURCE_FIELD_DESCR_PATH, fp.SOURCE_GLOSSARY_PATH
    )


def main():
    layers = get_layer_names()
    sources = gpd.read_file(fp.GEOL_PATH, layer=layers["sources_layer"]).fillna("")
    build_source_field_glossary(sources)


if __name__ == "__main__":
    main()
