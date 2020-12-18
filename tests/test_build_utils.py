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
    ((pd.DataFrame([{
      'field_description': 'test',
      'source_of_vals': 'test',
      'value_formatting': 'test',
      'field_metadata_link': 'test',
      'field_value_restrictions': 'test',
      }]),
     'REGION'),
     {"Description": 'test',
      "Source of Values": 'test',
      "Value Format": 'test',
      "Metadata Link": 'test',
      "Field Values": 'field_values/REGION_values.md',
      "Field Value Restrictions": 'test'
      }),
])
def test_create_output(test_input, expected):
    assert create_output(test_input[0], test_input[1]) == expected


@pytest.mark.parametrize('test_input,expected', [
    (('Description', '', 'TEST'), ''),
    (('Description', 'legend', 'TEST'), '[legend](legend.md)'),
    (('Description', 'test legend test', 'TEST'), 'test [legend](legend.md) test'),
    (('Metadata Link', 'https', 'TEST'), '[https](https)'),
    (('Field Value Restrictions', 'test.md', 'TEST'), '[Restricted List](test.md)'),
    (('Field Values', 'test.md', 'TEST'), '[List of Values](test.md)'),
])
def test_format_output(test_input, expected):
    assert format_output(test_input[0], test_input[1], test_input[2]) == expected
