#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.get_config import get_cfgt as cfgt # where all the config data lives
from lib.get_api import get_api as ga # where we interact with the Twitter API
import lib.construct_tweet as ct # where the tweet is put together
from lib.debug import debug_tweet, d1, s # All the deugging happens here && parses for passed arguements


from threader import Threader

# Tweet it!
def tweet_it(apiTW):
    
    print(ga(cfgt())[3])

    # build tweet
    PHtweet = ct.construct_PHtweet(ct.pi())
    SYtweet = ct.construct_SYtweet(ct.si())
    NETtweet =  ct.construct_NETtweet(ct.sip())
    # and send it

    tweets = [PHtweet, SYtweet, NETtweet]
    th = Threader(tweets, apiTW[1], wait=2, end_string=False)
    th.send_tweets()

    for x in th.tweet_ids_:
        print('Status posted! https://twitter.com/' + ga(cfgt())[0].me().screen_name + '/status/' + str(x))


# Make it Happen!!
def main():
    d = int(d1)
    if d != 0: # checks for any passed args
        s.switch(d) 
    else: # if no args send it!!
        tweet_it(ga(cfgt()))

# action really happens down here tho
if __name__ == '__main__':
    main()
