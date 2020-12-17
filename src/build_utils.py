import sys
import os
import mdutils
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..')))
import src.file_paths as fp


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
    field_value = None
    if os.path.exists(f"{os.path.join(fp.FIELD_VALS_DIR, field_name)}_values.md"):
        field_value = f"{os.path.join(os.path.basename(fp.FIELD_VALS_DIR), field_name)}_values.md"

    return {"Description": descr,
            "Source of Values": source,
            "Value Format": formatting,
            "Metadata Link": metadata_link,
            "Field Values": field_value,
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
    elif descr_header == "Field Value Restrictions" and '.md' in value:
        value = mdutils.tools.Link.Inline.new_link(value, "Restricted List")
    elif descr_header == "Field Values":
        value = mdutils.tools.Link.Inline.new_link(
            link=value,
            text="List of Values"
        )
    return value
