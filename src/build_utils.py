import os
import mdutils
import requests
import zipfile
import io
import logging
import logging.config
import yaml
import pandas as pd

import src.file_paths as fp


def configure_logger(logger_name: str):
    logger = logging.getLogger(logger_name)
    with open(os.path.join(fp.BUILD_DIR, "logging.yml")) as f:
        log_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(log_config)
    return logger


logger = configure_logger(__name__)


def create_output(record: pd.DataFrame, field_name: str):
    """
    @param DataFrame Row record: Single row from a pandas DataFrame corresponding to the metadata category
    @param String field_name: the name of the field. Used in generating field values links

    @returns dict: a set of key, value pairs that can be iterated over to output on the markdown page.

    extract fields from each field metadata record and format special cases (e.g. field values links)
    """
    descr = record["field_description"].iloc[0]
    source = record["source_of_vals"].iloc[0]
    formatting = record["value_formatting"].iloc[0]
    metadata_link = record["field_metadata_link"].iloc[0]
    restrictions = record["field_value_restrictions"].iloc[0]
    field_value = None
    if os.path.exists(f"{os.path.join(fp.FIELD_VALS_DIR, field_name)}_values.md"):
        field_value = (
            f"{os.path.join(os.path.basename(fp.FIELD_VALS_DIR), field_name)}_values.md"
        )

    return {
        "Description": descr,
        "Source of Values": source,
        "Value Format": formatting,
        "Metadata Link": metadata_link,
        "Field Values": field_value,
        "Field Value Restrictions": restrictions,
    }


def format_output(descr_header, value, field_name):
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
    if replace_string in value:
        start = value.index(replace_string)
        end = start + len(replace_string)
        value = value[:start] + legend_link + value[end:]
    elif (
        descr_header in ["Metadata Link", "Field Value Restrictions"]
        and "http" in value
    ):
        value = mdutils.tools.Link.Inline.new_link(value, value)
    elif descr_header == "Field Value Restrictions" and ".md" in value:
        value = mdutils.tools.Link.Inline.new_link(value, "Restricted List")
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
        "https://data.gns.cri.nz/mapservice/Content/antarctica/geomap/GeoMAP_v201907.zip",
        stream=True,
    )
    logger.info("response received")

    if response.status_code != 200:
        logger.error(f"Data Download request status code: {response.status_code}")
        return
    logger.info(f"Extracting data to {fp.DATA_DIR}")
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(fp.DATA_DIR)
