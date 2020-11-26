import requests

scholar_query = "https://scholar.google.com/scholar?q=Geology of the Bull Pass - St Johns area, southern Victoria Land, Antarctica. Turnbull I.M., Allibone A.H., Forsyth P.J., Heron D.W. 1994"

r = requests.get(url=scholar_query)

with open("./scholar_test_data/scholar_search_results2.html", 'w') as f:
    f.write(r.text)

cite_query = "https://scholar.google.com/scholar?q=info:4qAC3XBmStsJ:scholar.google.com/&output=cite&scirp=0&hl=en"
r = requests.get(url=cite_query)

with open("./scholar_test_data/citation.html", 'w') as f:
    f.write(r.text)

bibtex_query = "https://scholar.googleusercontent.com/scholar.bib?q=info:4qAC3XBmStsJ:scholar.google.com/"\
    "&output=citation&scisdr=CgXC2t2nEIjL5FKBpyE:AAGBfm0AAAAAX7GEvyHQXiEFUhjbB4xfdap-fcgIzrFv&"\
    "scisig=AAGBfm0AAAAAX7GEvycnk4KEAyozZqZZcNRq1tfw41cm&scisf=4&ct=citation&cd=-1&hl=en"

r = requests.get(url=bibtex_query)

with open("./scholar_test_data/bibtex.html", 'w') as f:
    f.write(r.text)
