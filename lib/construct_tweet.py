#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.sys_info import sys_info as si # where system information is gathered
from lib.pihole_info import pihole_info as pi # where pihole information is gathered

# Build the tweet
def construct_tweet(ph, sy):
    
    # First Tweet
    PHtweet = '#PiHoleStats'
    PHtweet += '\nBlocklist Size: ' + ph[0] # size of block list
    PHtweet += '\nTotal Querries: ' + ph[1] # total querries
    PHtweet += '\nQuerriess Blocked: ' + ph[2] # ads blocked
    PHtweet += '\nQuerries Forwarded: ' + ph[3] # forwarded querries
    PHtweet += '\nQuerries Cached: ' + ph[4] # cached querries
    PHtweet += '\nUnique Clients: ' + ph[5] # unique clients
    PHtweet += '\nPrivacy Level: ' + ph[6] # privacy level
    PHtweet += '\nGravity Last Updated: ' + ph[7] # gravity last updated (printed as your local time)
    PHtweet += '\n#Python'
    
    # Second Tweet
    SYtweet = '#SystemStats'
    SYtweet += '\nCPU Laod AVG: ' + sy[1] # CPU load average
    SYtweet += '\nRam Usage: ' + sy[2] # RAM usage
    SYtweet += '\nDisk Usage: ' + sy[4] # disk usage information
    SYtweet += '\nNetwork Interfaces: ' + sy[3] # network interface names (doesn't include the loopback interface)
    SYtweet += '\nKernel && OS: ' + sy[5] # kernel && OS information
    SYtweet += '\nBoot Time: ' + sy[0] # time when system booted (printed as your local time)
    SYtweet += '\n#' + sy[13]

    # Third Tweet
    Nettweet = '#NetStats'
    # Nettweet += '\nNetwork Interfaces: ' + sy[3] # network interface names (doesn't include the loopback interface)
    Nettweet += '\nPing: ' + sy[8] # Ping via speedtest-cli
    Nettweet += '\nDown/Up Speed: ' + sy[7] + '/' + sy[6] # Upload speed via speedtest-cli
    Nettweet += '\nData Used (dl/ul): ' + sy[11] + '/' + sy[12]
    Nettweet += '\nIP: ' + sy[14]
    Nettweet += '\nISP: ' + sy[9]
    Nettweet += '\nCity: ' + sy[15]
    Nettweet += '\nCountry: ' + sy[16]
    Nettweet += '\nShare: ' + sy[10]
    Nettweet += '\n#Speedtest'
    # print(tweet) # always print tweet to console so we can see the output locally
    return PHtweet, SYtweet, Nettweet


