from src import first_letter_artists_count

EXPECTED_RESULT = [
    ('S', 27),
    ('A', 26),
    ('B', 22),
    ('T', 20),
    ('M', 20),
    ('C', 20),
    ('J', 17),
    ('L', 13),
    ('R', 12),
    ('P', 11),
    ('O', 11),
]


def test_get_first_letter_artists_count() -> None:
    tested_result = [tuple(row) for row in first_letter_artists_count.get_first_letter_artists_count()]
    assert tested_result == EXPECTED_RESULT
