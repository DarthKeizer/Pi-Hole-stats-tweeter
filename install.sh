#!/bin/sh
## tweetStats
NAMEOFAPP="tweetStats"
WHATITDOES="This is a script from mwoolweaver to tweet the Pi-Hole stats and other system stats once/day."

{ if 
(whiptail --title "$NAMEOFAPP" --yes-button "Skip" --no-button "Proceed" --yesno "Do you want to setup $NAMEOFAPP? $WHATITDOES" 8 78) 
then
echo "Declined $NAMEOFAPP"
else
sudo apt-get install python3-pip git
git clone https://github.com/mwoolweaver/tweetStats.git ~/
cd ~/tweetStats
sudo chmod 777 config.json
cp tweetStats tweetStats.sh
sudo chmod 777 tweetStats.sh
sed -i "s/VALUE7/$(whoami)/" ~/tweetStats/tweetStats.sh
pip3 install -r requirements.txt
cp config.json.example config.json
PIHOLE_API=$(whiptail --inputbox "Pi-hole API Path" 20 60 "" 3>&1 1>&2 2>&3)
CONSUMER_KEY=$(whiptail --inputbox "Twitter Consumer Key" 20 60 "" 3>&1 1>&2 2>&3)
CONSUMER_SECRET=$(whiptail --inputbox "Twitter Consumer Secret" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN=$(whiptail --inputbox "Twitter Access Token" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN_SECRET=$(whiptail --inputbox "Twitter Access Token Secret" 20 60 "" 3>&1 1>&2 2>&3)
IPSTACK_ACCESS_KEY=$(whiptail --inputbox "ipstack Access Key" 20 60 "" 3>&1 1>&2 2>&3)
sed -i "s/VALUE1/$PIHOLE_API/" ~/tweetStats/config.json
sed -i "s/VALUE2/$CONSUMER_KEY/" ~/tweetStats/config.json
sed -i "s/VALUE3/$CONSUMER_SECRET/" ~/tweetStats/config.json
sed -i "s/VALUE4/$ACCESS_TOKEN/" ~/tweetStats/config.json
sed -i "s/VALUE5/$ACCESS_TOKEN_SECRET/" ~/tweetStats/config.json
sed -i "s/VALUE6/$IPSTACK_ACCESS_KEY/" ~/tweetStats/config.json
{ if 
(whiptail --title "$NAMEOFAPP" --yes-button "Skip" --no-button "Proceed" --yesno "Do you want to setup $NAMEOFAPP as a reaccuring cron job?" 8 78) 
then
echo "Declined $NAMEOFAPP cron job."
else
sudo ln -s tweetStats.sh /etc/cron.daily/tweetStats
fi }
