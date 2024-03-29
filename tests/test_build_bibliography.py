import pytest
from src.build_bibliography import split_authors, split_name


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "Isaac M.J., Chinn T.J., Edbrooke S.W., Forsyth P.J.",
            ["Isaac M.J.", "Chinn T.J.", "Edbrooke S.W.", "Forsyth P.J."],
        ),
        ("McElroy C.T., Rose G.", ["McElroy C.T.", "Rose G."]),
        ("Cook Y. A.", ["Cook Y. A."]),
        ("Skinner D. N. B.", ["Skinner D. N. B."]),
        (
            "Skinner D.N.B.; Waterhouse B.C.; Brehaut G.; Sullivan K,",
            ["Skinner D.N.B.", "Waterhouse B.C.", "Brehaut G.", "Sullivan K,"],
        ),
        ("Ballance P.F.", ["Ballance P.F."]),
        (
            "Hamilton R.J.; Luyendyk B.P.; Sorlien C.",
            ["Hamilton R.J.", "Luyendyk B.P.", "Sorlien C."],
        ),
        ("Rowell A.J., Rees M et al.", ["Rowell A.J.", "Rees M", "et al."]),
        (
            "Capponi G., Casnedi R., Castelli D., Flotmann T. et al.",
            ["Capponi G.", "Casnedi R.", "Castelli D.", "Flotmann T.", "et al."],
        ),
        ("McGregor V.R.; Wade F.A.", ["McGregor V.R.", "Wade F.A."]),
        ("Barrett P.J. et al. in Cooper A.K. et al. (eds)", ["Barrett P.J.", "et al."]),
        ("foo & bar in cooper et al.", ["foo", "bar"]),
        ("foo G. & bar K. in cooper et al.", ["foo G.", "bar K."]),
        ("foo G. in cooper et al.", ["foo G."]),
        ("foo G. and bar K. in cooper et al.", ["foo G.", "bar K."]),
        ("McElroy C.T. and Rose G.", ["McElroy C.T.", "Rose G."]),
        ("McElroy, C.T. and Rose G.", ["McElroy, C.T.", "Rose G."]),
        ("McElroy, C.T. and Rose, G.", ["McElroy, C.T.", "Rose, G."]),
    ],
)
def test_split_authors(test_input, expected):
    assert split_authors(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Isaac M.J.", ("Isaac", "MJ")),
        ("Rose G.", ("Rose", "G")),
        ("Skinner D. N. B.", ("Skinner", "DNB")),
    ],
)
def test_split_name(test_input, expected):
    assert split_name(test_input) == expected
