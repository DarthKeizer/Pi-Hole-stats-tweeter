#!/bin/sh
## tweetStats
NAMEOFAPP="tweetStats"
WHATITDOES="This is a script from mwoolweaver to tweet the Pi-Hole stats and other system stats once/day."

{ if 
(whiptail --title "$NAMEOFAPP" --yes-button "Skip" --no-button "Proceed" --yesno "Do you want to setup $NAMEOFAPP? $WHATITDOES" 8 78) 
then
echo "Declined $NAMEOFAPP"
else
git clone https://github.com/mwoolweaver/tweetStats.git ~/
sudo apt-get install -y python3-pip
cd ~/tweetStats
pip3 install -r requirements.txt
cp config.json.example config.json
PIHOLE_API=$(whiptail --inputbox "Pi-hole API Path" 20 60 "" 3>&1 1>&2 2>&3)
CONSUMER_KEY=$(whiptail --inputbox "Consumer Key" 20 60 "" 3>&1 1>&2 2>&3)
CONSUMER_SECRET=$(whiptail --inputbox "Consumer Secret" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN=$(whiptail --inputbox "Access Token" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN_SECRET=$(whiptail --inputbox "Access Token Secret" 20 60 "" 3>&1 1>&2 2>&3)
sudo sed -i "s/VALUE1/$PIHOLE_API/" ~/tweetStats/config.json
sudo sed -i "s/VALUE2/$CONSUMER_KEY/" ~/tweetStats/config.json
sudo sed -i "s/VALUE3/$CONSUMER_SECRET/" ~/tweetStats/config.json
sudo sed -i "s/VALUE4/$ACCESS_TOKEN/" ~/tweetStats/config.json
sudo sed -i "s/VALUE5/$ACCESS_TOKEN_SECRET/" ~/tweetStats/config.json
{ if 
(whiptail --title "$NAMEOFAPP" --yes-button "Skip" --no-button "Proceed" --yesno "Do you want to setup $NAMEOFAPP as a reaccuring cron job?" 8 78) 
then
echo "Declined $NAMEOFAPP cron job."
else
sudo cp tweetStats /etc/cron.d/
fi }
