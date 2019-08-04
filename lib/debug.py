#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.pihole_info import pihole_info as pi # where pihole information is gathered
from lib.get_api import get_api as apiT # where we interact with the Twitter API
import lib.get_config as apiC # where all the config data lives
from emoji import UNICODE_EMOJI # where we get our emoji dictionary from
from argparse import ArgumentParser # how we parse command line when/if they are passed

# parse command line arguements, IF any are passed
parser = ArgumentParser()
parser.add_argument('-db', dest='db', type=int, nargs='?', default=0, const=1, help='Will print all variables to console including a contructed tweet')
parser.add_argument('-dbl', dest='dbl', type=int, nargs='?', default=0, const=3, help='test twitter login')
parser.add_argument('-dbp', dest='dbp', type=int, nargs='?', default=0, const=5, help='test pi-hole api reachability')

args = parser.parse_args()

db = args.db
dbl = args.dbl
dbp = args.dbp

d1 = db + dbl + dbp # add our args together for better handling of each case

class debugSwitch:
    
    # Print number used to determine debug output
    print("Debug Variable = " + str(d1) + "\ntweetStats.py -h for more info")

    # Where the switching happens    
    def switch(self, dbm):
        return getattr(self, 'case_' + str(dbm), lambda: parser.print_help())()
    # Where the switch goes
    def case_1(self): # Print test tweet with real values
        return debug_tweet()
    def case_3(self): # Check Twitter login
        print(apiT(apiC.get_cfgt())[3])
        print(apiC.get_cfgt()[5])
        return
    def case_4(self): # Print Test Tweet && Verify Twitter Login
        print(apiT(apiC.get_cfgt())[3])
        return debug_tweet()
    def case_5(self): # Check pi-hole api reachability
        print('if ' + str(pi()[9]) + ' == 200 --> success \n\n Otherwise pi-hole URL is not configured properly. \n Check config.json.\n')
        return
    def case_6(self): # Print Test Tweet && Check pi-hole api reachability
        print('if ' + str(pi()[9]) + ' == 200 --> success \n\n Otherwise pi-hole URL is not configured properly. \n Check config.json.\n')
        return debug_tweet()
    def case_8(self): # Check Twitter login && Check pi-hole api reachability
        print(apiT(apiC.get_cfgt())[3])
        print('if ' + str(pi()[9]) + ' == 200 --> success \n\n Otherwise pi-hole URL is not configured properly. \n Check config.json.\n')
        return
    def case_9(self): # Print All The Above Debug Options
        return debug_tweet()

s = debugSwitch()

# prints a test tweet and most (if not all) information used by this program
def debug_tweet():

    print('\n Twitter Keys')
    print(apiC.get_cfgt()[5])

    print("\nCheck Twitter Login")
    from lib.get_api import get_api as apiT # where we interact with the Twitter API
    print(apiT(apiC.get_cfgt())[3])
    
    print('\n Pihole Address')
    print(apiC.get_cfgp()[1])
    
    print("\nPiHole Status")
    from lib.pihole_info import pihole_info as pi # where pihole information is gathered
    print('if ' + str(pi()[9]) + ' == 200 --> success \n\n Otherwise pi-hole URL is not configured properly. \n Check config.json.\n')
    
    print('\n Pihole Stats')
    from lib.pihole_info import pihole_info as pi # where pihole information is gathered
    print(pi())
    
    print('\n SpeedTest Info')
    from lib.speed_test import data
    print(data)
    
    print('\n System Stats')
    from lib.sys_info import sys_info as si # where system information is gathered
    print(si())
    
    print('\n The tweets that where created.')
    import lib.construct_tweet as ct # where the tweet is put together
    # build tweet
    PHtweet = ct.construct_tweet(ct.pi(), ct.si())[0]
    SYtweet = ct.construct_tweet(ct.pi(), ct.si())[1]
    Nettweet = ct.construct_tweet(ct.pi(), ct.si())[2]
    tweet = '\n\n Tweet 1\n' + PHtweet + '\n\n Tweet 2\n' + SYtweet + '\n\n Tweet 3\n' + Nettweet + '\n'
    print(tweet)
    
    print('\n Number of characters in tweet +/- 1 or 2') # will try and nail this down to a more accurate number
    num_emoji = (sum(tweet.count(emoji) for emoji in UNICODE_EMOJI)) # accurately count and track emoji
    ignored_chars = UNICODE_EMOJI.copy() # thanks to https://stackoverflow.com/q/56214183/11456464

    PHnum_other = sum(0 if char in ignored_chars else 1 for char in PHtweet)
    totalS = (num_emoji * 2 + PHnum_other)
    print(str(num_emoji) + '(<- individual emjoi * 2) + ' + str(PHnum_other) + '(<- # of characters that aren\'t emoji\'s) = ' +  str(totalS))

    SYnum_other = sum(0 if char in ignored_chars else 1 for char in SYtweet)
    totalS = (num_emoji * 2 + SYnum_other)
    print(str(num_emoji) + '(<- individual emjoi * 2) + ' + str(SYnum_other) + '(<- # of characters that aren\'t emoji\'s) = ' +  str(totalS))

    Netnum_other = sum(0 if char in ignored_chars else 1 for char in Nettweet)
    totalS = (num_emoji * 2 + Netnum_other)
    print(str(num_emoji) + '(<- individual emjoi * 2) + ' + str(Netnum_other) + '(<- # of characters that aren\'t emoji\'s) = ' +  str(totalS))
    return