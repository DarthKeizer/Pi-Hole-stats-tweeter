#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib import get_config as cfg # where all the config data lives
from lib.get_api import get_api as ga # where we interact with the Twitter API
import lib.construct_tweet as ct # where the tweet is put together
from lib.debug import debug_tweet, d1, s # All the deugging happens here && parses for passed arguements

# Tweet it!
def tweet_it(api):
        
    # build tweet
    PHtweet = ct.construct_tweet(ct.pi(), ct.si())[0]
    SYtweet = ct.construct_tweet(ct.pi(), ct.si())[1]    
    # and send it
    try:
        status = api[0].update_status(status=PHtweet)
    except api[2].TweepError as e: # most of the time you end up here cause your tweet was to long ( tweet > 280 characters)
        print(e.reason)            #  if this happens regularly you might have to remove some data from the tweet
        s.switch(1)
        return
    print('Tweet tweeted!! --> https://twitter.com/' + status.author.screen_name + '/status/' + status.id_str)

    piStatus = status.id_str
    me = status.author.screen_name
    reply_status = "@%s @The_Pi_Hole @GoogleCompute\n %s" % (me, SYtweet)

    try:
        status = api[0].update_status(status=reply_status, in_reply_to_status_id=piStatus)
    except api[2].TweepError as e: # most of the time you end up here cause your tweet was to long ( tweet > 280 characters)
        print(e.reason)            #  if this happens regularly you might have to remove some data from the tweet
        s.switch(1)
        return
    print('Tweet tweeted!! --> https://twitter.com/' + status.author.screen_name + '/status/' + status.id_str)

# Make it Happen!!
def main():
    d = int(d1)
    print(d)
    if d != 0: # checks for any passed args
        s.switch(d) 
    else: # if no args send it!!
        tweet_it(ga(cfg.get_cfgt()))

# action really happens down here tho
if __name__ == '__main__':
    main()
