#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.sys_info import sys_info as si # where system information is gathered
from lib.pihole_info import pihole_info as pi # where pihole information is gathered

# Build the tweet
def construct_tweet(ph, sy):
    tweet = '🚫🌐: ' + ph[0] # size of block list
    tweet += '\n🈵⁉: ' + ph[1] # total querries
    tweet += '\n📢🚫: ' + ph[2] # ads blocked
    tweet += '\n⁉⏭: ' + ph[3] # forwarded querries
    tweet += '\n⁉💾: ' + ph[4] # cached querries
    tweet += '\n🦄🙈: ' + ph[5] # unique clients
    tweet += '\n🔐🎚: ' + ph[6] # privacy level
    tweet += '\n🚫📝⌛: ' + ph[7] # gravity last updated (printed as UTC-5 or UTC-6 depends on DST)
    tweet += '\n⚖️x̅: ' + sy[1] # CPU load average
    tweet += '\n🐏📈: ' + sy[2] # RAM usage
    tweet += '\n🔗📡: ' + sy[3] # network interface names (doesn't include the loopback interface)
    tweet += '\n💾📊: ' + sy[4] # disk usage information
    tweet += '\n🐧🌽: ' + sy[5] # kernel && OS information
    tweet += '\n🖥️👢⏳: ' + sy[0] # time when system booted (printed as UTC-5 or UTC-6 depends on DST)
    # print(tweet) # always print tweet to console so we can see the output locally
    return tweet

