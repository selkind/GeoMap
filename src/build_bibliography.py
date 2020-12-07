import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import geopandas as gpd
import mdutils
import urllib
import src.file_paths as fp

REMOVED_CHARS = " .,;"


def make_citations(records):
    citations = {}
    for i in range(records.shape[0]):
        citation = {}
        citation['bibtex'] = build_bibtex(records.iloc[i])
        citation['scholar_link'] = build_scholar_link(records.iloc[i])

        citations[records.iloc[i]['IDENTIFIER']] = citation

    return citations


def build_scholar_link(record):
    query = f'{record["TITLE"]} {record["AUTHORS"]} {int(record["YEAR"])}'.replace(" ", "%20")
    components = ('https', 'scholar.google.com', '/scholar', '', f'q={query}', '')
    return urllib.parse.urlunparse(components)


def split_name(author):
    name = author.split(" ")
    last_name = name[0].strip(REMOVED_CHARS)
    if len(name) > 1:
        initials = ""
        for i in name[1:]:
            for j in REMOVED_CHARS:
                i = i.replace(j, "")
            initials += i

        return (last_name, initials)
    return (last_name, None)


def build_bibtex(record):
    author_list = split_authors(record['AUTHORS'])

    authors = ""
    for i in author_list[:-1]:
        author = split_name(i)
        authors += f"{author[0]}, {author[1]} and " if author[1] else f"{author[0]} and "
    last_author = split_name(author_list[-1])
    authors += f"{last_author[0]}, {last_author[1]}" if last_author[1] else last_author[0]

    identifier = split_name(author_list[0])[0]
    identifier += str(int(record['YEAR']))
    identifier += record['TITLE'].split(" ")[0]

    return f"@article{{{identifier},\n" \
           f"  title={{{record['TITLE']}}},\n"\
           f"  authors={{{authors}}},\n"\
           f"  journal={{{record['PUBLICATION']}}},\n"\
           f"  year={{{int(record['YEAR'])}}}\n"\
           f"}}"


def split_authors(authors):
    # list is ordered so that entries with multiple delimiters will have the more likely delimiter chosen. ','
    # can be a delimiter for
    # first and last name, whereas ampersand and semi-colon will not be and thus have higher 'priority'
    in_string = " in "
    if in_string in authors:
        authors = authors[:authors.find(in_string)]

    delimiters = (' and ', '&', ';', ',')
    delimiter = None
    for i in delimiters:
        if i in authors:
            delimiter = i
            break

    # Nothing can be done about the entries with a list of authors and et al. until better data is added to the
    # authors field.
    # Same goes for references of references that are characterized by 'identifier in other identifier' format
    etal = " et al."
    if delimiter is None:
        if etal in authors:
            return [authors[:authors.find(etal)], 'et al.']
        return [authors]
    else:
        individual_authors = authors.split(delimiter)
        for i in range(len(individual_authors)):
            author = individual_authors[i]
            if etal in author:
                author = author.replace(etal, "")
                individual_authors.append("et al.")
            individual_authors[i] = author.strip()
        return individual_authors


def main():
    geomap = gpd.read_file(fp.GEOL_PATH, layer="ATA_sources_poly")
    published = geomap[geomap["PUBTYPE"].isin(["Published paper", "Published map"])]
    published_output = make_citations(published)

    mdfile = mdutils.MdUtils(file_name=fp.WORKS_REF_PATH, author="Samuel Elkind")

    mdfile.new_header(1, title='Works Referenced')

    for i in published_output:
        mdfile.new_header(2, title=i)

        mdfile.new_line("Bibtex citation", bold_italics_code='b')
        mdfile.insert_code(published_output[i]['bibtex'])

        mdfile.new_line(mdutils.tools.Link.Inline.new_link(link=published_output[i]['scholar_link'],
                                                           text='Google Scholar Link'), bold_italics_code='b')

    mdfile.create_md_file()


if __name__ == "__main__":
    main()
