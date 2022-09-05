import os

BUILD_DIR = os.path.dirname(os.path.realpath(__file__))

BASE_DIR = os.path.dirname(BUILD_DIR)
SITE_DIR = os.path.join(BASE_DIR, "source")

FIELD_DESCR_PATH = os.path.join(BUILD_DIR, "field_descr_data.csv")
SOURCE_FIELD_DESCR_PATH = os.path.join(BUILD_DIR, "sources_field_descr_data.csv")
FAULTS_FIELD_DESCR_PATH = os.path.join(BUILD_DIR, "fault_field_descr_data.csv")
QUALINFO_FIELD_DESCR_PATH = os.path.join(BUILD_DIR, "qualityinfo_field_descr_data.csv")

DATA_DIR = os.path.join(BASE_DIR, "data")
GEOL_PATH = os.path.join(DATA_DIR, "ATA_SCAR_GeoMAP_geology.gdb")
CULTURE_PATH = os.path.join(DATA_DIR, "ATA_SCAR_GeoMAP_culture.gdb")

FIELD_VALS_DIR = os.path.join(SITE_DIR, "field_values")

GEOL_GLOSSARY_PATH = os.path.join(SITE_DIR, "field_glossary.md")
SOURCE_GLOSSARY_PATH = os.path.join(SITE_DIR, "source_glossary.md")
FAULTS_GLOSSARY_PATH = os.path.join(SITE_DIR, "faults_glossary.md")
QUALINFO_GLOSSARY_PATH = os.path.join(SITE_DIR, "qualinfo_glossary.md")

WORKS_REF_DIR = os.path.join(SITE_DIR, "works_referenced")
PUB_PAPER_REF_PATH = os.path.join(WORKS_REF_DIR, "published_paper.md")
PUB_MAP_REF_PATH = os.path.join(WORKS_REF_DIR, "published_map.md")
GIS_REF_PATH = os.path.join(WORKS_REF_DIR, "gis.md")
THESIS_REF_PATH = os.path.join(WORKS_REF_DIR, "thesis.md")
UNPUB_REF_PATH = os.path.join(WORKS_REF_DIR, "unpublished.md")
UNK_REF_PATH = os.path.join(WORKS_REF_DIR, "unknown.md")

RESTRICTED_VALS_SOURCE_DIR = os.path.join(BUILD_DIR, "restricted_values")
RESTRICTED_VALS_PATH = os.path.join(SITE_DIR, "restricted_values.md")
