import os
from itertools import chain
import geopandas as gpd
import file_paths as fp
import fields

import mdutils


def build_field_values(geol_units: gpd.GeoDataFrame):
    for i in geol_units.columns:
        if i in fields.OMITTED_FIELDS:
            continue
        column = (
            geol_units[i]
            .value_counts()
            .reset_index()
            .sort_values([i, "index"], ascending=[False, True])
            .set_index("index")
        )
        if column.shape[0] > 200:
            continue

        mdfile = mdutils.MdUtils(
            file_name=os.path.join(fp.FIELD_VALS_DIR, f"{i}_values.md"),
            title=f"Unique values of {i}",
        )

        table_header = ["Value", "Number of Occurrences"]
        # to populate a table, mdutils needs a flat list of all values divisible by m columns
        # chain.from_iterable flattens the tupled output of zip()
        table_header.extend(chain.from_iterable(zip(column.index, column[i])))

        mdfile.new_table(
            columns=2, rows=column.shape[0] + 1, text=table_header, text_align="center"
        )

        mdfile.create_md_file()


def main():
    geol_units = gpd.read_file(
        fp.GEOL_PATH, layer="ATA_geological_units", ignore_fields=["CAPTDATE"]
    )
    build_field_values(geol_units)


if __name__ == "__main__":
    main()
