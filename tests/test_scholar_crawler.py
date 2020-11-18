import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
import pytest
from build.scholar_crawler import ScholarSpider
from tests.mock_response import fake_response_from_file

SCHOLAR_SEARCH_RESULTS_PATH = "../scholar_test_data/scholar_search_results.html"


class TestScholarCrawler:

    @pytest.fixture
    def spider(self):
        return ScholarSpider()

    @pytest.fixture
    def results_page(self):
        return fake_response_from_file(SCHOLAR_SEARCH_RESULTS_PATH)

    def test_parse_search_results(self, spider, results_page):
        assert spider.parse_search_results(results_page) == "4qAC3XBmStsJ"
