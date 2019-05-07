#!/bin/sh
## python-tweet-statistics
## file originally created by https://github.com/deathbybandaid and can be seen @ https://github.com/deathbybandaid/Pi-Hole-stats-tweeter/blob/master/install.sh
NAMEOFAPP="python-tweet-statistics"
WHATITDOES="This script will install python-tweet-statistics and can setup a cronjob that runs every day at 23:55"

{ if 
(whiptail --title "$NAMEOFAPP" --yes-button "Skip" --no-button "Proceed" --yesno "Do you want to setup $NAMEOFAPP? $WHATITDOES" 8 78) 
then
echo "Declined $NAMEOFAPP"
else
sudo apt-get install -y python3-pip
pip3 install -U -r https://raw.githubusercontent.com/ComputeHole/python-tweet-statistics/master/requirements.txt
wget https://raw.githubusercontent.com/ComputeHole/python-tweet-statistics/master/tweetStats.py -O ~/python-tweet-statistics/tweetStats.py
wget https://raw.githubusercontent.com/ComputeHole/python-tweet-statistics/master/config.ini.sample -O ~/python-tweet-statistics/config.ini
CONSUMER_KEY=$(whiptail --inputbox "Consumer Key" 20 60 "" 3>&1 1>&2 2>&3)
CONSUMER_SECRET=$(whiptail --inputbox "Consumer Secret" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN=$(whiptail --inputbox "Access Token" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN_SECRET=$(whiptail --inputbox "Access Token Secret" 20 60 "" 3>&1 1>&2 2>&3)
sed -ie "s/VALUE1/$CONSUMER_KEY/" ~/python-tweet-statistics/config.ini
sed -ie "s/VALUE2/$CONSUMER_SECRET/" ~/python-tweet-statistics/config.ini
sed -ie "s/VALUE3/$ACCESS_TOKEN/" ~/python-tweet-statistics/config.ini
sed -ie "s/VALUE4/$ACCESS_TOKEN_SECRET/" ~/python-tweet-statistics/config.ini
fi }
{ if 
(whiptail --title "$NAMEOFAPP" --yes-button "Skip" --no-button "Proceed" --yesno "Do you want to setup $NAMEOFAPP as a cronjob?" 8 78) 
then
rm ~/pihole_tweeter/config.inie
echo "did not install cronjob"
else
sudo wget https://github.com/ComputeHole/python-tweet-statistics/blob/master/tweetStats -P /etc/cron.d/
rm ~/python-tweet-statistics/config.inie
fi }
