import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import pytest
import scrapy
from build.scholar_crawler import ScholarSpider, Citation, CitationSet
from tests.mock_response import fake_response_from_file

SCHOLAR_SEARCH_RESULTS_PATH = "../scholar_test_data/scholar_search_results2.html"
SCHOLAR_CITE_PATH = "../scholar_test_data/citation.html"


class TestScholarCrawler:

    @pytest.fixture
    def spider(self):
        return ScholarSpider(urls=[])

    @pytest.fixture
    def results_page(self):
        return fake_response_from_file(SCHOLAR_SEARCH_RESULTS_PATH)

    @pytest.fixture
    def cite_page(self):
        return fake_response_from_file(SCHOLAR_CITE_PATH)

    def test_parse_search_results(self, spider, results_page):
        return_value = spider.parse_search_results(results_page)
        assert type(return_value) == scrapy.Request
        assert return_value.url == "https://scholar.google.com/scholar?q=info:4qAC3XBmStsJ:scholar.google.com/"\
            "&output=cite&scirp=0&hl=en"

    def test_parse_citation_results(self, spider, cite_page):
        return_value = spider.parse_citation_results(cite_page, "")
        assert type(return_value) == CitationSet
        assert return_value["url"] is not None
        assert type(return_value["mla"] == Citation)
        assert return_value["mla"]["plain_text"] == ['Isaac, M. J., et al. '
                                                     '"Geology of the Olympus Range Area, Southern Victoria Land.\" ',
                                                     ' (1996).']
        assert return_value["mla"]["italics"] == "Antarctica. Institute of Geological"\
                                                 " and Nuclear Sciences, Lower Hutt, New Zealand"""
        assert return_value["bibtex"] == "https://scholar.googleusercontent.com/scholar.bib?q=info:4qAC3XBmStsJ:"\
                                         "scholar.google.com/&output=citation&scisdr=CgXC2t2nGAA:"\
                                         "AAGBfm0AAAAAX7wK3rp0bEjNSTvBK2kLAlClvznv2h8Y&scisig="\
                                         "AAGBfm0AAAAAX7wK3rc1diaBA-2FZ6g9mkvv57shz7Ns&scisf=4&ct=citation&"\
                                         "cd=-1&hl=en"
