import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import geopandas as gpd
# import mdutils
from build.file_paths import GEOL_PATH


def make_citations():
    geomap = gpd.read_file(GEOL_PATH, layer="ATA_sources_poly")
    published = geomap[geomap["PUBTYPE"].isin(["Published paper", "Published map"])]
    print(published.columns)

    citations = {}
    for i in range(published.shape[0]):
        citations[published.iloc[i]['IDENTIFIER']] = make_mla_markdown_citation(published.iloc[i])

    return citations


def make_mla_markdown_citation(record):
    separated_authors = split_authors(record['AUTHORS'])
    authors = format_mla_authors(separated_authors)
    return authors


def split_authors(authors):
    # list is ordered so that entries with multiple delimiters will have the more likely delimiter chosen. ',' can be a delimiter for 
    # first and last name, whereas ampersand and semi-colon will not be and thus have higher 'priority'
    delimiters = ("&", ";", ",")
    delimiter = None
    for i in delimiters:
        if i in authors:
            delimiter = i
            break
    if delimiter is None:
        return [authors]
    else:
        individual_authors = authors.split(delimiter)
        for i in range(len(individual_authors)):
            author = individual_authors[i]
            etal = "et al."
            if etal in author:
                author = author.replace(etal, "")
                individual_authors.append("et al.")
            author = author.replace(",", ".")
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
    test = make_citations()


if __name__ == "__main__":
    main()
