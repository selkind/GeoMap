import os
import geopandas as gpd
import pandas as pd
import file_paths as fp
import fields

import mdutils


def create_output(record, field_name):
    source = record['source_of_vals'].iloc[0]
    formatting = record['value_formatting'].iloc[0]
    metadata_link = record['field_metadata_link'].iloc[0]
    # field_vals = record['Field Values'].iloc[0]
    restrictions = record['Field value restrictions'].iloc[0]
    return {"Source of Values": source,
            "Value Format": formatting,
            "Metadata Link": metadata_link,
            "Field Values": f"{os.path.join(os.path.basename(fp.FIELD_VALS_DIR), field_name)}_values.md",
            "Field Value Restrictions": restrictions}


def format_output(descr_header, value, field_name):
    # this is a sloppy handling of blanks because Pandas reads "None" as nan. There's probably a way to change this
    if value == "blank":
        value == "None"

    elif descr_header in ["Metadata Link", "Field Value Restrictions"] and "http" in value:
        value = mdutils.tools.Link.Inline.new_link(value, value)
    elif descr_header == "Field Values":
        value = mdutils.tools.Link.Inline.new_link(
                                                link=os.path.join("field_values", f"{field_name}_values.md"),
                                                text="List of Values")
    return value


def create_stats(value_counts):
    stats = {}
    stats["Unique Values"] = len(value_counts)
    if len(value_counts) > 0:
        stats["Most frequently occurring value"] = value_counts.index[0]
        stats["Number of values with a single occurrence"] = len([k for k in value_counts if k == 1])
    return stats


def main():
    geomap = gpd.read_file(fp.GEOL_PATH)
    field_descr = pd.read_csv(fp.FIELD_DESCR_PATH)

    mdfile = mdutils.MdUtils(file_name=fp.GLOSSARY_PATH, title="Field Glossary", author="SCAR GeoMAP Project")

    for i in geomap.columns:
        if i in fields.OMITTED_FIELDS:
            continue
        try:
            value_counts = geomap[i].value_counts()
        except AttributeError:
            continue

        condition = field_descr['field_name'] == i
        record = field_descr.loc[condition]
        output = create_output(record, i)

        mdfile.new_header(1, i)
        for j in output:
            output[j] = format_output(j, output[j], i)
            mdfile.new_header(2, f"{j}:")
            mdfile.new_paragraph(text=output[j])

        mdfile.new_header(2, "Descriptive Statistics:")

        stats = create_stats(value_counts)

        mdfile.new_list([f"{k}: {stats[k]}" for k in stats])

    mdfile.create_md_file()


if __name__ == "__main__":
    main()
