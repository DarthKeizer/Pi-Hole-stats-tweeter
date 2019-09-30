#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# login to Twitter
def get_api(keys):

    import tweepy as tp # used to verify login creds is also
    from TwitterAPI import TwitterAPI
    
    auth = tp.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    api = tp.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    # verify twitter credentials
    try:
        login = ('Logged in as @' + api.me().screen_name)
    except tp.error.TweepError as e:
        print(e.reason + 'This your down fall')
        return
        
    KEYSapi = TwitterAPI(**keys[4])
    
    return (api, KEYSapi, login) # get_api[0] && get_api[1] && get_api[2]
                          #  ^^ login result
