from song.models import Song


class TestSong:
    def test___init__(self):
        song = Song(
            artist='Black Sabbath',
            title='Paranoid',
            album='Paranoid',
            year=1970
        )
        assert song.artist == 'Black Sabbath'
        assert song.title == 'Paranoid'
        assert song.album == 'Paranoid'
        assert song.year == 1970
