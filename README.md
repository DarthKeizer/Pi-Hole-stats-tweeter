# python-tweet-statistics

![alt text](https://img.shields.io/badge/python-3.7-green.svg "Python3.7") ![alt text](https://img.shields.io/badge/tweepy-3.7-green.svg "tweepy3.7") ![alt text](https://img.shields.io/badge/requests-2.21-green.svg "requests2.21") 

Send a daily tweet with different server statistics!

# Preview

can be seen working [here](https://twitter.com/ComputeHole).

![preview](preview.png)

# How to use

1. Create an application via Twitter [here](https://apps.twitter.com/). You will need the tokens for this to work.

2. ```curl -sSL https://raw.githubusercontent.com/ComputeHole/python-tweet-statistics/master/install.sh | bash```

the install script will ask if you want to install as a cronjob

upon successful cron completion you will find ~/pihole_tweeter/twitter_bot.txt


# Credits

original install script was found [here](https://github.com/deathbybandaid/Pi-Hole-stats-tweeter/blob/master/install.sh) by [@deathbybandaid](https://github.com/deathbybandaid)


[@Akamaru](https://github.com/Akamaru) for porting to Python 3.

[@DarthKeizer](https://github.com/DarthKeizer) for the original idea.


# Compatibility

Compatible with Python 3.7 && tweepy 3.7 && requests 2.21
