import yt_dlp
from urllib.parse import urlparse, parse_qs
import os
import csv

def get_video_code(url):
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
    return None

def download_audio(user_tag, csv_filename):
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            url = row[0]  # Assuming the URL is in the first column
            video_code = get_video_code(url)
            video_id = row[1]

            if video_id is None or video_id == '':
               print(f"Invalid video_id: {video_id}")
               continue
            if video_code is not None:
                output_dir = f"./archive/youtube/{user_tag}/{video_id}"
                os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
                output_filename = f"{output_dir}/{video_code}"
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': output_filename,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
            else:
                print(f"Invalid YouTube URL: {url}")

# Use the function
user_tag = input("Enter the user tag: ")
csv_filename = f"{user_tag}.csv"
download_audio(user_tag, csv_filename)

print("Archived all files from " + str(user_tag) + " Successfully 🎉✨")

'''
import yt_dlp
from urllib.parse import urlparse, parse_qs
import os

def get_video_code(url):
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
    return None

def download_audio(user_tag, urls):
    for url in urls:
        video_code = get_video_code(url)
        if video_code is not None:
            output_dir = f"./archive/youtube/{user_tag}"
            os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
            output_filename = f"{output_dir}/{video_code}.mp3"
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': output_filename,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        else:
            print(f"Invalid YouTube URL: {url}")

# Use the function
user_tag = input("Enter the user tag: ")
urls = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=3tmd-ClpJxA']
download_audio(user_tag, urls)
'''