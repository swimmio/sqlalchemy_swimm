from src import count_customer_states

EXPECTED_RESULT = 11


def test_count_customer_countries() -> None:
    tested_result = count_customer_states.count_usa_customer_states()
    assert tested_result == EXPECTED_RESULT
