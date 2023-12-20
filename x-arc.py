import os
import re
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
      title = row[2]
      
      # Skip if video_id is None or empty
      if spaces_id is None or spaces_id == '':
         continue

      startTime = time.time()
      directory = f'./archive/twitter/{username}/{spaces_id}'
      unga = f'./archive/twitter/{username}/{spaces_id}/{spaces_id}.mp3'
      os.makedirs(directory, exist_ok=True)

      if os.path.exists(unga):
        print(f"File : {spaces_id}.mp3 already exists")
        continue
      # Download the Twitter space
      subprocess.run(['twspace_dl', '-i', url, '-c', 'cookies.txt', '-o', f'{directory}/{spaces_id}']) # subprocess.run(['twspace_dl', '-i', url, '-c', 'cookies.txt', '-o', f'{directory}{spaces_id}']) 
      time.sleep(10)
      # Convert the m4a file to mp3 format
      subprocess.run(['ffmpeg', '-i', f'{directory}/{spaces_id}.m4a', '-codec:a', 'libmp3lame', '-qscale:a', '2', f'{directory}/{spaces_id}.mp3'])
      time.sleep(10)
      print("Transcribed " + str(spaces_id) + " : " + str(title) + " Sucessfully 🎉✨")
      executionTime = (time.time() - startTime)
      print('Execution time in seconds: ' + str(executionTime))

'''
# Ask for the URL
url = input("Enter the URL of the Twitter space : ")

# Extract the Space ID
space_id = re.search(r'https://twitter.com/i/spaces/(.*)', url).group(1)

# Ask for the user tag
user_tag = input("Enter the user tag : ")
space_id = re.search(r'https://twitter.com/i/spaces/(.*)', url).group(1)

# Ask for the CSV filename
# csv_filename = input("Enter the name of the CSV file: ")

# Create the directory if it doesn't exist
directory = f'./archive/twitter/{user_tag}/{space_id}'
os.makedirs(directory, exist_ok=True)

# Download the Twitter space
subprocess.run(['twspace_dl', '-i', url, '-c', 'cookies.txt', '-o', f'{directory}{space_id}'])
# Convert the m4a file to mp3 format
subprocess.run(['ffmpeg', '-i', f'{directory}/{space_id}.m4a', '-codec:a', 'libmp3lame', '-qscale:a', '2', f'{directory}/{space_id}.mp3'])

'''

'''
# Ask for the URL
url = input("Enter the URL of the Twitter space : ")

# Extract the Space ID
space_id = re.search(r'https://twitter.com/i/spaces/(.*)', url).group(1)

# Ask for the user tag
user_tag = input("Enter the user tag : ")
space_id = re.search(r'https://twitter.com/i/spaces/(.*)', url).group(1)

# Ask for the CSV filename
# csv_filename = input("Enter the name of the CSV file: ")

# Create the directory if it doesn't exist
directory = f'./archive/twitter/{user_tag}/{space_id}'
os.makedirs(directory, exist_ok=True)

# Download the Twitter space
subprocess.run(['twspace_dl', '-i', url, '-c', 'cookies.txt', '-o', f'{directory}{space_id}'])
# Convert the m4a file to mp3 format
subprocess.run(['ffmpeg', '-i', f'{directory}/{space_id}.m4a', '-codec:a', 'libmp3lame', '-qscale:a', '2', f'{directory}/{space_id}.mp3'])
---

username = input("Enter username : ")
csv_filename = f"{username}.csv"

with open(csv_filename, "r") as file:
  csv_reader = csv.reader(file)
  next(csv_reader)
  for row in csv_reader:
      spaces_id = row[1]
      
      # Skip if video_id is None or empty
      if spaces_id is None or spaces_id == '':
         continue
      url = "r.https://twitter.com/i/spaces/{spaces_id}"

      directory = f'./archive/twitter/{username}/{spaces_id}'
      os.makedirs(directory, exist_ok=True)

      # Download the Twitter space
      subprocess.run(['twspace_dl', '-i', url, '-c', 'cookies.txt', '-o', f'{directory}{space_id}'])

      # Convert the m4a file to mp3 format
      subprocess.run(['ffmpeg', '-i', f'{directory}/{space_id}.m4a', '-codec:a', 'libmp3lame', '-qscale:a', '2', f'{directory}/{space_id}.mp3'])

'''