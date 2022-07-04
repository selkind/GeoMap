import sys
import os

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import geopandas as gpd
from src.build_bibliography import build_bibliography
from src.build_faults_field_glossary import build_faults_field_glossary
from src.build_field_value_files import build_field_values
from src.build_field_glossary import build_field_glossary
from src.build_qualityinfo_field_glossary import build_quality_info_field_glossary
from src.build_source_field_glossary import build_source_field_glossary
from src.build_utils import download_data
import src.file_paths as fp


def main():
    os.system("make clean")
    download_data()

    geol_units = gpd.read_file(
        fp.GEOL_PATH, layer="ATA_geological_units", ignore_fields=["CAPTDATE"]
    ).fillna("")
    sources = gpd.read_file(fp.GEOL_PATH, layer="ATA_sources_poly")
    faults = gpd.read_file(fp.GEOL_PATH, layer="ATA_faults").fillna("")
    quality_info = gpd.read_file(
        fp.GEOL_PATH, layer="ATA_GeoMAP_qualityinformation"
    ).fillna("")

    build_bibliography(sources)
    build_faults_field_glossary(faults)

    # order matters here, field_glossary depends on field value file existence
    build_field_values(geol_units)
    build_field_glossary(geol_units)

    build_quality_info_field_glossary(quality_info)
    build_source_field_glossary(sources)

    os.system("make html")
    os.system("make latexpdf")


if __name__ == "__main__":
    main()
