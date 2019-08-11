#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.sys_info import sys_info as si # where system information is gathered
from lib.pihole_info import pihole_info as pi # where pihole information is gathered

# Build the tweet
def construct_tweet(ph, sy):
    
    # First Tweet
    PHtweet = '#PiHoleStats'
    PHtweet += '\nBlocklist Size: ' + ph[0] # size of block list
    PHtweet += '\nTotal Queries: ' + ph[1] # total queries
    PHtweet += '\nQueries Blocked: ' + ph[2] # ads blocked
    PHtweet += '\nQueries Forwarded: ' + ph[3] # forwarded queries
    PHtweet += '\nQueries Cached: ' + ph[4] # cached queries
    PHtweet += '\nUnique Clients: ' + ph[5] # unique clients
    PHtweet += '\nPrivacy Level: ' + ph[6] # privacy level
    PHtweet += '\nGravity Last Updated: ' + ph[7] # gravity last updated (printed as your local time)
    PHtweet += '\n#Python'
    
    # Second Tweet
    SYtweet = '#SystemStats'
    SYtweet += '\nCPU Load AVG: ' + sy[1] # CPU load average
    SYtweet += '\nRam Usage: ' + sy[2] # RAM usage
    SYtweet += '\nDisk Usage: ' + sy[4] # disk usage information
    SYtweet += '\nNetwork Interfaces: ' + sy[3] # network interface names (doesn't include the loopback interface)
    SYtweet += '\nKernel && OS: ' + sy[5] # kernel && OS information
    SYtweet += '\nBoot Time: ' + sy[0] # time when system booted (printed as your local time)
    SYtweet += '\n#' + sy[13] 

    # Third Tweet
    Nettweet = '#NetStats'
    Nettweet += '\nPing: ' + sy[8] # Ping via speedtest-cli
    Nettweet += '\nSpeed Achieved (dl/ul): ' + sy[7] + '/' + sy[6] # Speed Achieved (dl/ul) via speedtest-cli
    Nettweet += '\nData Used (dl/ul): ' + sy[11] + '/' + sy[12] # Data used during speedtest (dl/ul) via speedtest-cli
    Nettweet += '\nIP: ' + sy[14] # IP address as reported by speedtest-cli
    Nettweet += '\nISP: ' + sy[9] # ISP as reported by speedtest-cli
    Nettweet += '\nRegion: ' + sy[15] # give region to preserve exact location
    Nettweet += '\nContinent: ' + sy[16] # give continent to preserve exact location
    Nettweet += '\nShare: ' + sy[10] # give sharable speedtest link (how can i make this show as a pic on Twitter??)
    Nettweet += '\n#Speedtest'

    return PHtweet, SYtweet, Nettweet
