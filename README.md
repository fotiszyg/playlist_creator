# Playlist creator

This simple app is part of my side project, 
with which I want to create playlists from my music library. 

I have created already the csv file, which contain some details for a few songs.

The first endpoint is to gather all songs for a specific decade.

In the future this will be extended to create more specialised lists from the database
(for example based on views of Spotify, rating or specific style of music with info taken from Discogs).

## How to run

First install all dependencies as listed.

Second step is to run the following command from your terminal so application starts:
```
python -m flask --app app run --port 8000 --debug
```


Then open http://127.0.0.1:8000/upload so csv file will be uploaded and saved in a postgres table.
This step will be redundant in the future, kept for now as starting point.

Then you can run http://127.0.0.1:8000/list/1970 to get all songs in the database for the 
decade you want.



