#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def speedtest_ip():
    
    import os
    import math
    
    import urllib.request, json
    from lib.get_config import get_cfgip as cfgIP
    
    jstring = os.popen("speedtest-cli --share --json").read()
    data = json.loads(jstring)
    client = data["client"]
    server = data["server"]

    ulByte = data["bytes_sent"]/1024/1024
    dlByte = data["bytes_received"]/1024/1024
    us = data["upload"]/1000000
    ds = data["download"]/1000000
    pg = data["ping"]
    isp = client["isp"]
    share = data["share"]
    ip = client["ip"]
    country = client["country"]

    key = cfgIP()
    address = "http://api.ipstack.com/" + ip + "?access_key=" + key + "&output=json&fields=region_name,continent_name"

    with urllib.request.urlopen(address) as url:
         ipstack = json.loads(url.read().decode())

    uls = round(us, 2)
    dls = round(ds, 2)
    pings = round(pg, 2)
    dlMB = round(dlByte, 2)
    ulMB = round(ulByte, 2)

    ping = str(pings) + " ms"

    ul = str(uls) + " Mbps"
    dl = str(dls) + " Mbps"
    speed = ul + "/" + dl

    ulMBs = str(ulMB) + " MB"
    dlMBs = str(dlMB) + " MB"
    Sdata = ulMBs + "/" + dlMBs
    
    ip = '.'.join(ip.split('.')[:2]) + '.xx.xx'
    region = ipstack['region_name']
    continent = ipstack['continent_name']

    return (ping, speed, Sdata, ip, isp, region, continent, share)
