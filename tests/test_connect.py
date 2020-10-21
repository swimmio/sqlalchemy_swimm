from src import connect


def test_connect_to_helloworldb() -> None:
    assert sorted(connect.connect_to_helloworldb()) == ['hello', 'sqlalchemy']
