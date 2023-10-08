import spotipy
from spotipy.oauth2 import SpotifyOAuth
from langdetect import detect
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Set your Spotify API credentials
client_id = os.getenv('ID')
client_secret = os.getenv('SECRET')
redirect_uri = os.getenv('REDIRECT_URI')

# Initialize Spotipy with the necessary credentials and scope
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='playlist-modify-public'))

# Name and description for the new playlist
playlist_name = 'API Magic'
playlist_description = 'This is a new playlist created with the Spotify API.'

# Create the new playlist
playlist = sp.user_playlist_create(user='your_account_username', name=playlist_name, public=True, description=playlist_description)

# Print the ID and name of the created playlist
print(f"Playlist ID: {playlist['id']}")
print(f"Playlist Name: {playlist['name']}")
