#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.get_api import get_api as ga # where we interact with the Twitter API
from lib.construct_tweet import build_tweet as bt # where the tweet is put together
from lib.debug import debug_tweet, d1, s # All the deugging happens here && parses for passed arguements


from threader import Threader

# Tweet it!
def tweet_it():

    k_a = ga()
    # build tweets
    tweets = bt()
    # send tweets
    th = Threader(tweets, k_a[0], wait=2, end_string=False)
    th.send_tweets()
    # print tweet id's to console
    print(th.tweet_ids_)

# Make it Happen!!
def main():
    d = int(d1)
    if d != 0: # checks for any passed args
        s.switch(d) 
    else: # if no args send it!!
        tweet_it()

# action really happens down here tho
if __name__ == '__main__':
    main()
