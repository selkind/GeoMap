import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import geopandas as gpd
# import mdutils
from src.file_paths import GEOL_PATH

REMOVED_CHARS = " .,;"


def make_citations():
    geomap = gpd.read_file(GEOL_PATH, layer="ATA_sources_poly")
    published = geomap[geomap["PUBTYPE"].isin(["Published paper", "Published map"])]
    # print(published.columns)
    citations = {}
    # for i in range(published.shape[0]):
    for i in range(4):
        citations[published.iloc[i]['IDENTIFIER']] = build_bibtex(published.iloc[i])

    return citations


def make_mla_markdown_citation(record):
    separated_authors = split_authors(record['AUTHORS'])
    authors = format_mla_authors(separated_authors)
    return authors


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
            # author = author.replace(",", ".")
            individual_authors[i] = author.strip()
        return individual_authors


def format_mla_authors(split_authors):
    author_count = len(split_authors)
    if author_count > 2:
        return f'{split_authors[0].split(" ")[0]} et al.'
    elif author_count == 2:
        return f'{split_authors[0].split(" ")[0]} and {split_authors[1].split(" ")[0]}'
        print("meow")
    else:
        return split_authors


def main():
    print(make_citations())


if __name__ == "__main__":
    main()
