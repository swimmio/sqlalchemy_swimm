import pytest
from src import count_artist_tracks


@pytest.mark.parametrize('artist_name, expected_track_count', [('Foo Fighters', 44), ('AC/DC', 18), ('Queen', 45)])
def test_insertions(artist_name: str, expected_track_count: int) -> None:
    count_tracks = count_artist_tracks.count_artist_tracks(artist_name)
    assert count_tracks == expected_track_count
