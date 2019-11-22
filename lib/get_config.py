#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json as js  # Used to parse config.json

# check for config.json
try:
    with open('config.json') as data:
        cfg = js.load(data)
except FileNotFoundError as e:
    print(e)
    raise SystemExit

# get data needed for pi-hole communication
def get_cfgp():
    
    # verify && set key info from config.json
    cfgP = cfg['pihole']
    try: # try to get api_path for pi-hole
        api = cfgP['api_path']
    except KeyError as e:
        print(str(e) + ' variable(s) not found.')
        raise SystemExit
    if not (api): #verify api_path is not None
        print('Please check your config.ini.')
        raise SystemExit
    # return as tuple to ensure data integrity
    return (api)

# get data needed for twitter communication
def get_cfgt():

    # verify && set key info from config.json
    cfgT = cfg['twitter']
    try:
        consumer_key = cfgT['consumer_key'] # get_cfgt()[0]
        consumer_secret = cfgT['consumer_secret'] # get_cfgt()[1]
        access_token_key = cfgT['access_token'] # get_cfgt()[2]
        access_token_secret = cfgT['access_token_secret'] # get_cfg()[3]
    except KeyError as e:
        print(str(e) + ' variable(s) not found.')
        raise SystemExit
    if not (consumer_key, consumer_secret, access_token_key, access_token_secret):
        print('2 Please check your config.ini.')
        raise SystemExit
    # return as tuple to ensure data integrity
    
    keys = dict(consumer_key=cfgT['consumer_key'], consumer_secret=cfgT['consumer_secret'], access_token_key=cfgT['access_token'], access_token_secret=cfgT['access_token_secret'])
    
    return (consumer_key, consumer_secret, access_token_key, access_token_secret, keys)

    
def get_cfgip():
    
    ipstackKey = cfg['ipstack']['access_key']

    return (ipstackKey)