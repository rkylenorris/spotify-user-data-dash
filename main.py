import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
import os

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri='https://127.0.0.1:8888/callback',
    scope='user-top-read user-read-recently-played'
))

top_artists = sp.current_user_top_artists(limit=10, time_range='short_term')

if top_artists:
    for artist in top_artists['items']:
        print(f"Artist: {artist['name']}")
        print(f"Followers: {artist['followers']['total']}")
        print(f"Popularity: {artist['popularity']}")
        print(f"Genres: {', '.join(artist['genres']) if artist['genres'] else 'No genres available'}")
        print("-" * 40)
else:
    print("No top artists found.")
