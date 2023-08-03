import requests
import random
import time
from bs4 import BeautifulSoup
import os
import threading
import re

def sanitize_song_name(song_name):
    # Remove numeric values from the song name
    song_name = re.sub(r'\d+', '', song_name)

    # Add spaces between each word
    song_name = re.sub(r'\W+', ' ', song_name)

    # Remove leading and trailing spaces
    song_name = song_name.strip()

    # Remove 'Kbps' from the end of the song name
    song_name = song_name.replace('Kbps', '').strip()

    return song_name

def download_song(url, save_directory):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        filename = url.split('/')[-1]
        song_name, _ = os.path.splitext(filename)  # Get the song name without extension
        song_name = sanitize_song_name(song_name)
        file_path = os.path.join(save_directory, f"{song_name}.mp3")

        # Check if the file already exists in the save_directory
        if os.path.exists(file_path):
            print(f"Skipped: {filename}, already downloaded.")
        else:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {filename}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

def crawl_songs(url, num_songs_to_crawl, save_directory):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        song_links = soup.find_all('a', href=True)

        count = 0
        download_threads = []
        for link in song_links:           
            href = link.get('href')
            if "music" in href:
                response1 = requests.get(href)
                response1.raise_for_status()

                soup1 = BeautifulSoup(response1.text, 'html.parser')
                song_links1 = soup1.find_all('a', href=True)
                print("Downloaded till now : ", count)
                

                for newLink in song_links1:
                    if count >= num_songs_to_crawl:
                        break
                    href1 = newLink.get('href')
                    if href1 and href1.endswith('.mp3') and '320%20Kbps' not in href1:
                        print("Downloading : ", href1)
                        download_url = href1.strip()  # Fix this line, it was using 'href' instead of 'href1'
                        
                        # Start a new thread for each download
                        download_thread = threading.Thread(target=download_song, args=(download_url, save_directory))
                        download_thread.start()
                        download_threads.append(download_thread)

                        count += 1

            # Introduce jitter by adding random delays between 1 to 5 seconds
            time.sleep(random.uniform(3, 10))

        # Wait for all download threads to finish
        for thread in download_threads:
            thread.join()

    except Exception as e:
        print(f"Error crawling songs: {e}")

if __name__ == "__main__":
    base_url = "https://pagalfree.com/"  # Replace with the actual website URL
    num_songs_to_crawl = 200
    save_directory = r'C:\Users\14089\Desktop\NILAY JAIN\Personal Projects\Play_Song_By_Mood\SongsList\DownloadedSongs'   # Replace with the directory where you want to save the songs

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    crawl_songs(base_url, num_songs_to_crawl, save_directory)
