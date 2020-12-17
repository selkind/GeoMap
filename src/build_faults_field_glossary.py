import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import geopandas as gpd
import pandas as pd
import mdutils
# Globals
import src.file_paths as fp
import src.fields
from src.build_utils import create_output, format_output


def main():
    faults = gpd.read_file(fp.GEOL_PATH, layer="ATA_faults").fillna("")
    field_descr = pd.read_csv(fp.FAULTS_FIELD_DESCR_PATH).fillna("")

    mdfile = mdutils.MdUtils(file_name=fp.FAULTS_GLOSSARY_PATH, author='Samuel Elkind')

    mdfile.new_header(1, title='Faults Field Glossary')

    for i in faults.columns:
        if i in src.fields.OMITTED_FIELDS:
            continue

        record = field_descr.loc[field_descr['field_name'] == i]
        output = create_output(record, i)

        mdfile.new_header(2, i)

        for j in output:
            if not output[j] or j == 'Field Values':
                continue
            output[j] = format_output(j, output[j], i)
            mdfile.new_line(f'{j}:', bold_italics_code='b')
            mdfile.new_line('')
            mdfile.new_line(text=output[j])
            mdfile.new_line('')

    mdfile.create_md_file()


if __name__ == "__main__":
    main()
