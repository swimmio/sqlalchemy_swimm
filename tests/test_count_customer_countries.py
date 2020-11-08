from src import count_customer_countries

EXPECTED_RESULT = 24


def test_count_customer_countries() -> None:
    tested_result = count_customer_countries.count_customer_countries()
    assert tested_result == EXPECTED_RESULT
