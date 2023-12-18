import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#my_user = "ThreaToSociety2"
my_user = "ThreatT0Society"
my_pass = "Anky@123"

'''

my_user = "ThreatT0Society"

my_pass = "Anky007cj@123"

'''

# Create a new service with the specified executable path
service = Service(executable_path='/Users/anky/Downloads/geckodriver')

# Create a new Firefox driver
driver = webdriver.Firefox(service=service)


# Navigate to the Twitter login page
driver.get('https://twitter.com/i/flow/login')
sleep(5)

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

# Navigate to the tweet
driver.get('https://x.com/aaronleupp/status/1725967113377202281')

last_height = driver.execute_script("return document.body.scrollHeight")

# Initialize an empty list to store the reply contents

reply_contents = []
username_contents = []

while True:
   # Scroll down the page to load more replies
   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   sleep(5)

   # Replace 'xpath_to_replies' with the actual XPath to the replies
   replies = driver.find_elements(By.XPATH, "(//div[@data-testid='tweetText'])[position()>1]")
   
   # handle = driver.find_element(By.XPATH, "(//div[@data-testid='User-Name'])[position()>1]")

   # Extract the content of each reply and append it to the list
   for reply in replies:
       name = reply.find_element(By.XPATH, "(//div[@data-testid='User-Name'])[position()>1]").text
       reply_contents.append(reply.text)
       username_contents.append(name)

   sleep(3)

   # Check if the page has scrolled to the bottom
   new_height = driver.execute_script("return document.body.scrollHeight")
   if new_height == last_height:
       break
   last_height = new_height



# Write the reply contents to a CSV file
import csv

with open('replies.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Tweet Content", "Name", "Number"])
  for i, (content, name) in enumerate(zip(reply_contents, username_contents), start=1):
      writer.writerow([content, name, i])
