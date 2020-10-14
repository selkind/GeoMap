import pandas as pd
import geopandas as gpd
import os

import mdutils

def main():
    cwd = os.getcwd()
    geomap_path = os.path.join(cwd, "data", "ATA_SCAR_GeoMAP_geology.gdb")
    geomap = gpd.read_file(geomap_path)
    field_values_path = os.path.join(cwd, "documentation", "field_values")

    for i in geomap.columns:
        if i in ["Shape_Length", "Shape_Area", "geometry", "SYMBOL"]:
            continue
        test = geomap[i].value_counts()
        values = test.index.tolist()

        mdfile = mdutils.MdUtils(file_name=os.path.join(field_values_path, f"{i}_values.md"), title=f"Unique values of {i}")
        table_header = ["Value", "Number of Occurrences"]
        for j in values:
            table_header.extend([str(j), str(test[j])])

        mdfile.new_table(columns=2, rows=len(values) + 1, text=table_header, text_align="center")

        mdfile.create_md_file()


if __name__ == "__main__":
    main()
