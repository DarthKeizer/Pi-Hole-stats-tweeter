# tweetStats

Send a daily tweet with your Pi-Hole statistics!

## How to use

1. `git clone https://github.com/mwoolweaver/tweetStats.git`
2. Install Python 3
3. `pip3 install -U -r requirements.txt`
4. Copy `config.ini.example` to `config.ini` and adjust it `cp config.ini.example config.ini`
   - `api_path` = Path to your `/admin/api.php` of Pi-Hole
   - Tokens: Create an application [here](https://apps.twitter.com/)
5. Run it!
6. ???
7. Profit

## Cronjob

This will tweet your stats at 23:59 everyday and redirects output to /dev/null:

```
59 23 * * * python3 /path/to/pihole_tweeter.py >/dev/null 2>&1
```

# What Does It Mean

 * 🚫🌐 = domains_being_blocked

 * 🈵⁉️  = dns_queries_today

 * 📢🚫 = ads_blocked_today|ads_percentage_today

 * ⁉️⏭  = queries_forwarded

 * ⁉️💾  = queries_cached

 * 🦄🙈 = unique_clients

 * 🔐🎚️ = privacy_level
 
      * domains_being_blocked, dns_queries_today, ads_blocked_today, ads_percentage_today, queries_forwarded, queries_cached, unique_clients, privacy_level - All pulled from [pi-hole/AdminLTE/api.php](https://github.com/pi-hole/AdminLTE/blob/master/api.php)

 * 🆙⏳ = [pretty_time_delta](https://gist.github.com/mwoolweaver/1eb76fbe26d1cda45cd4b7d39cb762a1)([uptime](https://pythonhosted.org/uptime/#uptime.uptime)())

 * ⚖️x̅  = [os.getloadavg](https://docs.python.org/2/library/os.html#os.getloadavg)()
 
      * w/ [regex](https://stackoverflow.com/questions/56153426/regex-for-replacing-special-patterns-in-a-list#comment98942961_56153556) `'lo'(?:,\s*)?|[][')(]|(?:,\s*)?'lo'` to remove unwanted output - [regex test](https://regex101.com/r/IhReCT/4)

 * 🐏📈 = [psutil.virtual_memory()[3] / psutil.virtual_memory()[1] | psutil.virtual_memory()[2]](https://www.programcreek.com/python/example/53871/psutil.virtual_memory)

 * 🔗📡 = [netifaces.interfaces](https://pypi.org/project/netifaces/)()
 
      * w/ [regex](https://stackoverflow.com/questions/56153426/regex-for-replacing-special-patterns-in-a-list#comment98942961_56153556) `'lo'(?:,\s*)?|[][')(]|(?:,\s*)?'lo'` to remove unwanted output - [regex test](https://regex101.com/r/IhReCT/4)

 * 🐧🌽 = [platform.platform](https://docs.python.org/2/library/platform.html#platform.platform)()




# How it looks

```
#ComputeHole: The @The_Pi_Hole on @GoogleCompute       
🚫🌐: 760,159        
🈵⁉: 26,173      
📢🚫: 14,488|55.35%       
⁉⏭: 6,821       
⁉💾: 4,806      
🦄🙈: 3       
🔐🎚: 2       
🆙⏳: 1d 18h 34m 19s      
⚖️x̅: 0.03, 0.08, 0.03       
🐏📈: 469M/1G|38.2%       
🔗📡: ens4, tun0, tun1      
🐧/🌽: Linux-5.0.0-1004-gcp-x86_64-with-Ubuntu-19.10-eoan
```
![example](.github/exampleShot.png)
