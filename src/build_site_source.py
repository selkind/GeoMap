import sys
import os

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import geopandas as gpd
import pandas as pd
from mdutils import MdUtils
from src.build_bibliography import build_bibliography
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
    geol_units = gpd.read_file(
        fp.GEOL_PATH, layer="ATA_geological_units", ignore_fields=["CAPTDATE"]
    ).fillna("")
    sources = gpd.read_file(fp.GEOL_PATH, layer="ATA_sources_poly")
    build_bibliography(sources)
    src.build_faults_field_glossary.main()

    # order matters here, field_glossary depends on field value file existence
    src.build_field_value_files.main()

    field_descr = pd.read_csv(fp.FIELD_DESCR_PATH).fillna("")
    geol_glossary = MdUtils(file_name=fp.GEOL_GLOSSARY_PATH, author="Samuel Elkind")
    build_field_glossary(geol_units, field_descr, geol_glossary)

    src.build_qualityinfo_field_glossary.main()
    src.build_source_field_glossary.main()

    os.system("make html")
    os.system("make latexpdf")


if __name__ == "__main__":
    main()
