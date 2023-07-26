import os
import csv
import mutagen
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import base64
# Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your Spotify API credentials
client_id = '5e72cefadf2242f185811400e85ae9cf'
client_secret = '7353a65633624c60996996693beba8e5'

credentials = f"{client_id}:{client_secret}"
credentials_b64_encode = base64.b64encode(credentials.encode())
credentials_b64_deencode = credentials_b64_encode.decode()

# Create a Spotipy client with credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

DIRECTORY = os.path.join(r'C:\Users\14089\Desktop\NILAY JAIN\Personal Projects\PlaySongByMood\SongsList\DownloadedSongs')
CATEGORIES = ["Hindi Happy", "Hindi Sad"]

# adding the heading of the features in the csv file
with open('play_song_by_mood.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['song_name', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'mood'])

'''def get_audio_metadata(audio_path):
    try:
        audio = mutagen.File(audio_path, easy=True)
        metadata = audio.info
        return metadata
    except Exception as e:
        print(f"Error extracting audio metadata: {e}")
        return None'''

for song_name in os.listdir(DIRECTORY):
        
        break
        

# for category in CATEGORIES:
#     path = os.path.join(DIRECTORY, category) # path to Hindi Happy and Hindi Sad
#     for song_name in os.listdir(path):
#         print("Processing song : ", song_name)
#         '''code to get the features of the a song using spotipy api'''

#         # Search for the song using the Spotify API
#         results = sp.search(q=f'track:{song_name}', type='track')

#         print("Response from Spotify for song : ", song_name, " is : ", results)

#         # Get the first result (top match) from the search
#         if results['tracks']['items']:
#             track = results['tracks']['items'][0]

#             # Get the track ID
#             track_id = track['id']

#             # Get the audio features of the track
#             track_features = sp.audio_features(track_id)

#             if track_features:
#                 # Extract the features
#                 danceability = track_features[0]['danceability']
#                 energy = track_features[0]['energy']
#                 key = track_features[0]['key']
#                 loudness = track_features[0]['loudness']
#                 mode = track_features[0]['mode']
#                 speechiness = track_features[0]['speechiness']
#                 acousticness = track_features[0]['acousticness']
#                 instrumentalness = track_features[0]['instrumentalness']
#                 liveness = track_features[0]['liveness']
#                 valence = track_features[0]['valence']
#                 tempo = track_features[0]['tempo']
#                 duration_ms = track_features[0]['duration_ms']
#                 time_signature = track_features[0]['time_signature']
            
#             with open('play_song_by_mood.csv', 'a', newline='') as csvfile:
#                 writer = csv.writer(csvfile)
#                 writer.writerow([song_name, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, time_signature, category])
