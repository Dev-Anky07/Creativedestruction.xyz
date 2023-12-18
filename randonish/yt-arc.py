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

def download_audio():
    url = input("Enter the YouTube video URL: ")
    user_tag = input("Enter the user tag: ")
    video_code = get_video_code(url)
    if video_code is not None:
        output_dir = f"./archive/youtube/{user_tag}"
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
        print("Invalid YouTube URL.")

# Use the function
download_audio()

# youtube link : https://www.youtube.com/watch?v=35lS7gJVTyA

# Older Code : Without Saving the file in a specific repo
'''import yt_dlp
from urllib.parse import urlparse, parse_qs

def get_video_code(url):
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
    return None

def download_audio():
    url = input("Enter the YouTube video URL: ")
    video_code = get_video_code(url)
    if video_code is not None:
        output_filename = f"{video_code}"
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_filename,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }, {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    else:
        print("Invalid YouTube URL.")

# Use the function
download_audio()'''
