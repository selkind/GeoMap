import sys
import os
import geopandas as gpd
import pandas as pd
import mdutils
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import src.file_paths as fp
import src.fields


def main():
    qi = gpd.read_file(fp.GEOL_PATH, layer="ATA_GeoMAP_qualityinformation").fillna("")
    field_descr = pd.read_csv(fp.QUALINFO_FIELD_DESCR_PATH).fillna("")

    mdfile = mdutils.MdUtils(file_name=fp.QUALINFO_GLOSSARY_PATH, author='Samuel Elkind')

    mdfile.new_header(1, title='Quality Information Field Glossary')

    for i in qi.columns:
        if i in src.fields.OMITTED_FIELDS:
            continue

        record = field_descr.loc[field_descr['field_name'] == i]

        mdfile.new_header(2, i)

        for j, k in [('field_description', 'Field Description'), ('value_formatting', 'Formatting of Values')]:
            if not record[j].iloc[0]:
                continue
            mdfile.new_line(f'{k}:', bold_italics_code='b')
            mdfile.new_line('')
            mdfile.new_line(text=record[j].iloc[0])
            mdfile.new_line('')

    mdfile.create_md_file()


if __name__ == "__main__":
    main()
