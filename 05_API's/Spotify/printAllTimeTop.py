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

# Initialize Spotipy with the necessary credentials and scope
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='user-top-read'))

# Get the user's top 10 tracks of all time
top_tracks = sp.current_user_top_tracks(limit=10, time_range='long_term')

# Print the top 10 tracks
if top_tracks:
    print("Your top 10 tracks of all time:")
    for idx, track in enumerate(top_tracks['items']):
        print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")
else:
    print("No top tracks found.")
