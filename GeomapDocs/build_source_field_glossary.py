import sys
import os
import geopandas as gpd
import pandas as pd
import mdutils
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import GeomapDocs.file_paths as fp
import GeomapDocs.fields


def main():
    sources = gpd.read_file(fp.GEOL_PATH, layer="ATA_sources_poly").fillna("")
    field_descr = pd.read_csv(fp.SOURCE_FIELD_DESCR_PATH).fillna("")

    mdfile = mdutils.MdUtils(file_name=fp.SOURCE_GLOSSARY_PATH, author='Samuel Elkind')

    mdfile.new_header(1, title='Sources Field Glossary')

    for i in sources.columns:
        if i in GeomapDocs.fields.OMITTED_FIELDS:
            continue

        record = field_descr.loc[field_descr['field_name'] == i]

        mdfile.new_header(2, i)

        for j in [('field_description', 'Field Description'), ('value_formatting', 'Formatting of Values')]:
            mdfile.new_line(f'{j[1]}:', bold_italics_code='b')
            mdfile.new_line('')
            mdfile.new_line(text=record[j[0]].iloc[0])
            mdfile.new_line('')

    mdfile.create_md_file()


if __name__ == "__main__":
    main()
