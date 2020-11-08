from src import something_like

EXPECTED_RESULT = ('Mark', 'Philips')


def test_something_like() -> None:
    tested_result = tuple(something_like.something_like())
    assert tested_result == EXPECTED_RESULT
