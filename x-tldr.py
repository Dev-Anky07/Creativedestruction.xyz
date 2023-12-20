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
       spaces_id = row[1]
       title = row[2]
       if spaces_id is None or spaces_id == '': # if spaces_id is not None:
         continue
       
       startTime = time.time()
       audio_url = f"./archive/twitter/{username}/{spaces_id}/{spaces_id}.mp3"
       
       
       if not os.path.exists(audio_url):
        print(f"File {spaces_id}.mp3 not found")
        continue
       
       unga = f"./archive/twitter/{username}/{spaces_id}/tldr.txt"
       
       if os.path.exists(unga):
        print(f"Summary File exists already")
        continue

       config = aai.TranscriptionConfig(
           summarization=True,
           summary_model=aai.SummarizationModel.informative,
           #summary_model=aai.SummarizationModel.conversational,
           summary_type=aai.SummarizationType.bullets
       )

       transcript = aai.Transcriber().transcribe(audio_url, config)
       print("TLDR'd " + str(spaces_id) + " : " + str(title) + " Sucessfully 🥳")
       executionTime = (time.time() - startTime)
       print('Execution time in seconds: ' + str(executionTime))

       # Create the directory if it doesn't exist
       output_dir = f"./archive/twitter/{username}/{spaces_id}"
       if not os.path.exists(output_dir):
                 os.makedirs(output_dir)
       with open(f"./archive/twitter/{username}/{spaces_id}/tldr.txt", "w") as file:
         if transcript.summary is not None:
           file.write(transcript.summary)
         else:
          print("Error Processing file : " + str(spaces_id) + " : Error 404 : Retrying ")


print("TLDR'd all files from " + str(username) + " Successfully 🎉✨")
