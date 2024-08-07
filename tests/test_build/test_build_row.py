"""Test function in module."""

from terminaltables3.build import build_row


def test_one_line():
    """Test with one line cells."""
    row = [
        ["Left Cell"],
        ["Center Cell"],
        ["Right Cell"],
    ]
    actual = [tuple(i) for i in build_row(row, ">", "|", "<")]
    expected = [
        (">", "Left Cell", "|", "Center Cell", "|", "Right Cell", "<"),
    ]
    assert actual == expected


def test_two_line():
    """Test with two line cells."""
    row = [
        [
            "Left ",
            "Cell1",
        ],
        [
            "Center",
            "Cell2 ",
        ],
        [
            "Right",
            "Cell3",
        ],
    ]
    actual = [tuple(i) for i in build_row(row, ">", "|", "<")]
    expected = [
        (">", "Left ", "|", "Center", "|", "Right", "<"),
        (">", "Cell1", "|", "Cell2 ", "|", "Cell3", "<"),
    ]
    assert actual == expected


def test_three_line():
    """Test with three line cells."""
    row = [
        [
            "Left ",
            "Cell1",
            "     ",
        ],
        [
            "Center",
            "Cell2 ",
            "      ",
        ],
        [
            "Right",
            "Cell3",
            "     ",
        ],
    ]
    actual = [tuple(i) for i in build_row(row, ">", "|", "<")]
    expected = [
        (">", "Left ", "|", "Center", "|", "Right", "<"),
        (">", "Cell1", "|", "Cell2 ", "|", "Cell3", "<"),
        (">", "     ", "|", "      ", "|", "     ", "<"),
    ]
    assert actual == expected


def test_single():
    """Test with single cell."""
    actual = [tuple(i) for i in build_row([["Cell"]], ">", "|", "<")]
    expected = [
        (">", "Cell", "<"),
    ]
    assert actual == expected


def test_empty():
    """Test with empty cell."""
    actual = [tuple(i) for i in build_row([[""]], ">", "|", "<")]
    expected = [
        (">", "", "<"),
    ]
    assert actual == expected


def test_no_cells():
    """Test with no cells."""
    actual = [tuple(i) for i in build_row([[]], ">", "|", "<")]
    expected = [
        (">", "<"),
    ]
    assert actual == expected

    actual = [tuple(i) for i in build_row([], ">", "|", "<")]
    expected = [
        (">", "<"),
    ]
    assert actual == expected
