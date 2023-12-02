from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

my_user = "ThreaToSociety2"
my_pass = "Anky@123"

service = Service(executable_path='/Users/anky/Downloads/geckodriver')

driver = webdriver.Firefox(service=service)

driver.get('https://twitter.com/i/flow/login')
time.sleep(5)

username = driver.find_element(By.XPATH,"//input[@type='text']")
username.send_keys(my_user)
time.sleep(3)
username.send_keys(Keys.ENTER)
time.sleep(3)

password = driver.find_element(By.XPATH,"//input[@type='password']")
password.send_keys(my_pass)
time.sleep(3)
password.send_keys(Keys.ENTER)
time.sleep(3)

time.sleep(3)


driver.get('https://twitter.com/ApeComms') # replace 'john' with the username you want to scrape

last_height = driver.execute_script("return document.body.scrollHeight")

#tweet_contents = []
tweet_links = []

while True:
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(5)

  tweets = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweet"]')

  for tweet in tweets:
      #content = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]').text
      link = tweet.find_element(By.CSS_SELECTOR, 'a[href]').get_attribute('href')
      #tweet_contents.append(content)
      tweet_links.append(link)

  new_height = driver.execute_script("return document.body.scrollHeight")
  if new_height == last_height:
      break
  last_height = new_height

with open('tweets.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  #writer.writerow(["Tweet Content", "Tweet Link"])
  writer.writerow(["Tweet Link"])
  for content, link in zip(tweet_links):
      writer.writerow([link])





''' v1.2 : Use tweepy and Twitter's api to scrpae the last 100 tweets links and 

import tweepy
import pandas as pd

consumer_key = "XXXX" #Your API/Consumer key 
consumer_secret = "XXXX" #Your API/Consumer Secret Key
access_token = "XXXX"   #Your Access token key
access_token_secret = "XXXX" #Your Access token Secret key

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret,
   access_token, access_token_secret
)

api = tweepy.API(auth, wait_on_rate_limit=True)
username = "john"
no_of_tweets = 100
tweets = api.user_timeline(screen_name=username, count=no_of_tweets)

import re

spaces_tweets = [tweet for tweet in tweets if re.search(r'https://twitter.com/i/spaces/1', tweet.text)]

spaces_df = pd.DataFrame([[tweet.created_at, tweet.text] for tweet in spaces_tweets], columns=["Date Created", "Tweet"])

spaces_df.to_csv('spaces.csv', index=False)


'''









''' v1.1 : Using twitter api basic version -> Can scrape your posts
import requests
import pandas as pd


bearer_token = "YOUR_BEARER_TOKEN"
headers = {"Authorization": "Bearer {}".format(bearer_token)}

response = requests.get("https://api.twitter.com/2/spaces/search", headers=headers)
spaces = response.json()

links_and_titles = [(space['url'], space['title']) for space in spaces['data']]
df = pd.DataFrame(links_and_titles, columns=["Link", "Title"])
df.to_csv('spaces.csv', index=False)
'''

''' v1.0 : Without Twiter's API
import snscrape.modules.twitter as sntwitter
import pandas as pd

attributes_container = []
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:@ThreatT0Society').get_items()):
   if i>100:
       break
   attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])

tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
tweets_df.to_csv('tweets.csv', index=False)
'''