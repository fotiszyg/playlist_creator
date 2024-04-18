from sqlalchemy import select

from common import get_first_year
from database.extensions import db
from song.models import Song


def decade_playlist(decade):
    # returns the songs in db that belong to a specific decade
    playlist = []
    year = get_first_year(decade)
    for _ in range(1, 10):
        songs = db.session.scalars(
            select(Song.title)
            .where(Song.year == year)
        ).all()
        if songs:
            for song in songs:
                playlist.append(song)
        year = year + 1
    if not playlist:
        raise ValueError('No songs from this decade, sorry!')
    return playlist
