#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.get_config import get_cfgt as cfgt # where all the config data lives
from lib.get_config import get_cfgp as cfgp # pihole data
from lib.get_api import get_api as ga # where we interact with the Twitter API
from lib.construct_tweet import build_tweet as bt # where the tweet is put together
from lib.debug import debug_tweet, d1, s # All the deugging happens here && parses for passed arguements


from threader import Threader

# Tweet it!
def tweet_it(apiTW):
    
    print(apiTW[2])

    # build tweets
    
    tweets = bt()
    
    # send tweets
    
    th = Threader(tweets, apiTW[1], wait=2, end_string=False)
    th.send_tweets()

    for x in th.tweet_ids_:
        print('Status posted! https://twitter.com/' + apiTW[0].me().screen_name + '/status/' + str(x))


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
