# Summarization 

import time
import assemblyai as aai
import os
from dotenv import load_dotenv

load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')

aai.settings.api_key = ASSEMBLYAI_API_KEY

startTime = time.time()

audio_url = "Archive/Youtube/Podcasts/download.mp3"

config = aai.TranscriptionConfig(
  summarization=True,
  summary_model=aai.SummarizationModel.informative,
  summary_type=aai.SummarizationType.bullets_verbose
)

transcript = aai.Transcriber().transcribe(audio_url, config)

print(transcript.summary)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))