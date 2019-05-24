# tweetStats

Send a daily tweet with your Pi-Hole statistics and other system information!

## How to use

1. `git clone https://github.com/mwoolweaver/tweetStats.git`
2. Install Python 3
3. `pip3 install -U -r requirements.txt`
4. Copy `config.json.example` to `config.json` and adjust it `cp config.json.example config.json`
   - `api_path` = Path to your `/admin/api.php` of Pi-Hole
   - Tokens: Create an application [here](https://apps.twitter.com/)
5. Run it! `python3 tweetStats.py` `python3 tweetStats.py -h` -> for help
6. ???
7. Profit

## cmd line args for testing

  *  -db will print the tweet to be sent and all other variables that are used in the proccess.

  *  -dbl will test your twitter credentials to test a successful login.

  *  -dbp will make sure the pi-hole api can be reached. 

## Cronjob

This will tweet your stats at 23:55 everyday and redirects output to ~/tweetStats/tweetStats.txt so you know that it actually worked.

```
55 23 * * * root cd ~/tweetStat/ && python3 tweetStat.py >> ~/tweetStat/twitter_bot.txt
```

# What Does It Mean

 * 🚫🌐 = domains_being_blocked

 * 🈵⁉️  = dns_queries_today

 * 📢🚫 = ads_blocked_today|ads_percentage_today

 * ⁉️⏭  = queries_forwarded

 * ⁉️💾  = queries_cached

 * 🦄🙈 = unique_clients

 * 🔐🎚️ = privacy_level
 
 * 🚫📝⌛ = gravity_last_updated

      * domains_being_blocked, dns_queries_today, ads_blocked_today, ads_percentage_today, queries_forwarded, queries_cached, unique_clients, privacy_level, gravity_last_updated  - All pulled from [pi-hole/AdminLTE/api.php](https://github.com/pi-hole/AdminLTE/blob/master/api.php) - the default path is -> http://localhost:8080/admin/api.php and should work if you are running the python script from the machine hosting Pi-hole

 * ⚖️x̅  = [psutil.getloadavg()](https://psutil.readthedocs.io/en/latest/#psutil.getloadavg)() - will not show the `loopback` interface.

     * w/ [regex](https://stackoverflow.com/questions/56153426/regex-for-replacing-special-patterns-in-a-list#comment98942961_56153556) `'lo'(?:,\s*)?|[][')(]|(?:,\s*)?'lo'` to remove unwanted characters - [regex test](https://regex101.com/r/IhReCT/4)

 * 🐏📈 = [psutil.virtual_memory()[3] / psutil.virtual_memory()[1] | psutil.virtual_memory()[2]](https://www.programcreek.com/python/example/53871/psutil.virtual_memory)

 * 🔗📡 = [netifaces.interfaces()](https://pypi.org/project/netifaces/)()
 
      * w/ [regex](https://stackoverflow.com/questions/56153426/regex-for-replacing-special-patterns-in-a-list#comment98942961_56153556) `'lo'(?:,\s*)?|[][')(]|(?:,\s*)?'lo'` to remove unwanted characters - [regex test](https://regex101.com/r/IhReCT/4)

 * 💾📊 = [shutil.disk_usage("/")](https://docs.python.org/3/library/shutil.html#shutil.disk_usage)

 * 🐧🌽 = [platform.platform()](https://docs.python.org/2/library/platform.html#platform.platform)()

 * 🖥️👢⏳ = [datetime.utcfromtimestamp](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp)([psutil.boot_time](https://psutil.readthedocs.io/en/latest/#psutil.boot_time)()).[strftime](https://www.programiz.com/python-programming/datetime/strftime)("%Y-%m-%d %H:%M")


# How it looks

```
🚫🌐: 811,593
🈵⁉: 22,636
📢🚫: 10,520|46.47%
⁉⏭: 6,436
⁉💾: 5,680
🦄🙈: 5
🔐🎚: 2
🚫📝⌛: 2019-05-19 08:37
⚖️x̅: 0.0, 0.0, 0.0
🐏📈: 504M/1004M|40.5%
🔗📡: ens4, tun0, tun1
💾📊: 9G/28G|32.14%
🐧🌽: Linux-5.0.0-1006-gcp-x86_64-with-Ubuntu-19.10-eoan
🖥️👢⏳: 2019-05-19 03:40
```
![example](.github/exampleShot.png)
