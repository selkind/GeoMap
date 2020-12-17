import sys
import os
import geopandas as gpd
import pandas as pd
import mdutils
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import src.file_paths as fp


def main():
    faults = gpd.read_file(fp.GEOL_PATH, layer="ATA_faults").fillna("")

    field_values = pd.read_csv(fp.RESTRICTED_VALS_PATH).fillna("")

    field_map = {'Accuracy': {'fields': ['ACCURACY'], 'fp': fp.ACCURACY_PATH},
                 'Fault Type': {'fields': ['TYPE'], 'fp': fp.FAULT_TYPE_PATH},
                 'Fault Sense': {'fields': ['DOMSENSE', 'SUBSENSE'], 'fp': fp.FAULT_SENSE_PATH},
                 'Down-thrown Side': {'fields': ['DOWNQUAD'], 'fp': fp.DOWN_THROWN_PATH},
                 'Plot Rank': {'fields': ['PLOTRANK'], 'fp': fp.PLOTRANK_PATH}
                 }

    for i in field_values.columns:
        mdfile = mdutils.MdUtils(file_name=field_map[i]['fp'], author='Samuel Elkind')
        mdfile.new_header(1, title=f'{i} Restricted Values')

        rel_fields = "Relevant Fields: "
        for k in field_map[i]['fields']:
            rel_fields += f"{k}, "
        rel_fields = rel_fields[:-2]

        mdfile.new_line(rel_fields)

        qmap_vals = [i for i in field_values[i] if i != ""]
        used_vals = []
        for j in field_map[i]['fields']:
            used_vals = list(set(used_vals + list(field_values[field_values[i].isin(faults[j])][i].unique())))
            geomap_specific = list(faults[~faults[j].isin(qmap_vals)][j].unique())

        restricted_list = ["Value", "Value Present in Dataset"]
        for item in qmap_vals + geomap_specific:
            if str(item).strip() in restricted_list:
                continue
            restricted_list.append(str(item).strip())
            if item in used_vals:
                restricted_list.append("[ x ]")
            else:
                restricted_list.append("[  ]")
        

        mdfile.new_table(2, int(len(restricted_list) / 2), restricted_list, 'center')

        mdfile.create_md_file()


if __name__ == "__main__":
    main()
