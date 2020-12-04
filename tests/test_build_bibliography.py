import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
print(sys.path)
import pytest
from build.build_bibliography import split_authors, split_name


@pytest.mark.parametrize("test_input,expected", [
    ("Isaac M.J., Chinn T.J., Edbrooke S.W., Forsyth P.J.", ['Isaac M.J.', 'Chinn T.J.', 'Edbrooke S.W.',
                                                             'Forsyth P.J.']),
    ("McElroy C.T., Rose G.", ['McElroy C.T.', 'Rose G.']),
    ("Cook Y. A.", ['Cook Y. A.']),
    ("Skinner D. N. B.", ['Skinner D. N. B.']),
    ("Skinner D.N.B.; Waterhouse B.C.; Brehaut G.; Sullivan K,", ['Skinner D.N.B.', 'Waterhouse B.C.', 'Brehaut G.',
     'Sullivan K.']),
    ("Ballance P.F.", ['Ballance P.F.']),
    ("Barrett P.J. et al. in Cooper A.K. et al. (eds)", ['Barrett P.J.', 'et al.']),
    ("Hamilton R.J.; Luyendyk B.P.; Sorlien C.", ['Hamilton R.J.', 'Luyendyk B.P.', 'Sorlien C.']),
    ("Rowell A.J., Rees M et al.", ['Rowell A.J.', 'Rees M', 'et al.']),
    ("Capponi G., Casnedi R., Castelli D., Flotmann T. et al.", ['Capponi G.', 'Casnedi R.', 'Castelli D.',
     'Flotmann T.', 'et al.']),
    ("McGregor V.R.; Wade F.A.", ['McGregor V.R.', 'Wade F.A.']),
])
def test_split_authors(test_input, expected):
    assert split_authors(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('Isaac M.J.', ('Isaac', 'MJ')),
    ('Rose G.', ('Rose', 'G')),
    ('Skinner D. N. B.', ('Skinner', 'DNB')),
])
def test_split_name(test_input, expected):
    assert split_name(test_input) == expected
