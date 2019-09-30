#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Build the tweet
def construct_tweet():

    from lib.pihole_info import pihole_info as ph # where pihole information is gathered
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

    from lib.sys_info import sys_info as sy # where system information is gathered
    # Second Tweet
    SYtweet = '#SystemStats'
    SYtweet += '\nCPU Load AVG: ' + sy[0] # CPU load average
    SYtweet += '\nRam Usage: ' + sy[1] # RAM usage
    SYtweet += '\nDisk Usage: ' + sy[2] # disk usage information
    SYtweet += '\nNetwork Interfaces: ' + sy[3] # network interface names (doesn't include the loopback interface)
    SYtweet += '\nKernel && OS: ' + sy[4] # kernel && OS information
    SYtweet += '\nBoot Time: ' + sy[5] # time when system booted (printed as your local time)
    SYtweet += '\n#' + sy[6] # create hashtag from OS name

    from lib.speed_test import speedtest_ip as stp
    # Third Tweet
    Nettweet = '#NetStats'
    Nettweet += '\nPing: ' + stp[0] # Ping via speedtest-cli
    Nettweet += '\nSpeed Achieved (dl/ul): ' + stp[1] # Speed Achieved (dl/ul) via speedtest-cli
    Nettweet += '\nData Used (dl/ul): ' + stp[2] # Data used during speedtest (dl/ul) via speedtest-cli
    Nettweet += '\nIP: ' + stp[3] # IP address as reported by speedtest-cli
    Nettweet += '\nISP: ' + stp[4] # ISP as reported by speedtest-cli
    Nettweet += '\nRegion: ' + stp[5] # give region to preserve exact location
    Nettweet += '\nContinent: ' + stp[6] # give continent to preserve exact location
    Nettweet += '\nShare: ' + stp[7] # give sharable speedtest link (how can i make this show as a pic on Twitter??)
    Nettweet += '\n#Speedtest'

    return PHtweet, SYtweet, Nettweet
