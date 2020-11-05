from src import queries

EXPECTED_RESULT = ('Mark', 'Philips')


def test_queries() -> None:
    tested_result = tuple(queries.queries())
    assert tested_result == EXPECTED_RESULT
