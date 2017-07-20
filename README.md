# Pi Hole stats tweeter
I want to send a a daily tweet with the results of what my Pi-Hole blocked. Here is the code, run in Python3.

# How to use
Install following python dependencies with sudo pip install: 
  tweepy
  datetime
  json
  urllib

Download python file and replace it with your own account data and link to your own path/to/admin/api.php

# Cronjob
This will tweet your stats at 23:59 everyday

59 23 * * * sudo python3 /home/pi/Desktop/twittertweeter.py >/dev/null 2>&1

# Twitter acces keys and tokens
On their own website it is quite clearly explained: https://dev.twitter.com/oauth/overview/application-owner-access-tokens

# Reddit
https://www.reddit.com/r/pihole/comments/67umvj/need_help_with_doing_a_daily_pihole_tweet/
