# Send tweet when script is called
# RUN WITH PYTHON3

import tweepy
import datetime
import json
import urllib
from urllib.request import urlopen

# Retrieve data and load it into a dictionary
data = urlopen('http:/path/to/admin/api.php').read() #bytes
body = data.decode('utf-8')
data = json.loads(body)

# Create tweet
template_tweet = "\nAds Blocked: %s\nAds Percentage Today: %i\nDNS Queries Today: %s\nDomains Being Blocked: %s"
data = template_tweet % (data['ads_blocked_today'],
                          float (data['ads_percentage_today']),
                          data['dns_queries_today'],
                          data['domains_being_blocked']
                         )

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values from twitter here
  cfg = { 
    "consumer_key"        : "VALUE",
    "consumer_secret"     : "VALUE",
    "access_token"        : "VALUE",
    "access_token_secret" : "VALUE" 
    }
  
  api = get_api(cfg)
  tweet = "I am A #Raspberry_Pi #Python scripted #Bot\n\nThis is my daily " + "#PiHole report:\n" + data + "\n\nTime and date: " + datetime.datetime.today().strftime("%H:%M %d-%m-%Y")
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing
  print (tweet)

if __name__ == "__main__":
  main()
