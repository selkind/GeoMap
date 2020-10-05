import os

DOC_DIR = os.path.dirname(os.path.realpath(__file__))

BASE_DIR = os.path.dirname(DOC_DIR)

FIELD_DESCR_PATH = os.path.join(DOC_DIR, "field_descr_data.csv")

DATA_DIR = os.path.join(BASE_DIR, "data")
GEOL_PATH = os.path.join(DATA_DIR, "ATA_SCAR_GeoMAP_geology.gdb")
CULTURE_PATH = os.path.join(DATA_DIR, "ATA_SCAR_GeoMAP_culture.gdb")

FIELD_VALS_DIR = os.path.join(DOC_DIR, "field_values")

for i in [FIELD_DESCR_PATH, GEOL_PATH, CULTURE_PATH]:
    if not os.path.exists(i) and not os.path.isfile(i):
        raise FileNotFoundError(f"{i} does not exist")

