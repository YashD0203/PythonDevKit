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
                                               scope='user-library-read'))

# Get the user's saved tracks (Liked Songs)
results = sp.current_user_saved_tracks(limit=10)  # Limit to top 10 songs

# Print the top 10 liked songs
for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx + 1}. {track['artists'][0]['name']} - {track['name']}")
