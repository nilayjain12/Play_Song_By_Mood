import mutagen

def get_mp3_metadata(mp3_file_path):
    try:
        audio = mutagen.File(mp3_file_path, easy=True)
        if audio:
            # Extract the media properties
            media = {
                'title': audio.get('title', ''),
                'artist': audio.get('artist', ''),
                'album': audio.get('album', ''),
                'genre': audio.get('genre', ''),
                'duration': audio.info.length,
                # Add more properties as needed
            }
            return media
        else:
            print("Failed to read MP3 file.")
            return None, None
    except Exception as e:
        print(f"Error extracting MP3 metadata: {e}")
        return None, None

# Example usage:
mp3_file_path = r'C:\Users\14089\Desktop\NILAY JAIN\Personal Projects\PlaySongByMood\SongsList\DownloadedSongs\Aaj Ke Baad Reprise.mp3'
media = get_mp3_metadata(mp3_file_path)
    
if media is not None:
    name = media['title'][0]
    name = name[:name.index('[')]
    artist = media['artist'][0]
    artist = artist[:artist.index('[')]
else:
    print("No media information found.")