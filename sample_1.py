import os
import csv
import mutagen
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import base64
import sample


# Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your Spotify API credentials
client_id = '5e72cefadf2242f185811400e85ae9cf'
client_secret = '7353a65633624c60996996693beba8e5'

# Create a Spotipy client with credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

file_path = r'C:\Users\14089\Desktop\NILAY JAIN\Personal Projects\PlaySongByMood\SongsList\DownloadedSongs'

for file_name in os.listdir(file_path):
    complete_path = os.path.join(file_path, file_name)
    
    file_name = file_name[:file_name.index('.')]
    results = sp.search(q=f'track:{file_name}', type='track', limit=1)

    track_metadata = sample.get_mp3_metadata(complete_path)
    track_metadata_artist = track_metadata['artist'][0]
    track_metadata_artist = track_metadata_artist[:track_metadata_artist.index('[')]

    track_artist = results['tracks']['items'][0]['artists']
    for elem in track_artist:
        dict_artist_name = elem['name']
        if dict_artist_name in track_metadata_artist:
            track_id = elem['id']
    


track_id = results['tracks']['items'][0]['id']
track_artist = results['tracks']['items'][0]['artists']

print(track_id)
print(track_artist)
# print(track_id)
# print(track_artist)


# track_features = sp.audio_features(track_id)

# danceability = track_features[0]['danceability']
# energy = track_features[0]['energy']
# key = track_features[0]['key']
# loudness = track_features[0]['loudness']
# mode = track_features[0]['mode']
# speechiness = track_features[0]['speechiness']
# acousticness = track_features[0]['acousticness']
# instrumentalness = track_features[0]['instrumentalness']
# liveness = track_features[0]['liveness']
# valence = track_features[0]['valence']
# tempo = track_features[0]['tempo']
# duration_ms = track_features[0]['duration_ms']
# time_signature = track_features[0]['time_signature']

