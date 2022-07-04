import sys
import os

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import geopandas as gpd
import pandas as pd
from mdutils import MdUtils
import src.build_bibliography
import src.build_faults_field_glossary
import src.build_field_value_files
from src.build_field_glossary import build_field_glossary
import src.build_qualityinfo_field_glossary
import src.build_source_field_glossary
from src.build_utils import download_data
import src.file_paths as fp


def main():
    os.system("make clean")
    download_data()
    geol_units = gpd.read_file(fp.GEOL_PATH, layer="ATA_geological_units", ignore_fields=["CAPTDATE"]).fillna("")
    field_descr = pd.read_csv(fp.FIELD_DESCR_PATH).fillna("")
    mdfile = MdUtils(file_name=fp.GEOL_GLOSSARY_PATH, author="Samuel Elkind")
    src.build_bibliography.main()
    src.build_faults_field_glossary.main()

    # order matters here, field_glossary depends on field value file existence
    src.build_field_value_files.main()
    build_field_glossary(geol_units, field_descr, mdfile)

    src.build_qualityinfo_field_glossary.main()
    src.build_source_field_glossary.main()

    os.system("make html")
    os.system("make latexpdf")


if __name__ == "__main__":
    main()
