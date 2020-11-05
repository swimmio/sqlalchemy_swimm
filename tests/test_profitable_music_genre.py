from decimal import Decimal

from src import profitable_music_genre

EXPECTED_RESULT = [
    (Decimal('826.65'), 'Rock'),
    (Decimal('382.14'), 'Latin'),
    (Decimal('261.36'), 'Metal'),
    (Decimal('241.56'), 'Alternative & Punk'),
    (Decimal('93.53'), 'TV Shows'),
    (Decimal('79.20'), 'Jazz'),
    (Decimal('60.39'), 'Blues'),
    (Decimal('57.71'), 'Drama'),
    (Decimal('40.59'), 'R&B/Soul'),
    (Decimal('40.59'), 'Classical'),
    (Decimal('39.80'), 'Sci Fi & Fantasy'),
    (Decimal('29.70'), 'Reggae'),
    (Decimal('27.72'), 'Pop'),
    (Decimal('19.80'), 'Soundtrack'),
    (Decimal('17.91'), 'Comedy'),
    (Decimal('16.83'), 'Hip Hop/Rap'),
    (Decimal('14.85'), 'Bossa Nova'),
    (Decimal('13.86'), 'Alternative'),
    (Decimal('12.87'), 'World'),
    (Decimal('11.94'), 'Science Fiction'),
    (Decimal('11.88'), 'Heavy Metal'),
    (Decimal('11.88'), 'Electronica/Dance'),
    (Decimal('9.90'), 'Easy Listening'),
    (Decimal('5.94'), 'Rock And Roll'),
]


def test_most_profitable_music_genre() -> None:
    tested_result = [tuple(row) for row in profitable_music_genre.most_profitable_music_genre()]
    assert tested_result == EXPECTED_RESULT
