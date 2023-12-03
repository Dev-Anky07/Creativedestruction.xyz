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
      spaces_id = row[1]
      
      # Skip if video_id is None or empty
      if spaces_id is None or spaces_id == '':
         continue
      url = "r.https://twitter.com/i/spaces/{spaces_id}"

      directory = f'./archive/twitter/{username}/{spaces_id}'
      os.makedirs(directory, exist_ok=True)

      # Download the Twitter space
      subprocess.run(['twspace_dl', '-i', url, '-c', 'cookies.txt', '-o', f'{directory}{spaces_id}'])
      time.sleep(10)


with open(csv_filename, "r") as file:
  csv_reader = csv.reader(file)
  next(csv_reader)
  for row in csv_reader:
      spaces_id = row[1]
      
      # Skip if video_id is None or empty
      if spaces_id is None or spaces_id == '':
         continue

      directory = f'./archive/twitter/{username}/{spaces_id}'
      os.makedirs(directory, exist_ok=True)

      # Convert the m4a file to mp3 format
      subprocess.run(['ffmpeg', '-i', f'{directory}/{spaces_id}.m4a', '-codec:a', 'libmp3lame', '-qscale:a', '2', f'{directory}/{spaces_id}.mp3'])
      time.sleep(10)





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


'''# Open the CSV file
with open(csv_filename, "r") as file:
  csv_reader = csv.reader(file)
  for row in csv_reader:
      video_id = row[1]
      if video_id is not None:
          # Rest of your code here...
          pass
      else:
          continue

  # Add a delay of 60 seconds
  time.sleep(60)
'''

'''import os
import re
import subprocess

# Ask for the URL
url = input("Enter the URL of the Twitter space: ")

# Extract the Space ID
space_id = re.search(r'https://twitter.com/i/spaces/(.*)', url).group(1)

# Ask for the user tag
user_tag = input("Enter the user tag: ")

# Create the directory if it doesn't exist
directory = f'./archive/twitter/{user_tag}/'
os.makedirs(directory, exist_ok=True)

# Download the Twitter space
subprocess.run(['twspace_dl', '-i', url, '-c', 'cookies.txt', '-o', f'{directory}{space_id}.mp3'])

# link to a space : https://twitter.com/i/spaces/1YqGoDqVbyMJv?s=20'''