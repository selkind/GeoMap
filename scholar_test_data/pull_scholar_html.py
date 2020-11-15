import requests

scholar_query = """
                https://scholar.google.com/scholar?q=Geology of the Olympus Range area, 
                southern Victoria Land, Antarctica. Isaac M.J., Chinn T.J., Edbrooke S.W., 
                Forsyth P.J. 1996
                """

r = requests.get(url=scholar_query)

with open("./scholar_test_data/scholar_search_results.html", 'w') as f:
    f.write(r.text)


cite_query = """
             https://scholar.google.com/scholar?q=Geology%20of%20the%20Olympus%20Range%20area,
             %20southern%20Victoria%20Land,%20Antarctica.%20Isaac%20M.J.,%20Chinn%20T.J.,
             %20Edbrooke%20S.W.,%20Forsyth%20P.J.%201996#d=gs_cit&u=%2Fscholar
             %3Fq%3Dinfo%3A4qAC3XBmStsJ%3Ascholar.google.com%2F%26output%3Dcite%26scirp%3D0%26hl%3Den
             """

r = requests.get(url=cite_query)

with open("./scholar_test_data/citation.html", 'w') as f:
    f.write(r.text)

bibtex_query = """
               https://scholar.googleusercontent.com/scholar.bib?q=info:4qAC3XBmStsJ
               :scholar.google.com/&output=citation&scisdr=CgXC2t2nEIjL5FKBpyE
               :AAGBfm0AAAAAX7GEvyHQXiEFUhjbB4xfdap-fcgIzrFv&scisig=AAGBfm0AAAAAX7GEvycnk4K
               EAyozZqZZcNRq1tfw41cm&scisf=4&ct=citation&cd=-1&hl=en
               """

r = requests.get(url=bibtex_query)

with open("./scholar_test_data/bibtex.html", 'w') as f:
    f.write(r.text)
