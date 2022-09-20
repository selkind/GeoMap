import os
from typing import Dict
import logging
import logging.config
import yaml
import re

import requests
import zipfile
import io

import geopandas as gpd
import mdutils
import pandas as pd
import fiona

import src.file_paths as fp
import src.fields as fields


def configure_logger(logger_name: str):
    logger = logging.getLogger(logger_name)
    with open(os.path.join(fp.BUILD_DIR, "logging.yml")) as f:
        log_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(log_config)
    return logger


logger = configure_logger(__name__)


def build_field_glossary(
    data: gpd.GeoDataFrame, layer: str, datadict_path: str, output_path: str
) -> None:
    field_descr = pd.read_csv(datadict_path).fillna("")

    mdfile = mdutils.MdUtils(file_name=output_path, author="Samuel Elkind")

    mdfile.new_header(1, title=f"{layer} Field Glossary")

    for i in data.columns:
        if i in fields.OMITTED_FIELDS:
            continue
        record = field_descr.loc[field_descr["Field Name"] == i]
        if record.shape[0] == 0:
            logger.info(
                f"field {i} has no metadata. Add an entry to {fp.FAULTS_FIELD_DESCR_PATH}"
            )
            continue
        output = create_output(record, i)

        mdfile.new_header(2, i)

        for j in fields.OUTPUT_ORDERED_FIELDS:
            if j not in output or not output[j] or output[j] == "":
                continue
            output[j] = format_output(j, output[j])
            mdfile.new_line(f"+ **{j}:** {output[j]}")
            mdfile.new_line("")

        value_counts = data[i].value_counts()

        mdfile.new_line("More Information:", bold_italics_code="b")
        mdfile.new_line()
        stats = create_stats(value_counts)
        [mdfile.new_line(f"+ **{k}:** {stats[k]}") for k in stats]

    mdfile.create_md_file()


def create_stats(value_counts):
    """
    @param pd.Series value_counts: the value counts of the field in question

    @returns dict: the statistics to be output in markdown
    """
    stats = {}
    stats["Unique Values"] = len(value_counts)
    if len(value_counts) > 0:
        stats["Most frequently occurring value"] = value_counts.index[0]
        stats["Number of values with a single occurrence"] = len(
            [k for k in value_counts if k == 1]
        )
    return stats


def create_output(record: pd.DataFrame, field_name: str):
    """
    @param DataFrame Row record: Single row from a pandas DataFrame corresponding to the metadata category
    @param String field_name: the name of the field. Used in generating field values links

    @returns dict: a set of key, value pairs that can be iterated over to output on the markdown page.

    extract fields from each field metadata record and format special cases (e.g. field values links)
    """
    field_value = (
        f"{os.path.join(os.path.basename(fp.FIELD_VALS_DIR), field_name)}_values.md"
        if os.path.exists(f"{os.path.join(fp.FIELD_VALS_DIR, field_name)}_values.md")
        else ""
    )
    entry = {i: str(j[0]) for i, j in record.to_dict(orient="list").items()}

    entry["Field Values"] = field_value

    return entry


def format_output(descr_header, value):
    """
    @param String descr_header: the header of the metadata field to be formatted
    @param String value: the metadata to be formatted for outputting
    @param String field_name: The name of the field to be used in the Field Values link

    @returns String: the formatted value

    Creates inline links for particular metadata fields
    """
    replace_string = "legend"
    # This link will only work for documentation pages in the base /source directory, otherwise the path to legend
    # won't work
    legend_link = mdutils.tools.Link.Inline.new_link(
        link="legend.md", text=replace_string
    )

    restricted_vals = re.match(r"See (.+)\.list tab", value)

    if replace_string in value:
        start = value.index(replace_string)
        end = start + len(replace_string)
        value = value[:start] + legend_link + value[end:]
    elif "http" in value:
        value = mdutils.tools.Link.Inline.new_link(value, value)
    elif restricted_vals:
        value = mdutils.tools.Link.Inline.new_link(
            "restricted_values.md", "Restricted List"
        )
    elif descr_header == "Field Values":
        value = mdutils.tools.Link.Inline.new_link(link=value, text="List of Values")
    return value


def download_data():
    if os.path.exists(fp.GEOL_PATH):
        logger.info(f"Geodatabase already exists in {fp.GEOL_PATH}")
        return
    if not os.path.exists(fp.DATA_DIR):
        logger.info(f"Data directory does not exist. Creating it at {fp.DATA_DIR}")
        os.mkdir(fp.DATA_DIR)

    logger.info("sending request to download data")
    response = requests.get(
        "https://data.gns.cri.nz/mapservice/Content/antarctica/geomap/ATA_SCAR_GeoMAP_v2022_08_ESRI.zip",
        stream=True,
    )
    logger.info("response received")

    if response.status_code != 200:
        logger.error(f"Data Download request status code: {response.status_code}")
        return
    logger.info(f"Extracting data to {fp.DATA_DIR}")
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(fp.DATA_DIR)


def get_layer_names() -> Dict[str, str]:
    layer_name_modifier = "GeoMAP_"
    if any([layer_name_modifier in i for i in fiona.listlayers(fp.GEOL_PATH)]):
        return {
            "geol_layer": "ATA_GeoMAP_geological_units",
            "sources_layer": "ATA_GeoMAP_sources",
            "faults_layer": "ATA_GeoMAP_faults",
            "quality_info_layer": "ATA_GeoMAP_quality",
        }
    else:
        return {
            "geol_layer": "ATA_geological_units",
            "sources_layer": "ATA_sources_poly",
            "faults_layer": "ATA_faults",
            "quality_info_layer": "ATA_GeoMAP_qualityinformation",
        }
