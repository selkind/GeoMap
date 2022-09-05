import geopandas as gpd
import pandas as pd
import mdutils
from src.build_utils import configure_logger

# Globals
import src.file_paths as fp
import src.fields


logger = configure_logger(__name__)


def build_source_field_glossary(sources: gpd.GeoDataFrame):
    field_descr = pd.read_csv(fp.SOURCE_FIELD_DESCR_PATH).fillna("")

    mdfile = mdutils.MdUtils(file_name=fp.SOURCE_GLOSSARY_PATH, author="Samuel Elkind")

    mdfile.new_header(1, title="Sources Field Glossary")

    for i in sources.columns:
        if i in src.fields.OMITTED_FIELDS:
            continue

        record = field_descr.loc[field_descr["field_name"] == i]

        mdfile.new_header(2, i)

        for j in [
            ("field_description", "Field Description"),
            ("value_formatting", "Formatting of Values"),
        ]:
            mdfile.new_line(f"{j[1]}:", bold_italics_code="b")
            mdfile.new_line("")
            mdfile.new_line(text=record[j[0]].iloc[0])
            mdfile.new_line("")

    mdfile.create_md_file()


def main():
    sources = gpd.read_file(fp.GEOL_PATH, layer="ATA_sources_poly").fillna("")
    build_source_field_glossary(sources)


if __name__ == "__main__":
    main()
