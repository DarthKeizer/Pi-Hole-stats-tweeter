#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.get_config import get_cfgt as cfgt
from TwitterAPI import TwitterAPI

# login to Twitter
def get_api():

    keys = cfgt()
    
    KEYS_and_API = TwitterAPI(**keys)
    
    verify = KEYS_and_API.request('account/verify_credentials')
    
    name = verify['screen_name']

    print("Logged in as @" + str(name) + ".")

    return (KEYS_and_API)