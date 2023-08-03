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

# adding the heading of the features in the csv file
with open('play_song_by_mood.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['song_name', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'mood'])

file_path = r'C:\Users\14089\Desktop\NILAY JAIN\Personal Projects\Play_Song_By_Mood\SongsList\DownloadedSongs'

for file_name in os.listdir(file_path):
    complete_path = os.path.join(file_path, file_name)
    
    file_name = file_name[:file_name.index('.')]
    results = sp.search(q=f'track:{file_name}', type='track', limit=1)

#     # extracting metadata of a song, 'artist name', 'album name'
#     track_metadata = sample.get_mp3_metadata(complete_path)
#     try:
#           track_metadata_album = track_metadata['album'][0]
#     except:
#           continue
#     try:
#         track_metadata_album = track_metadata_album[:track_metadata_album.index('[')].strip().lower()
#     except:
#           continue
#     track_metadata_artist = track_metadata['artist'][0]
#     try:
#         track_metadata_artist = track_metadata_artist[:track_metadata_artist.index('[')].lower()
#     except:
#           continue

    # extracting track artist and track album name from spotify api
    try:
          track_name = results['tracks']['items'][0]['name']
          track_name = track_name[:track_name.index('(')]
    except:
          track_name = track_name

#     try:
#           track_artist = results['tracks']['items'][0]['artists']
#     except:
#           continue
#     track_album = results['tracks']['items'][0]['album']['name'].lower()

#     # validation for artist and album
#     if track_album in track_metadata_album:
#         for elem in track_artist:
#             dict_artist_name = elem['name'].lower()
#             if dict_artist_name in track_metadata_artist:

    if track_name.strip().lower() in file_name.strip().lower() or file_name.strip().lower() in track_name.strip().lower():

            track_id = results['tracks']['items'][0]['id']
            #call spotify api to using track_id and extract features of song and store it in csv
            track_features = sp.audio_features(track_id)

            # extracting features of current song
            danceability = track_features[0]['danceability']
            energy = track_features[0]['energy']
            key = track_features[0]['key']
            loudness = track_features[0]['loudness']
            mode = track_features[0]['mode']
            speechiness = track_features[0]['speechiness']
            acousticness = track_features[0]['acousticness']
            liveness = track_features[0]['liveness']
            valence = track_features[0]['valence']
            tempo = track_features[0]['tempo']
            duration_ms = track_features[0]['duration_ms']
            time_signature = track_features[0]['time_signature']

            # initial check to sort songs in happy or sad
            if (danceability + energy + valence)/3 >= 0.60:
                  category = 'Happy'
            else:
                  category = 'Relaxed'

            # add details to csv
            with open('play_song_by_mood.csv', 'a', newline='') as csvfile:
                  writer = csv.writer(csvfile)
                  writer.writerow([file_name, danceability, energy, key, loudness, mode, speechiness, acousticness, liveness, valence, tempo, duration_ms, time_signature, category])
            
                


# track_id = results['tracks']['items'][0]['id']
# track_artist = results['tracks']['items'][0]['artists']

# print(track_id)
# print(track_artist)
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

