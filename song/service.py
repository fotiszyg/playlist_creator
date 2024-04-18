from database.utils import db_save
from song.models import Song


def create_song_instance(rows):
    # Get songs from the csv file
    len_file = len(rows.index)
    i = 0
    while i < len_file:
        artist = rows.iloc[i]['Artist']
        title = rows.iloc[i]['Song']
        album = rows.iloc[i]['Album']
        year = int(rows.iloc[i]['Year'])
        # Create a Song instance and save in db
        song = Song(
            artist=artist,
            title=title,
            album=album,
            year=year
        )
        db_save(song)
        i += 1
