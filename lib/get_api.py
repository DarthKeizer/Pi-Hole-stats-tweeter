#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.get_config import get_cfgt as cfgt
# login to Twitter
def get_api():

    keys = cfgt()

    import tweepy as tp # used to verify login creds is also
    from TwitterAPI import TwitterAPI
    
        KEYS_and_API = TwitterAPI(**keys[4])
    
        verify = KEYS_and_API.request('account/verify_credentials')
        
        name = verify['screen_name']

        print("Logged in as @" + str(name) + "."
        
    
    
    return (KEYS_and_API)
