import snscrape.modules.twitter as sntwitter
import csv
# List to store tweet data
tweet_data = []

# Create a TwitterUserScraper object
scraper = sntwitter.TwitterUserScraper('ApeComms') # replace 'username' with the actual username

# Scrape the data
for i, tweet in enumerate(scraper.get_items()):
   if i > 100:
       break
   tweet_data.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

# Write the data to a CSV file
with open('tweets.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(["Date", "ID", "Content", "User"])
   writer.writerows(tweet_data)

'''
# Print the data
for tweet in tweet_data:
   print(f"Date: {tweet[0]}, ID: {tweet[1]}, Content: {tweet[2]}, User: {tweet[3]}")
'''