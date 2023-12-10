import tweepy
import os
from dotenv import load_dotenv

load_dotenv()
consumer_key = os.getenv('') #Your API/Consumer key 
consumer_secret = os.getenv('') #Your API/Consumer Secret Key
access_token = os.getenv('') #Your Access token key
access_token_secret = os.getenv('') #Your Access token Secret key

username = input("Enter the username: ")
spaces_id = input("Enter the spaces_id: ")


auth = tweepy.OAuth1UserHandler(
 consumer_key, consumer_secret,
 access_token, access_token_secret
)

api = tweepy.API(auth, wait_on_rate_limit=True)

# The ID of the tweet you're replying to
in_reply_to_status_id = "tweet_id"

# The text of your reply
status = "This is a reply to a tweet."

# Post the reply
api.update_status(status=status, in_reply_to_status_id=in_reply_to_status_id)

from pathlib import Path

file_path = Path(f'./archive/youtube/{username}/{spaces_id}/summary.txt')
with file_path.open() as file:
   summary = file.read()

'''
Changes I want to make :
1) Ask for link as well, extract tweet id
2) Segment the summary into digestible byte sized chunks using the GPT open ai api (using the credits you have)
3) Add no hashtags in the tweet : The phind is open on brave

'''