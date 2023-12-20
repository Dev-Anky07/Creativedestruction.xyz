import assemblyai as aai
import os
import datetime
import webvtt
from dotenv import load_dotenv
import time
import csv

load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')
aai.settings.api_key = ASSEMBLYAI_API_KEY

username = input("Enter username : ")
csv_filename = f"{username}.csv"

with open(csv_filename, "r") as file:
  csv_reader = csv.reader(file)
  next(csv_reader)
  for row in csv_reader:
      spaces_id = row[1]
      title = row[2]
      
      # Skip if spaces_id is None or empty
      if spaces_id is None or spaces_id == '':
         continue

      startTime = time.time()

      audio_url = f"./archive/twitter/{username}/{spaces_id}/{spaces_id}.mp3"

      if not os.path.exists(audio_url):
        print(f"File {spaces_id}.mp3 not found")
        continue

      unga = f"./archive/twitter/{username}/{spaces_id}/transcript.txt"
       
      if os.path.exists(unga):
        print(f"Summary File exists already")
        continue

      config = aai.TranscriptionConfig(speaker_labels=True)
      transcript = aai.Transcriber().transcribe(audio_url, config)
      #print(transcript.text)
      print("Transcribed " + str(spaces_id) + " : " + str(title) + " Sucessfully 🎉✨")
      executionTime = (time.time() - startTime)
      print('Execution time in seconds: ' + str(executionTime))

      def convert_ms_to_time(ms):
         seconds = ms / 1000
         time = datetime.timedelta(seconds=seconds)
         time_str = str(time)
         time_str_no_decimal = time_str.split('.')[0]
         time_str_with_zero = time_str_no_decimal + ".000"
         return time_str_with_zero

     # Check if transcript.utterances is None before iterating over it
      if transcript.utterances is None:
         print(f"No utterances found for spaces_id: {spaces_id}")
         continue

      with open(f"./archive/twitter/{username}/{spaces_id}/transcript.txt", "w") as f:
         for utterance in transcript.utterances:
             start_time = convert_ms_to_time(utterance.start)
             end_time = convert_ms_to_time(utterance.end)
             line = f"[ {start_time} ---> {end_time} ] Speaker {utterance.speaker} : {utterance.text}\n"
             f.write(line)

      vtt = webvtt.WebVTT()
      for utterance in transcript.utterances:
         start_time = convert_ms_to_time(utterance.start)
         end_time = convert_ms_to_time(utterance.end)
         caption_text = f"Speaker {utterance.speaker} : {utterance.text}"
         caption = webvtt.Caption(start_time, end_time, caption_text)
         vtt.captions.append(caption)
      vtt.save(f"./archive/twitter/{username}/{spaces_id}/transcript.vtt")
