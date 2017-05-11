#!/bin/sh
## pihole tweeter
NAMEOFAPP="piholetweeter"
WHATITDOES="This is a script from DarthKeizer to tweet the Pi-Hole stats daily."

{ if 
(whiptail --title "$NAMEOFAPP" --yes-button "Skip" --no-button "Proceed" --yesno "Do you want to setup $NAMEOFAPP? $WHATITDOES" 8 78) 
then
echo "Declined $NAMEOFAPP"
else
sudo apt-get install -y python3-pip
sudo python3 -m pip install -U setuptools
sudo python3 -m pip install tweepy
sudo python3 -m pip install request
sudo python3 -m pip install urllib
sudo python3 -m pip install json
sudo python3 -m pip install simplejson
sudo python3 -m pip install datetime
sudo cp -n /etc/piadvanced/piholetweaks/twittertweeter-ads.py
CONSUMER_KEY=$(whiptail --inputbox "Consumer Key" 20 60 "" 3>&1 1>&2 2>&3)
CONSUMER_SECRET=$(whiptail --inputbox "Consumer Secret" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN=$(whiptail --inputbox "Access Token" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN_SECRET=$(whiptail --inputbox "Access Token Secret" 20 60 "" 3>&1 1>&2 2>&3)
sudo sed -i "s/VALUE1/$CONSUMER_KEY/" /home/pi/Desktop/twittertweeter.py
sudo sed -i "s/VALUE2/$CONSUMER_SECRET/" /home/pi/Desktop/twittertweeter.py
sudo sed -i "s/VALUE3/$ACCESS_TOKEN/" /home/pi/Desktop/twittertweeter.py
sudo sed -i "s/VALUE4/$ACCESS_TOKEN_SECRET/" /home/pi/Desktop/twittertweeter.py
(crontab -l ; echo "## Pihole Tweeter") | crontab -
(crontab -l ; echo "59 23 * * * sudo python3 /home/pi/Desktop/twittertweeter.py >/dev/null 2>&1") | crontab -
(crontab -l ; echo "") | crontab -

## End of install
fi }
