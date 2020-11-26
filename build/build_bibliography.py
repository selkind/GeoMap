import geopandas as gpd
# import mdutils
from file_paths import GEOL_PATH


def make_citations():
    geomap = gpd.read_file(GEOL_PATH, layer="ATA_sources_poly")
    published = geomap[geomap["PUBTYPE"].isin(["Published paper", "Published map"])]
    print(published.columns)

    citations = {}
    for i in range(published.shape[0]):
        citations[published.iloc[i]['IDENTIFIER']] = make_mla_markdown_citation(published.iloc[i])

    return citations


def make_mla_markdown_citation(record):
    authors = format_authors(record['AUTHORS'])

    return f"{authors}."


def format_authors(authors):
    individual_authors = authors.split(", ")
    author_count = len(individual_authors)
    if author_count > 2:
        formatted = f'{individual_authors[0].split(" ")[0]} et al.'
    elif author_count == 2:
        formatted = f'{individual_authors[0].split(" ")[0]} and {individual_authors[1].split(" ")[0]}'
    else:
        ampersand_split = authors.split("; ")
        if len(ampersand_split) == 2:
            formatted = f'{ampersand_split[0].split(" ")[0]} and {ampersand_split[1].split(" ")[0]}'
        else:
            formatted = authors
    return formatted


def main():
    test = make_citations()
    for i in test:
        print(i, test[i])


if __name__ == "__main__":
    main()
