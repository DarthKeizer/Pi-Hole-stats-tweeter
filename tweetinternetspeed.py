import subprocess
import tweepy
import requests
import datetime

#
# Python script to tweet your Internet speed
#

def main():
  script_path = '/path/to/speedtest.py' # location of the original speedtest script located at: https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
  # Your IP adress
  ip = '69.69.69.69' + '\n\nTime and date: ' + datetime.datetime.today().strftime("%H:%M %d-%m-%Y") + ' GMT+0200'

  # Get the Internet speed by calling speedtest-cli
  speed = subprocess.check_output(['python', script_path, '--simple', '--bytes'])
  speed = "I am A #Raspberry_Pi #Python scripted #Bot\nThis is my daily #InternetSpeed report with #SpeedMeter:\n\n" + speed
  if ip != None:
    speed += "IP address: " + ip 

  # Twitter consumer key, secret, access token and secret
  consumer_key = '######'
  consumer_secret = '######'
  access_token = '######-######'
  access_token_secret = '######'
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)

  # Set status on Twitter
  status = api.update_status(status=speed)

  # Display information for logging
  print speed

if __name__ == "__main__":
  main()
