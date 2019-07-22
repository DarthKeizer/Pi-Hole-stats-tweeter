#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# get data needed for pi-hole communication
def get_cfgp():
    import json as js  # Used to parse config.json
    from requests import get # retreives file from a given url

    # check for config.json
    try:
        with open('config.json') as data:
            cfg = js.load(data)
    except FileNotFoundError as e:
        print(e)
        raise SystemExit
    
    # verify && set key info from config.json
    cfgP = cfg['pihole']
    try: # try to get api_path for pi-hole
        api = cfgP['api_path'] # get_cfgp()[0]
    except KeyError as e:
        print(str(e) + ' variable(s) not found.')
        raise SystemExit
    if not (api): #verify api_path is not None
        print('Please check your config.ini.')
        raise SystemExit
    # return as tuple to ensure data integrity
    return (api, cfgP)

# get data needed for twitter communication
def get_cfgt():
    import json as js  # Used to parse config.json
    import tweepy as tp # used to actually send tweet is also
    # ^^^^^^^^^^ passed as get_config[5] for no good reason

    # check for config.json
    try:
        with open('config.json') as data:
            cfg = js.load(data)
    except FileNotFoundError as e:
        print(e)
        raise SystemExit
    # verify && set key info from config.json
    cfgT = cfg['twitter']
    try:
        consumer_key = cfgT['consumer_key'] # get_cfgt()[0]
        consumer_secret = cfgT['consumer_secret'] # get_cfgt()[1]
        access_token = cfgT['access_token'] # get_cfgt()[2]
        access_token_secret = cfgT['access_token_secret'] # get_cfg()[3]
    except KeyError as e:
        print(str(e) + ' variable(s) not found.')
        raise SystemExit
    if not (consumer_key, consumer_secret, access_token, access_token_secret):
        print('2 Please check your config.ini.')
        raise SystemExit
    # return as tuple to ensure data integrity
    return (consumer_key, consumer_secret, access_token, access_token_secret,
            tp, cfgT)

    
def get_cfgip():
    
    import json as js  # Used to parse config.json

    with open('config.json') as data:
            cfg = js.load(data)
    
    ipstackKey = cfg['ipstack']['access_key']

    return (ipstackKey)