#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from configparser import ConfigParser
from datetime import datetime
import psutil
import os
from hurry.filesize import size
from uptime import uptime
import tweepy
import platform
from requests import get

config = ConfigParser()
try:
    config.read_file(open('config.ini'))
except FileNotFoundError:
    print('config.ini not found.')
    sys.exit(1)

# API path
try:
    api_path = config['DEFAULT']['api_path']
    consumer_key = config['DEFAULT']['consumer_key']
    consumer_secret = config['DEFAULT']['consumer_secret']
    access_token = config['DEFAULT']['access_token']
    access_token_secret = config['DEFAULT']['access_token_secret']
except KeyError as exception:
    print('Please check your config.ini.')
    sys.exit(1)
if not (api_path, consumer_key, consumer_key, consumer_secret, access_token, access_token_secret):
    print('2 Please check your config.ini.')
    sys.exit(1)

def pretty_time_delta(seconds):
    seconds = int(seconds)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
        return '%dd %dh %dm %ds' % (days, hours, minutes, seconds)
    elif hours > 0:
        return '%dh %dm %ds' % (hours, minutes, seconds)
    elif minutes > 0:
        return '%dm %ds' % (minutes, seconds)
    else:
        return '%ds' % (seconds,)

def comma_value(num):
    """Helper function for thousand separators"""
    return "{:,}".format(int(num)).replace(',', ',')


def get_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def get_pihole_data():
    try:
        res = get(api_path)
    except Exception as exception:
        print('Could not contact API: ' + str(exception))
        return

    if res.status_code != 200:
        print('Could not get data from Pi-Hole API.')
        return

    try:
        data = res.json()
    except:
        print('Got no or invalid JSON.')
        return
    if not all(k in data for k in
               ('ads_blocked_today', 'ads_percentage_today', 'dns_queries_today', 'domains_being_blocked')):
        print('This is not Pi-Hole JSON...')
        return

    return data



def construct_tweet(data):
    tweet = '#ComputeHole: The @The_Pi_Hole on @GoogleCompute\n'
    tweet += 'Ads Blocked: ' + str(comma_value(data['ads_blocked_today']))
    tweet += ' (' + str(round(data['ads_percentage_today'], 2)).replace('.', '.') + '%)\n'
    tweet += 'Total DNS Queries: ' + str(comma_value(data['dns_queries_today'])) + '\n'
    tweet += 'Domains on Blocklist: ' + str(comma_value(data['domains_being_blocked'])) + '\n'
    tweet += 'Uptime: ' + pretty_time_delta(uptime())  + '\n' + 'Load Avg: ' + str(os.getloadavg()) + '\n' + 'Ram Usage: ' + str(psutil.virtual_memory()[2]) +  '% ' + str(size(psutil.virtual_memory()[3])) + '/' + str(size(psutil.virtual_memory()[1])) + '\n'
    tweet += 'Kernel/OS: ' + str(platform.platform())
    return tweet


def main():
    # Twitter login
    api = get_api()
    try:
        print('Logged in as @' + api.me().screen_name)
    except tweepy.error.TweepError:
        print('Error while logging in - check your credentials.')
        return

    # Get Pi-Hole info from API
    data = get_pihole_data()
    if not data:
        return

    # Tweet it!
    tweet = construct_tweet(data)
    try:
        status = api.update_status(status=tweet)
    except tweepy.error.TweepError:
        print('Status could not be posted.')
        return
    print(status.id_str)


if __name__ == '__main__':
    main()
