import pandas

from song.service import create_song_instance


def upload_csv_file():
    with open('music.csv', newline='') as csvfile:
        rows = pandas.read_csv(csvfile)
        create_song_instance(rows)
        return 'Songs are uploaded to database!'


def get_first_year(decade):
    # If year passed in url is not the first of a decade,
    # set the starting year accordingly
    if str(decade)[-1] != '0':
        start_of_dec = decade - int(str(decade)[-1])
    else:
        start_of_dec = decade
    return start_of_dec
