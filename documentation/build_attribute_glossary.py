import geopandas as gpd
import pandas as pd
import file_paths as fp
import fields

import mdutils


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
        source = record['source_of_vals'].iloc[0]
        formatting = record['value_formatting'].iloc[0]
        metadata_link = record['field_metadata_link'].iloc[0]
        field_vals = record['Field Values'].iloc[0]
        restrictions = record['Field value restrictions'].iloc[0]
        output = {"Source of Values": source,
                  "Value Format": formatting,
                  "Metadata Link": metadata_link,
                  "Field Values": field_vals,
                  "Field Value Restrictions": restrictions}

        mdfile.new_header(1, i)
        for j in output:
            if output[j] == "blank":
                output[j] = "None"

            if j in ["Metadata Link", "Field Values", "Field Value Restrictions"]:
                output[j] == mdfile.new_inline_link(output[j], output[j])
            mdfile.new_header(2, f"{j}: {output[j]}")

        mdfile.new_header(2, "Descriptive Statistics:")
        stats = {}
        stats["Unique Values"] = len(value_counts)
        if len(value_counts) > 0:
            stats["Most frequently occurring value"] = value_counts.index[0]
            stats["Number of values with a single occurrence"] = len([k for k in value_counts if k == 1])

        mdfile.new_list([f"{k}: {stats[k]}" for k in stats])

    mdfile.new_table_of_contents("Table of Contents", depth=3)
    mdfile.create_md_file()


if __name__ == "__main__":
    main()
