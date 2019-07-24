#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# login to Twitter
def get_api(keys):
    auth = keys[4].OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    api = keys[4].API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    # verify twitter credentials
    try:
        login = ('Logged in as @' + api.me().screen_name)
    except keys[4].error.TweepError as e:
        print(e.reason + 'This your down fall')
        return
    return (api, keys[0],
            keys[4], login) # get_api[0] && get_api[1] && get_api[2]
        #   ^^ Tweepy recieved from get_config[3]
                    #  ^^ login result
