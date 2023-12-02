import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import getpass


my_user = "ThreaToSociety2"
#my_pass = getpass.getpass() # Enter 'Anky@123'
my_pass = "Anky@123"

#from selenium.webdriver.chrome.service import Service

# Create a new service with the specified executable path
service = Service(executable_path='/Users/anky/Downloads/geckodriver')
#service = Service(executable_path='/Users/anky/Downloads/chromedriver_mac64/chromedriver')

# Create a new Firefox driver

driver = webdriver.Firefox(service=service)
#driver = webdriver.Chrome(service=service)

# Navigate to the Twitter login page
driver.get('https://twitter.com/i/flow/login')
sleep(5)

'''
# Enter your username and password
wait = WebDriverWait(driver, 10)
username = driver.find_element(By.NAME, 'session[username_or_email]')
password = driver.find_element(By.NAME, 'session[password]')
username.send_keys('ThreaToSociety2')
password.send_keys('Anky@123')
'''

username = driver.find_element(By.XPATH,"//input[@type='text']")
username.send_keys(my_user)
sleep(3)
username.send_keys(Keys.ENTER)
sleep(3)

password = driver.find_element(By.XPATH,"//input[@type='password']")
password.send_keys(my_pass)
sleep(3)
password.send_keys(Keys.ENTER)
sleep(3)

# Click the login button
#password.send_keys(Keys.RETURN)

sleep(3)
# Navigate to the tweet
driver.get('https://x.com/aaronleupp/status/1725967113377202281')

last_height = driver.execute_script("return document.body.scrollHeight")

# Initialize an empty list to store the reply contents
reply_contents = []

while True:
   # Scroll down the page to load more replies
   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   sleep(5)

   # Replace 'xpath_to_replies' with the actual XPath to the replies
   replies = driver.find_elements(By.XPATH, "(//div[@data-testid='tweetText'])[position()>1]")

   # Extract the content of each reply and append it to the list
   for reply in replies:
       reply_contents.append(reply.text)

   # Check if the page has scrolled to the bottom
   new_height = driver.execute_script("return document.body.scrollHeight")
   if new_height == last_height:
       break
   last_height = new_height

# Write the reply contents to a CSV file
import csv

with open('replies.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(["Tweet Content", "Number"])
   for i, content in enumerate(reply_contents, start=1):
       writer.writerow([content, i])


'''
# Scroll down the page to load all the replies
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)
'''

'''# Scroll down the page to load all the replies
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   sleep(5)
   new_height = driver.execute_script("return document.body.scrollHeight")
   if new_height == last_height:
       break
   last_height = new_height

# Replace 'xpath_to_replies' with the actual XPath to the replies
replies = driver.find_elements(By.XPATH, "(//div[@data-testid='tweetText'])[position()>1]")

# Extract the content of each reply
reply_contents = [reply.text for reply in replies]

# Write the reply contents to a CSV file
import csv

with open('replies.csv', 'w', newline='') as file:
 writer = csv.writer(file)
 writer.writerow(["Tweet Content", "Number"])
 for i, content in enumerate(reply_contents, start=1):
   writer.writerow([content, i])
'''
'''
# Replace 'xpath_to_replies' with the actual XPath to the replies
replies = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
#replies = driver.find_elements(By.XPATH, "//div[@type='reply']")

# Extract the content of each reply
reply_contents = [reply.text for reply in replies]

# Write the reply contents to a CSV file
import csv

with open('replies.csv', 'w', newline='') as file:
 writer = csv.writer(file)
 writer.writerow(["Tweet Content", "Number"])
 for i, content in enumerate(reply_contents, start=1):
     writer.writerow([content, i])
'''

# //div[@data-testid="reply"]

'''
from selenium import webdriver

driver = webdriver.Firefox('/Users/anky/Downloads/geckodriver')
driver.get('https://twitter.com/AjeetK/status/1729060443988046322')

replies = driver.find_elements_by_xpath('xpath_to_replies')

reply_contents = [reply.text for reply in replies]

import csv

with open('replies.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(["Tweet Content", "Number"])
   for i, content in enumerate(reply_contents, start=1):
       writer.writerow([content, i])
'''

'''
# Status code was 200, that means the program was able to fetch the page but HTML structure has changed so it's not working
import requests
from bs4 import BeautifulSoup
import csv

def scrape_tweets(url):
   response = requests.get(url)
   soup = BeautifulSoup(response.text, 'html.parser')
   tweets = soup.find_all('div', class_='tweet')
   with open('result.csv', 'w', newline='') as csvfile:
       csvWriter = csv.writer(csvfile)
       for tweet in tweets:
           csvWriter.writerow([tweet.text, 1])
           response = requests.get(url)
       print(response.status_code)


scrape_tweets('https://x.com/ThreatT0Society/status/1728779741623144809')
'''

'''
import tweepy
import csv
import time

consumer_key = "mfTH49himV1V9SkvPbeNfkWBI" #Your API/Consumer key 
consumer_secret = "FEFnzOyEqkihxrGdY4Ind11gLcPRYPupKuMAJEbDXR4tDRKxKm" #Your API/Consumer Secret Key
access_token = "1493189235314405377-AEnIQY9criDRLhNTy5YVYw9aj6upZE"  #Your Access token key
access_token_secret = "bmCK2GPa700X699grDJKwsupjwELuZs71opWRBI6he3MJ" #Your Access token Secret key

auth = tweepy.OAuth1UserHandler(
  consumer_key, consumer_secret,
  access_token, access_token_secret
)

api = tweepy.API(auth, wait_on_rate_limit=True)

user_name = "@ThreatT0Society"
tweet_id = "1728779741623144809"

# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

replies = tweepy.Cursor(api.search_tweets, q='to:{}'.format(user_name),
                            since_id=tweet_id, tweet_mode='extended').items()

while True:
 try:
   reply = replies.next()
   if not hasattr(reply, 'in_reply_to_status_id_str'):
       continue
   if str(reply.in_reply_to_status_id) == tweet_id:
      csvWriter.writerow([reply.text, 1])

 except tweepy.errors.TweepyException as e:
   print("Tweepy error occured:", e)
   break

 except StopIteration:
   break

 except Exception as e:
   print("Failed while fetching replies", e)
   break

csvFile.close()

csvFile.close()
'''