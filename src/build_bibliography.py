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
        citation["bibtex"] = build_bibtex(records.iloc[i])
        citation["scholar_link"] = build_scholar_link(records.iloc[i])

        citations[records.iloc[i]["IDENTIFIER"]] = citation

    return citations


def build_scholar_link(record):
    query = f'{record["TITLE"]} {record["AUTHORS"]} {int(record["YEAR"])}'.replace(
        " ", "%20"
    )
    components = ("https", "scholar.google.com", "/scholar", "", f"q={query}", "")
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
    author_list = split_authors(record["AUTHORS"])

    authors = ""
    for i in author_list[:-1]:
        author = split_name(i)
        authors += (
            f"{author[0]}, {author[1]} and " if author[1] else f"{author[0]} and "
        )
    last_author = split_name(author_list[-1])
    authors += (
        f"{last_author[0]}, {last_author[1]}" if last_author[1] else last_author[0]
    )

    identifier = split_name(author_list[0])[0]
    identifier += str(int(record["YEAR"]))
    identifier += (record["TITLE"][:7] + record["TITLE"][7:].split(" ")[0]).replace(
        " ", ""
    )

    return (
        f"@article{{{identifier},\n"
        f"  title={{{record['TITLE']}}},\n"
        f"  authors={{{authors}}},\n"
        f"  journal={{{record['PUBLICATION']}}},\n"
        f"  year={{{int(record['YEAR'])}}}\n"
        f"}}"
    )


def split_authors(authors):
    # list is ordered so that entries with multiple delimiters will have the more likely delimiter chosen. ','
    # can be a delimiter for
    # first and last name, whereas ampersand and semi-colon will not be and thus have higher 'priority'
    in_string = " in "
    if in_string in authors:
        authors = authors[: authors.find(in_string)]

    delimiters = (" and ", "&", ";", ",")
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
            return [authors[: authors.find(etal)], "et al."]
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


def find_first_digit(identifier):
    for i, j in enumerate(identifier):
        if j.isdigit():
            return i
    return i


def build_bibliography(sources: gpd.GeoDataFrame):
    pub_paper_file = mdutils.MdUtils(
        file_name=fp.PUB_PAPER_REF_PATH, author="Samuel Elkind"
    )
    pub_map_file = mdutils.MdUtils(
        file_name=fp.PUB_MAP_REF_PATH, author="Samuel Elkind"
    )
    gis_file = mdutils.MdUtils(file_name=fp.GIS_REF_PATH, author="Samuel Elkind")
    thesis_file = mdutils.MdUtils(file_name=fp.THESIS_REF_PATH, author="Samuel Elkind")
    unpub_file = mdutils.MdUtils(file_name=fp.UNPUB_REF_PATH, author="Samuel Elkind")
    unk_file = mdutils.MdUtils(file_name=fp.UNK_REF_PATH, author="Samuel Elkind")

    for i in [
        ("Published paper", pub_paper_file, "Published Paper"),
        ("Published map", pub_map_file, "Published Map"),
        ("GIS dataset", gis_file, "GIS Dataset"),
        ("Thesis", thesis_file, "Thesis"),
        ("Unpublished", unpub_file, "Unpublished"),
        ("Unknown", unk_file, "Unknown"),
    ]:

        works = sources[sources["PUBTYPE"] == i[0]].fillna(0)
        works_citations = make_citations(works)

        i[1].new_header(1, title=f"{i[2]} Works Referenced")
        for j in sorted(
            works_citations,
            key=lambda x: (
                x[: find_first_digit(x)],
                x[find_first_digit(x) :],  # noqa: E203
            ),
        ):
            i[1].new_header(2, title=j)

            i[1].new_line("Bibtex citation", bold_italics_code="b")
            i[1].insert_code(works_citations[j]["bibtex"])

            if i[0] not in ["Unpublished", "Unknown"]:

                i[1].new_line(
                    mdutils.tools.Link.Inline.new_link(
                        link=works_citations[j]["scholar_link"],
                        text="Google Scholar Link",
                    ),
                    bold_italics_code="b",
                )

        i[1].create_md_file()


def main():
    sources = gpd.read_file(fp.GEOL_PATH, layer="ATA_sources_poly")
    build_bibliography(sources)


if __name__ == "__main__":
    main()
