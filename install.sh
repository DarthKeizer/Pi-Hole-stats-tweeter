#!/bin/sh
## pihole tweeter
NAMEOFAPP="Pi-hole Stats Tweeter"
WHATITDOES="This script will install Pi-Hole-stats-tweeter and setup a cronjob that runs every day at 23:55"

{ if 
(whiptail --title "$NAMEOFAPP" --yes-button "Skip" --no-button "Proceed" --yesno "Do you want to setup $NAMEOFAPP? $WHATITDOES" 8 78) 
then
echo "Declined $NAMEOFAPP"
else
sudo apt-get install -y python3-pip
pip3 install -U -r https://raw.githubusercontent.com/mwoolweaver/Pi-Hole-stats-tweeter/master/requirements.txt
wget https://raw.githubusercontent.com/mwoolweaver/Pi-Hole-stats-tweeter/master/pihole_tweeter.py -P ~/pihole_tweeter/
wget https://raw.githubusercontent.com/mwoolweaver/Pi-Hole-stats-tweeter/master/config.ini -P ~/pihole_tweeter/
CONSUMER_KEY=$(whiptail --inputbox "Consumer Key" 20 60 "" 3>&1 1>&2 2>&3)
CONSUMER_SECRET=$(whiptail --inputbox "Consumer Secret" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN=$(whiptail --inputbox "Access Token" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN_SECRET=$(whiptail --inputbox "Access Token Secret" 20 60 "" 3>&1 1>&2 2>&3)
sed -ie "s/VALUE1/$CONSUMER_KEY/" ~/pihole_tweeter/config.ini
sed -ie "s/VALUE2/$CONSUMER_SECRET/" ~/pihole_tweeter/config.ini
sed -ie "s/VALUE3/$ACCESS_TOKEN/" ~/pihole_tweeter/config.ini
sed -ie "s/VALUE4/$ACCESS_TOKEN_SECRET/" ~/pihole_tweeter/config.ini
fi }
{ if 
(whiptail --title "$NAMEOFAPP" --yes-button "Skip" --no-button "Proceed" --yesno "Do you want to setup $NAMEOFAPP as a cronjob?" 8 78) 
then
echo "did not install cronjob"
else
sudo wget http://raw.githubusercontent.com/mwoolweaver/Pi-Hole-stats-tweeter/master/pi-hole-tweeter-cron -P /etc/cron.d/
rm ~/pihole_tweeter/config.inie
fi }
