import sys
import os

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import geopandas as gpd
import pandas as pd
import mdutils

# Globals
import src.file_paths as fp
import src.fields
from src.build_utils import create_output, format_output


def create_stats(value_counts):
    """
    @param pd.Series value_counts: the value counts of the field in question

    @returns dict: the statistics to be output in markdown
    """
    stats = {}
    stats["Unique Values"] = len(value_counts)
    if len(value_counts) > 0:
        stats["Most frequently occurring value"] = value_counts.index[0]
        stats["Number of values with a single occurrence"] = len([k for k in value_counts if k == 1])
    return stats


def build_field_glossary(feature_class: gpd.GeoDataFrame, field_descr: pd.DataFrame, mdfile: mdutils.MdUtils):
    mdfile.new_header(1, title="Geological Units Field Glossary")
    for i in feature_class.columns:
        if i in src.fields.OMITTED_FIELDS:
            continue
        try:
            value_counts = feature_class[i].value_counts()
        except AttributeError:
            continue

        record = field_descr.loc[field_descr["field_name"] == i]
        output = create_output(record, i)

        mdfile.new_header(2, i)
        for j in output:
            if not output[j]:
                continue
            output[j] = format_output(j, output[j], i)
            mdfile.new_line(f"{j}:", bold_italics_code="b")
            mdfile.new_line("")
            mdfile.new_line(text=output[j])
            mdfile.new_line("")

        mdfile.new_line("More Information:", bold_italics_code="b")
        mdfile.new_line()

        stats = create_stats(value_counts)
        mdfile.new_list([f"{k}: {stats[k]}" for k in stats])

    mdfile.create_md_file()


def main():
    geol_units = gpd.read_file(fp.GEOL_PATH, layer="ATA_geological_units", ignore_fields=["CAPTDATE"]).fillna("")
    field_descr = pd.read_csv(fp.FIELD_DESCR_PATH).fillna("")
    mdfile = mdutils.MdUtils(file_name=fp.GEOL_GLOSSARY_PATH, author="Samuel Elkind")
    build_field_glossary(geol_units, field_descr, mdfile)


if __name__ == "__main__":
    main()
