import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import geopandas as gpd
import mdutils
# Globals
import src.file_paths as fp
import src.fields


def main():
    sources = gpd.read_file(fp.GEOL_PATH, layer="ATA_sources_poly").fillna("")
    print(sources.columns)
    # field_descr = pd.read_csv(fp.SOURCE_FIELD_DESCR_PATH).fillna("")


if __name__ == "__main__":
    main()
