import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import geopandas as gpd
import pandas as pd
import mdutils
# Globals
import src.file_paths as fp
import src.fields


def create_output(record, field_name):
    """
    @param DataFrame Row record: Single row from a pandas DataFrame corresponding to the metadata category
    @param String field_name: the name of the field. Used in generating field values links

    @returns dict: a set of key, value pairs that can be iterated over to output on the markdown page.

    extract fields from each field metadata record and format special cases (e.g. field values links)
    """
    descr = record['field_description'].iloc[0]
    source = record['source_of_vals'].iloc[0]
    formatting = record['value_formatting'].iloc[0]
    metadata_link = record['field_metadata_link'].iloc[0]
    restrictions = record['field_value_restrictions'].iloc[0]
    return {"Description": descr,
            "Source of Values": source,
            "Value Format": formatting,
            "Metadata Link": metadata_link,
            "Field Values": f"{os.path.join(os.path.basename(fp.FIELD_VALS_DIR), field_name)}_values.md",
            "Field Value Restrictions": restrictions}


def format_output(descr_header, value, field_name):
    """
    @param String descr_header: the header of the metadata field to be formatted
    @param String value: the metadata to be formatted for outputting
    @param String field_name: The name of the field to be used in the Field Values link

    @returns String: the formatted value

    Creates inline links for particular metadata fields
    """
    replace_string = "legend"
    legend_link = mdutils.tools.Link.Inline.new_link(link="legend.md", text=replace_string)
    if replace_string in value:
        start = value.index(replace_string)
        end = start + len(replace_string)
        value = value[:start] + legend_link + value[end:]
    elif descr_header in ["Metadata Link", "Field Value Restrictions"] and "http" in value:
        value = mdutils.tools.Link.Inline.new_link(value, value)
    elif descr_header == "Field Values":
        value = mdutils.tools.Link.Inline.new_link(
            link=value,
            text="List of Values"
        )
    return value


def create_stats(value_counts):
    """
    @param pd.Series value_counts: the value counts of the field in question

    @returns dict: the statistics to be output in markdown
    """
    stats = {}
    stats["Unique Values"] = len(value_counts)
    if len(value_counts) > 0:
        stats["Most frequently occurring value"] = value_counts.index[0]
        stats["Number of values with a single occurrence"] = len([k for k in value_counts if k == 1])
    return stats


def main():
    geomap = gpd.read_file(fp.GEOL_PATH, layer="ATA_geological_units")
    field_descr = pd.read_csv(fp.FIELD_DESCR_PATH).fillna("")

    mdfile = mdutils.MdUtils(file_name=fp.GEOL_GLOSSARY_PATH, author="Samuel Elkind")

    mdfile.new_header(1, title="Geological Units Field Glossary")
    for i in geomap.columns:
        if i in src.fields.OMITTED_FIELDS:
            continue
        try:
            value_counts = geomap[i].value_counts()
        except AttributeError:
            continue

        record = field_descr.loc[field_descr['field_name'] == i]
        output = create_output(record, i)

        mdfile.new_header(2, i)
        for j in output:
            if not output[j]:
                continue
            output[j] = format_output(j, output[j], i)
            mdfile.new_line(f'{j}:', bold_italics_code='b')
            mdfile.new_line('')
            mdfile.new_line(text=output[j])
            mdfile.new_line('')

        mdfile.new_line('More Information:', bold_italics_code='b')
        mdfile.new_line()

        stats = create_stats(value_counts)
        mdfile.new_list([f"{k}: {stats[k]}" for k in stats])

    mdfile.create_md_file()


if __name__ == "__main__":
    main()
