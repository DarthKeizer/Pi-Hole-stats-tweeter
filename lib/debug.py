#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.sys_info import sys_info as si # where system information is gathered
from lib.pihole_info import pihole_info as pi # where pihole information is gathered
import lib.get_config as apiC # where all the config data lives
from lib.get_api import get_api as apiT # where we interact with the Twitter API
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
    # Where the switching happens
    def switch(self, dbm):
        return getattr(self, 'case_' + str(dbm), lambda: parser.print_help())()
    # Where the switch goes
    def case_1(self): # Print test tweet with real values
        return debug_tweet(pi(), si())
    def case_3(self): # Check Twitter login
        return apiT(apiC.get_cfgt())
    def case_4(self): # Print Test Tweet && Verify Twitter Login
        return debug_tweet(pi(), si()), apiT(apiC.get_cfgt())
    def case_5(self): # Check pi-hole api reachability
        return print('if ' + str(pi()[9]) + ' == 200 --> success \n\n Otherwise pi-hole URL is not configured properly. \n Check config.json.\n')
    def case_6(self): # Print Test Tweet && Check pi-hole api reachability
        return debug_tweet(pi(), si()), print('if ' + str(pi()[9]) + ' == 200 --> success \n\n Otherwise pi-hole URL is not configured properly. \n Check config.json.\n')
    def case_8(self): # Check Twitter login && Check pi-hole api reachability
        return apiT(apiC.get_cfgt()), print('if ' + str(pi()[9]) + ' == 200 --> success \n\n Otherwise pi-hole URL is not configured properly. \n Check config.json.\n')
    def case_9(self): # Print All The Above Debug Options
        return debug_tweet(pi(), si()), apiT(apiC.get_cfgt()), print('if ' + str(pi()[9]) + ' == 200 --> success \n\n Otherwise pi-hole URL is not configured properly. \n Check config.json.\n')

s = debugSwitch()

# prints a test tweet and most (if not all) information used by this program
def debug_tweet(ph, sy):
    tweet = '🚫🌐: ' + ph[0]
    tweet += '\n🈵⁉: ' + ph[1]
    tweet += '\n📢🚫: ' + ph[2]
    tweet += '\n⁉⏭: ' + ph[3]
    tweet += '\n⁉💾: ' + ph[4]
    tweet += '\n🦄🙈: ' + ph[5]
    tweet += '\n🔐🎚: ' + ph[6]
    tweet += '\n🚫📝⌛: ' + ph[7]
    tweet += '\n⚖️x̅: ' + sy[1]
    tweet += '\n🐏📈: ' + sy[2]
    tweet += '\n🔗📡: ' + sy[3]
    tweet += '\n💾📊: ' + sy[4]
    tweet += '\n🐧🌽: ' + sy[5]
    tweet += '\n🖥️👢⏳: ' + sy[0]
    
    # These variables were used during development 
    # ne =28
    # sc = 43
    # tweets ="🚫🌐🈵⁉📢🚫⁉⏭⁉💾🦄🙈🔐🎚🚫📝⌛️🐏📈🔗📡💾📊🐧🌽️👢⏳"
    # x̅ is not an emoji so count it as a regular character
    # tweetS = 'x̅' + ph[0] + ph[1] + ph[2] + ph[3] + ph[4] + ph[5] + ph[6] + ph[7] + sy[0] + sy[1] + sy[2] + sy[3] + sy[4] + sy[5]
    
    # ^^^^^ These variables were used during development  ^^^^^^

    print('\n Twitter Keys')
    print(apiC.get_cfgt()[5])
    print('\n Pihole Address')
    print(apiC.get_cfgp()[1])
    print('\n Pihole Stats')
    print(ph)
    print('\n System Stats')
    print(sy)
    print('\n The tweet that was created.')
    print(tweet)
    print('\n Number of characters in tweet +/- 1 or 2') # will try and nail this down to a more accurate number
    num_emoji = (sum(tweet.count(emoji) for emoji in UNICODE_EMOJI)) # accurately count and track emoji
    ignored_chars = UNICODE_EMOJI.copy() # thanks to https://stackoverflow.com/q/56214183/11456464
    num_other = sum(0 if char in ignored_chars else 1 for char in tweet)
    totalS = (num_emoji * 2 + num_other)
    print(str(num_emoji) + '(<- individual emjoi * 2) + ' + str(num_other) + '(<- # of characters that aren\'t emoji\'s) = ' +  str(totalS))
    return