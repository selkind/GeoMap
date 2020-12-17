import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..')))
from src.build_utils import create_output, format_output
import pandas as pd


@pytest.mark.parametrize('test_input,expected', [
    ((pd.DataFrame([{
      'field_description': '',
      'source_of_vals': '',
      'value_formatting': '',
      'field_metadata_link': '',
      'field_value_restrictions': '',
      }]),
     'TEST'),
     {"Description": '',
      "Source of Values": '',
      "Value Format": '',
      "Metadata Link": '',
      "Field Values": None,
      "Field Value Restrictions": ''
      }),
])
def test_create_output(test_input, expected):
    assert create_output(test_input[0], test_input[1]) == expected


@pytest.mark.parametrize('test_input,expected', [
    (('Description', '', 'TEST'), '')
])
def test_format_output(test_input, expected):
    assert format_output(test_input[0], test_input[1], test_input[2]) == expected
