import assemblyai as aai
import os
import datetime
import webvtt
from dotenv import load_dotenv

load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')
aai.settings.api_key = ASSEMBLYAI_API_KEY

audio_url = "Archive/Youtube/Podcasts/dz.mp3"
#audio_url = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3" # Access files uploaded over the internet or google drive

config = aai.TranscriptionConfig(
  speaker_labels=True,
  speakers_expected=2
)

transcript = aai.Transcriber().transcribe(audio_url, config)

def convert_ms_to_time(ms):
 seconds = ms / 1000 # Convert milliseconds to seconds
 time = datetime.timedelta(seconds=seconds)
 time_str = str(time)
 time_str_no_decimal = time_str.split('.')[0] # Remove the part after the decimal point
 time_str_with_zero = time_str_no_decimal + ".000" # Append ".000" to the seconds part of the time string
 return time_str_with_zero

with open("output.txt", "w") as f:

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
  vtt.save('output.vtt')

'''
CONTEXT : 

Audio_URL : If we pass a link to a youtube video, the there's no result as the utterances returned are None and it's not parsable.


'''



''' 
with open("output.txt", "w") as f:
 if transcript.utterances is not None:
  for utterance in transcript.utterances:
   start_time = convert_ms_to_time(utterance.start)
   end_time = convert_ms_to_time(utterance.end)
   caption_text = f"Speaker {utterance.speaker} : {utterance.text}"
   line = f"[ {start_time} ---> {end_time} ] Speaker {utterance.speaker} : {utterance.text}\n"
   f.write(line)
   vtt = webvtt.WebVTT()
   caption = webvtt.Caption(start_time, end_time, caption_text)
   vtt.captions.append(caption)
  vtt.save('output.vtt')
'''

'''
def convert_ms_to_time(ms):
 seconds = ms / 1000 # Convert milliseconds to seconds
 milliseconds = seconds % 1 * 1000 # Get the milliseconds
 time = datetime.timedelta(seconds=seconds, milliseconds=milliseconds)
 time_str = str(time).replace('0:', '').replace('.', ',') # Format the time string
 return time_str

vtt = webvtt.WebVTT()
for utterance in transcript.utterances:
  start_time = convert_ms_to_time(utterance.start)
  end_time = convert_ms_to_time(utterance.end)
  caption_text = f"Speaker {utterance.speaker} : {utterance.text}"
  caption = webvtt.Caption(start_time, end_time, caption_text)
  vtt.captions.append(caption)
  vtt.save('output.vtt')

vtt = webvtt.WebVTT()
for utterance in transcript.utterances:
 start_time = convert_ms_to_time(utterance.start)
 end_time = convert_ms_to_time(utterance.end)
 #print(f"{start_time} ---> {end_time} Speaker {utterance.speaker} : {utterance.text}")
 caption = webvtt.Caption(start_time, end_time, utterance.text)
 vtt.captions.append(caption)
vtt.save('output.vtt')

for utterance in transcript.utterances:
  start_time = convert_ms_to_time(utterance.start)
  end_time = convert_ms_to_time(utterance.end)
  print(f"{start_time} ---> {end_time} Speaker {utterance.speaker} : {utterance.text}")
'''