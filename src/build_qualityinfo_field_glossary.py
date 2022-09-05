import geopandas as gpd
import pandas as pd
import mdutils
from src.build_utils import configure_logger

import src.file_paths as fp
import src.fields

logger = configure_logger(__name__)


def build_quality_info_field_glossary(quality_info: gpd.GeoDataFrame):
    field_descr = pd.read_csv(fp.QUALINFO_FIELD_DESCR_PATH).fillna("")

    mdfile = mdutils.MdUtils(
        file_name=fp.QUALINFO_GLOSSARY_PATH, author="Samuel Elkind"
    )

    mdfile.new_header(1, title="Quality Information Field Glossary")

    for i in quality_info.columns:
        if i in src.fields.OMITTED_FIELDS:
            continue

        record = field_descr.loc[field_descr["field_name"] == i]
        if record.shape[0] == 0:
            logger.info(
                f"field {i} has no metadata. Add an entry to {fp.QUALINFO_FIELD_DESCR_PATH}"
            )
            continue

        mdfile.new_header(2, i)

        for j, k in [
            ("field_description", "Field Description"),
            ("value_formatting", "Formatting of Values"),
        ]:
            if not record[j].iloc[0]:
                continue
            mdfile.new_line(f"{k}:", bold_italics_code="b")
            mdfile.new_line("")
            mdfile.new_line(text=record[j].iloc[0])
            mdfile.new_line("")

    mdfile.create_md_file()


def main():
    quality_info = gpd.read_file(
        fp.GEOL_PATH, layer="ATA_GeoMAP_qualityinformation"
    ).fillna("")
    build_quality_info_field_glossary(quality_info)


if __name__ == "__main__":
    main()
