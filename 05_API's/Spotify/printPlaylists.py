import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Set your Spotify API credentials
client_id = os.getenv('ID')
client_secret = os.getenv('SECRET')
redirect_uri = os.getenv('REDIRECT_URI')

# Initialize Spotipy with the necessary credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='playlist-read-private'))

# Get the user's playlists
playlists = sp.current_user_playlists()

# Print the names of the playlists
for playlist in playlists['items']:
    print(playlist['name'])
    