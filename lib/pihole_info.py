#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# retreive data from pi-hole api.php (probably will break in a future update of pi-hole)

import lib.get_config as cfg # where the config information lives

def pihole_info(cfgp):
    
    from lib.commaValue import commaValue as cv # insert commas where needed
    from datetime import datetime as dt # used to calculate UTC from epoch
    from requests import get # handles communication to pi-hole

    # verify pi-hole reachability
    try:
        pihole_api = get(cfgp) # is passed from get_cfgp
        x = pihole_api.status_code
    except Exception as e:
        x = 'Could not contact API: ' + str(e)
        print(x)
        return x
    # check HTTP response from pi-hole
    if pihole_api.status_code != 200:
        x = pihole_api.status_code
        print(pihole_api.status_code)
        return x
    # verify pi-hole data
    try:
        d = pihole_api.json()
        gla = d["gravity_last_updated"]
    except: # complain if no JSON
        x = ('Got no or invalid JSON.')
        print(x)
        return x
    if not all(k in d for k in # check for needed variables
               ("domains_being_blocked", "dns_queries_today", "ads_blocked_today", "ads_percentage_today",
                "queries_forwarded", "queries_cached", "unique_clients", "privacy_level", "gravity_last_updated")):
        x = 'This is not a Pi-Hole JSON...'
        print('This is not Pi-Hole JSON...') # complain if all aren't present
        return
    # setup pi-hole variables
    ads_blocked_today = str(cv(d["ads_blocked_today"])) #  total number of ads block for the last 24 hrs
    ads_percentage_today = str(round(d["ads_percentage_today"], 2)) # percentage of ads block for the last 24 hrs
    # variables to  be passedQ
    domains_being_blocked = str(cv(d["domains_being_blocked"])) # pihole_info[0] - Total number of domians on the block list
    dns_queries_today = str(cv(d["dns_queries_today"])) # pihole_info[1] - total number of dns queries for the last 24 hrs
    ads_blocked = ads_blocked_today + '|' + ads_percentage_today + '%' # pihole_info[2]
    queries_forwarded = str(cv(d["queries_forwarded"])) # pihole_info[3] - number of queries forward to upstream DNS
    queries_cached = str(cv(d["queries_cached"])) # pihole_info[4] - number of queries cached
    unique_clients = str(cv(d["unique_clients"])) # pihole_info[5] - number of unique clients
    privacy_level = str(cv(d["privacy_level"])) # pihole_info[6] - Admin Privacy level selected
    glu = dt.utcfromtimestamp(gla["absolute"]).strftime('%Y-%m-%d %H:%M') # pihole_info[7] - date gravity was updated lastSaW F XR
    # return as tuple to ensure data integrity
    return (domains_being_blocked, dns_queries_today, ads_blocked, queries_forwarded,
            queries_cached, unique_clients, privacy_level, glu, x)