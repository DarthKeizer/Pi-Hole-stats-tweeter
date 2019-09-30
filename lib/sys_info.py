#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# retreive data for system information

def sys_info():
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
    
 
    regex = r"'lo'(?:,\s*)?|[][')(]|(?:,\s*)?'lo'" # modified suggestion from https://stackoverflow.com/questions/56153426/regex-for-replacing-special-pa>
    total, used, free = du("/") # Get disk stats - we only use 2 of these but the function requires all 3 (total, used, free)
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
    OSN = OSname(pretty=False) # get OS name

    # variables to  be passed
    cpuLoadAvg = re(regex, '', cpuLoadAvg) # cpu load average
    memStats = usedMem + '/' + totMem + '|' + percentMem + '%' # All RAM stats in 1 variable
    hddStats = usedGB + '/' + totalGB + '|' + percentHDD + '%' # All hdd stats in 1 variable
    netfaces = re(regex, '', netfaces) # Network interface not including the loopback interface
    kernelOS = pl() # Kernel version && OS version
    sysUP = dt.utcfromtimestamp(bt()).strftime("%Y-%m-%d %H:%M") # uptime in your local time
    oSn = OSN.split(' ', 1)[0] # make OS name pretty

    # return as tuple to ensure data integrity
    return (cpuLoadAvg, memStats, hddStats, netfaces, kernelOS, sysUP, oSn, free)
