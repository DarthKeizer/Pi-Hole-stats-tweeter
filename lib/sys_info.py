#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# retreive data for system information

def sys_info():
    import platform
    from platform import platform as pl  # used to retreive OS && kernel version
    from distro import name as OSname # used to retreive OS name for hashtag
    from re import sub as re # used to apply regex
    from shutil import disk_usage as du # used to get hard drive info
    from hurry.filesize import size as sz # converts bytes to GB
    from psutil import virtual_memory as vm # Used to retrieve memory usage stats
    from psutil import boot_time as bt # how we get boot time
    from psutil import getloadavg as gl # how we get cpu load average
    import netifaces as ni  # used to retreive network interfaces
    from datetime import datetime as dt # used to calculate UTC from epoch
    from lib.speed_test import us, ds, pg, isp, share, dlByte, ulByte, ip, data
 
    

    regex = r"'lo'(?:,\s*)?|[][')(]|(?:,\s*)?'lo'" # modified suggestion from https://stackoverflow.com/questions/56153426/regex-for-replacing-special-pa>
    total, used, free = du("/") # Get disk stats - we only use 2 of these but the function requires all 3 (total, used, free)
    free = None
    GBtotal = (total // (2**30)) # convert total space to GB
    GBused = (used // (2**30)) # convert used space to GB
    percentHDD = round(100 * float(GBused)/float(GBtotal), 2) # create percentage for disk used
    cpuLoadAvg = str(gl()) # regex can't manipulate a list so turn to string
    netfaces = str(ni.interfaces()) # regex can't manipulate a list so turn to string
    usedMem = str(sz(vm()[3])) # RAM used
    totMem = str(sz(vm()[1])) #  RAM available
    percentMem = str(vm()[2]) # RAM percentage used
    totalGB = sz(total) # total disk space in GB
    usedGB = sz(used) # total disk space used in GB
    percentHDD = str(percentHDD) # percentage of disk space used
    uls = round(us, 2)
    dls = round(ds, 2)
    pings = round(pg, 2)
    dlMB = round(dlByte, 2)
    ulMB = round(ulByte, 2)

    ip = '.'.join(ip.split('.')[:2]) + '.xx.xx'

    # variables to  be passed
    sysUP = dt.utcfromtimestamp(bt()).strftime("%Y-%m-%d %H:%M") # sys_info[0] - uptime
    cpuLoadAvg = re(regex, '', cpuLoadAvg) # sys_info[1] - cpu load average
    memStats = usedMem + '/' + totMem + '|' + percentMem + '%' # sys_info[2] - All RAM stats in 1 variable
    netfaces = re(regex, '', netfaces) # sys_info[3] - Network interface not including the loopback interface
    hddStats = usedGB + '/' + totalGB + '|' + percentHDD + '%' # sys_info[4] - All hdd stats in 1 variable
    kernelOS = pl() # sys_info[5] - Kernel version && OS version
    OSN = OSname(pretty=False)
    ul = str(uls) + " Mbps"
    dl = str(dls) + " Mbps"
    ping = str(pings) + " ms"
    ulMBs = str(ulMB) + " MB"
    dlMBs = str(dlMB) + " MB"

    # return as tuple to ensure data integrity
    return (sysUP, cpuLoadAvg, memStats, netfaces, hddStats, kernelOS, ul, dl, ping, isp, share, dlMBs, ulMBs, OSN, ip, free)