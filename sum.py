import csv
import os
import assemblyai as aai
from urllib.parse import urlparse, parse_qs
import csv
from dotenv import load_dotenv
import time

load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')

aai.settings.api_key = ASSEMBLYAI_API_KEY

username = input("Enter Username : ")
#csv_filename = input("Enter csv file name : ")
csv_filename = f"{username}.csv"

with open(csv_filename, "r") as file:
   csv_reader = csv.reader(file)
   next(csv_reader)
   for row in csv_reader:
       video_id = row[1]
       title = row[3]
       if video_id is None or video_id == '': # if video_id is not None:
         continue
       
       audio_url = f"./archive/youtube/{username}/{video_id}/{video_id}.mp3"

       config = aai.TranscriptionConfig(
           summarization=True,
           summary_model=aai.SummarizationModel.informative,
           summary_type=aai.SummarizationType.bullets_verbose
       )

       transcript = aai.Transcriber().transcribe(audio_url, config)
       print("Summarized " + str(video_id) + " : " + str(title))
       # print("Summarized " + str(video_id)) # print("Summarized " + str(video_id) + " : " + str(title))

       # Create the directory if it doesn't exist
       output_dir = f"./archive/youtube/{username}/{video_id}"
       if not os.path.exists(output_dir):
                 os.makedirs(output_dir)
       with open(f"./archive/youtube/{username}/{video_id}/summary.txt", "w") as file:
         if transcript.summary is not None:
           file.write(transcript.summary)
         else:



          print("Summarized all files from " + str(username) + " Successfully 🎉✨")

''' 
import time
import assemblyai as aai
import os
from dotenv import load_dotenv

load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')

aai.settings.api_key = ASSEMBLYAI_API_KEY

username = input("Enter Username : ")
video_id = input("Enter Video ID : ")

startTime = time.time()

audio_url = f"./archive/youtube/{username}/{video_id}.mp3"

config = aai.TranscriptionConfig(
  summarization=True,
  summary_model=aai.SummarizationModel.informative,
  summary_type=aai.SummarizationType.bullets_verbose
)

transcript = aai.Transcriber().transcribe(audio_url, config)

# Create the directory if it doesn't exist
output_dir = f"./archive/youtube/{username}/{video_id}"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(f"./archive/youtube/{username}/{video_id}/summary.txt", "w") as file:
    file.write(transcript.summary)

print(transcript.summary)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
'''