import os
import geopandas as gpd
import file_paths as fp
import fields

import mdutils


def main():
    geomap = gpd.read_file(fp.GEOL_PATH)

    for i in geomap.columns:
        if i in fields.OMITTED_FIELDS:
            continue
        test = geomap[i].value_counts()
        values = test.index.tolist()
        if len(values) > 200:
            continue

        mdfile = mdutils.MdUtils(file_name=os.path.join(fp.FIELD_VALS_DIR, f"{i}_values.md"),
                                 title=f"Unique values of {i}")
        table_header = ["Value", "Number of Occurrences"]
        for j in values:
            table_header.extend([str(j), str(test[j])])

        mdfile.new_table(columns=2, rows=len(values) + 1, text=table_header, text_align="center")

        mdfile.create_md_file()


if __name__ == "__main__":
    main()
