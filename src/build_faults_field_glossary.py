import geopandas as gpd
import pandas as pd
import mdutils

# Globals
import src.file_paths as fp
import src.fields
from src.build_utils import configure_logger, create_output, format_output

logger = configure_logger(__name__)


def build_faults_field_glossary(faults: gpd.GeoDataFrame):
    field_descr = pd.read_csv(fp.FAULTS_FIELD_DESCR_PATH).fillna("")

    mdfile = mdutils.MdUtils(file_name=fp.FAULTS_GLOSSARY_PATH, author="Samuel Elkind")

    mdfile.new_header(1, title="Faults Field Glossary")

    for i in faults.columns:
        if i in src.fields.OMITTED_FIELDS:
            continue

        record = field_descr.loc[field_descr["field_name"] == i]
        if record.shape[0] == 0:
            logger.info(
                f"field {i} has no metadata. Add an entry to {fp.FAULTS_FIELD_DESCR_PATH}"
            )
            continue
        output = create_output(record, i)

        mdfile.new_header(2, i)

        for j in output:
            if not output[j] or j == "Field Values":
                continue
            output[j] = format_output(j, output[j], i)
            mdfile.new_line(f"{j}:", bold_italics_code="b")
            mdfile.new_line("")
            mdfile.new_line(text=output[j])
            mdfile.new_line("")

    mdfile.create_md_file()


def main():
    faults = gpd.read_file(
        fp.GEOL_PATH, layer="ATA_faults", ignore_fields=["CAPTDATE"]
    ).fillna("")
    build_faults_field_glossary(faults)


if __name__ == "__main__":
    main()
