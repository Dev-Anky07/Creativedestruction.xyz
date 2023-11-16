from googleapiclient.discovery import build
import csv
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

channel_id = input("Enter the Channel ID : ")
#api_key = input("Enter API KEY : ")

# Don't forget to change the max_results parameter accordingly

def get_channel_videos(GOOGLE_API_KEY, channel_id, max_results=50):
   youtube = build('youtube', 'v3', developerKey=GOOGLE_API_KEY)

   request = youtube.search().list(
       part="id,snippet",
       channelId=channel_id,
       maxResults=max_results,
       fields="items(id(videoId,videoId),snippet(publishedAt,title,description))"
   )
   response = request.execute()

   return [(f"https://www.youtube.com/watch?v={item['id'].get('videoId')}", item['id'].get('videoId') , item['snippet'].get('publishedAt'), item['snippet'].get('title') , item['snippet'].get('description')) for item in response['items']]

def save_to_csv(filename, urls):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["url", "video_id", "upload_time", "title", "description"])
        for url, video_id, upload_time, title, description in urls:
            writer.writerow([url, video_id, upload_time, title, description])

# Use the functions
csv_filename = f"{channel_id}.csv"

urls = get_channel_videos(GOOGLE_API_KEY, channel_id)
save_to_csv(csv_filename, urls)


''' OLDER CODE 1.0 :

from googleapiclient.discovery import 
import csv

def get_channel_videos(api_key, channel_id, max_results=50):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        maxResults=max_results,
        fields="items(id(videoId))"
    )
    response = request.execute()

    return [f"https://www.youtube.com/watch?v={item['id']['videoId']}" for item in response['items']]

def save_to_csv(filename, urls):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["url"])
        for url in urls:
            writer.writerow([url])

# Use the functions
api_key = "YOUR_API_KEY"
channel_id = "CHANNEL_ID"
csv_filename = f"{channel_id}.csv"

urls = get_channel_videos(api_key, channel_id)
save_to_csv(csv_filename, urls)
'''

''' OLDER CODE 2.0 : 
 def get_channel_videos(api_key, channel_id, max_results=50):
    youtube = build('youtube', 'v3', developerKey = GOOGLE_API_KEY)

    request = youtube.search().list(
        part="id,snippet",
        channelId=channel_id,
        maxResults=max_results,
        fields="items(id(videoId),snippet(publishedAt,description))"
    )
    response = request.execute()

    return [(f"https://www.youtube.com/watch?v={item['id']['videoId']}", item['snippet']['publishedAt'], item['snippet']['description']) for item in response['items']]'''