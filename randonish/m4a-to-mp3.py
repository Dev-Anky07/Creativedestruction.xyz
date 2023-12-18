import os
import subprocess
import csv
import time

username = input("Enter username : ")
csv_filename = f"{username}.csv"

with open(csv_filename, "r") as file:
  csv_reader = csv.reader(file)
  next(csv_reader)
  for row in csv_reader:
      url = row[0]
      spaces_id = row[1]
      
      # Skip if video_id is None or empty
      if spaces_id is None or spaces_id == '':
         continue

      directory = f'./archive/twitter/{username}/{spaces_id}'
      os.makedirs(directory, exist_ok=True)

      # Convert the m4a file to mp3 format
      subprocess.run(['ffmpeg', '-i', f'{directory}/{spaces_id}.m4a', '-codec:a', 'libmp3lame', '-qscale:a', '2', f'{directory}/{spaces_id}.mp3'])
      time.sleep(10)