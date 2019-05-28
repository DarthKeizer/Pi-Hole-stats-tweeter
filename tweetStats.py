#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.get_config import get_cfgt as cfgt # where all the config data lives
from lib.get_api import get_api as ga # where we interact with the Twitter API
import lib.construct_tweet as ct # where the tweet is put together
from lib.debug import debug_tweet, d1, s # All the deugging happens here && parses for passed arguements

from TwitterAPI import TwitterAPI
from threader import Threader

# Tweet it!
def tweet_it(apiTW):
        
    # build tweet
    PHtweet = ct.construct_tweet(ct.pi(), ct.si())[0]
    SYtweet = ct.construct_tweet(ct.pi(), ct.si())[1]    
    # and send it

    keys = dict(consumer_key=cfgt()[0],
            consumer_secret=cfgt()[1],
            access_token_key=cfgt()[2],
            access_token_secret=cfgt()[3])
    api = TwitterAPI(**keys)

    tweets = [PHtweet, SYtweet]
    th = Threader(tweets, api, wait=2, end_string=False)
    th.send_tweets()

    print(apiTW[0].get_oembed(id=tweet.id).url)

    


# Make it Happen!!
def main():
    d = int(d1)
    print(d)
    if d != 0: # checks for any passed args
        s.switch(d) 
    else: # if no args send it!!
        tweet_it(ga(cfgt()))

# action really happens down here tho
if __name__ == '__main__':
    main()
