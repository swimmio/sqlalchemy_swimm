from src import most_invoices

EXPECTED_RESULT = (14, 'Berlin')


def test_most_invoices() -> None:
    tested_result = most_invoices.get_city_with_most_invoices()
    assert tested_result == EXPECTED_RESULT
