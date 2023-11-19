from googleapiclient.discovery import build
import csv
import os
from dotenv import load_dotenv
import time
import subprocess

startTime = time.time()

# Loads the environment variables :
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Extracts username from link to channel :
def extract_username(link):
   return link.replace('https://www.youtube.com/@', '')

link = input("Enter link to the Channel : ")
username = extract_username(link)
print(username)

# Extracts channel_id from url and username :
from googleapiclient.discovery import build

def get_channel_id(GOOGLE_API_KEY, username):
   youtube = build('youtube', 'v3', developerKey=GOOGLE_API_KEY)

   request = youtube.search().list(
       part="snippet",
       type="channel",
       q=username,
       fields="items(id(channelId))"
   )
   response = request.execute()

   if response['items']:
       return response['items'][0]['id']['channelId']
   else:
       return None

channel_id = get_channel_id(GOOGLE_API_KEY, username)

# Queries the API and retrieves the required info :
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

# Names the file :
csv_filename = f"{username}.csv"

# Parses the retrieved values onto the .csv file :
urls = get_channel_videos(GOOGLE_API_KEY, channel_id)
save_to_csv(csv_filename, urls)

# Measures time to completion :
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

# Run the second script from within the first script and pass the arguments
# subprocess.run(["python", "multi_yt_arc.py", username, csv_filename])


''' OLDER CODE 1.0 :

#channel_id = input("Enter the Channel ID : ")
#api_key = input("Enter API KEY : ")

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
#channel_id = input("Enter the Channel ID : ")
#api_key = input("Enter API KEY : ")
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