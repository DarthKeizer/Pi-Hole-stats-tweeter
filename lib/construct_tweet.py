#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.sys_info import sys_info as si # where system information is gathered
from lib.pihole_info import pihole_info as pi # where pihole information is gathered

# Build the tweet
def construct_tweet(ph, sy):
    
    PHtweet = '#ComputeHole: @The_Pi_Hole on @GoogleCompute'
    PHtweet += '\n🚫🌐: ' + ph[0] # size of block list
    PHtweet += '\n🈵⁉: ' + ph[1] # total querries
    PHtweet += '\n📢🚫: ' + ph[2] # ads blocked
    PHtweet += '\n⁉⏭: ' + ph[3] # forwarded querries
    PHtweet += '\n⁉💾: ' + ph[4] # cached querries
    PHtweet += '\n🦄🙈: ' + ph[5] # unique clients
    PHtweet += '\n🔐🎚: ' + ph[6] # privacy level
    PHtweet += '\n🚫📝⌛: ' + ph[7] # gravity last updated (printed as your local time)
    PHtweet += '\n#Pihole_Stats'
    
    SYtweet = '#Ubuntu #IoT #GCP #cloud'
    SYtweet += '\n⚖️x̅: ' + sy[1] # CPU load average
    SYtweet += '\n🐏📈: ' + sy[2] # RAM usage
    SYtweet += '\n🔗📡: ' + sy[3] # network interface names (doesn't include the loopback interface)
    SYtweet += '\n💾📊: ' + sy[4] # disk usage information
    SYtweet += '\n🐧🌽: ' + sy[5] # kernel && OS information
    SYtweet += '\n🖥️👢⏳: ' + sy[0] # time when system booted (printed as your local time)
    # print(tweet) # always print tweet to console so we can see the output locally
    return PHtweet, SYtweet

