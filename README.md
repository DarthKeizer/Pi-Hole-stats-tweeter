# Pi-Hole stats tweeter
Send a daily tweet with your Pi-Hole statistics!

# How to use
1. Create an application via Twitter [here](https://apps.twitter.com/). You will need the tokens for this to work.

2. ```curl -sSL https://raw.githubusercontent.com/mwoolweaver/Pi-Hole-stats-tweeter/master/install.sh | bash```

the install script will ask if you want to install as a cronjob

upon successful cron completion you will find ~/pihole_tweeter/twitter_bot.txt


#Credits

original install script was found [here](https://github.com/deathbybandaid/Pi-Hole-stats-tweeter/blob/master/install.sh) 

