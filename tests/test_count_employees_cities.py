from src import count_employees_cities

EXPECTED_RESULT = [('Calgary', 5), ('Lethbridge', 2), ('Edmonton', 1)]


def test_count_employees_cities() -> None:
    tested_result = count_employees_cities.count_employees_cities()
    assert tested_result == EXPECTED_RESULT
