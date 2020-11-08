import typing

import pytest
from src import oldest_employees


@pytest.mark.parametrize(
    'count, expected',
    [
        (3, [('Margaret', 'Park'), ('Nancy', 'Edwards'), ('Andrew', 'Adams')]),
        (1, [('Margaret', 'Park')]),
        (
            15,
            [
                ('Margaret', 'Park'),
                ('Nancy', 'Edwards'),
                ('Andrew', 'Adams'),
                ('Steve', 'Johnson'),
                ('Laura', 'Callahan'),
                ('Robert', 'King'),
                ('Michael', 'Mitchell'),
                ('Jane', 'Peacock'),
            ],
        ),
    ],
)
def test_oldest_employees(count: int, expected: typing.List[typing.Tuple[str, str]]) -> None:
    tested_result = oldest_employees.get_oldest_employees(count)
    assert tested_result == expected
