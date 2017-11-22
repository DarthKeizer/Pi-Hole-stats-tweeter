# Pi-Hole stats tweeter
Send a daily tweet with your Pi-Hole statistics!

# How to use
1. Install Python 3
2. `pip install -U - r requirements.txt`
3. Copy config.ini.example to config.ini and adjust it
  3.1. `api_path` = Path to your /admin/api.php of Pi-Hole
  3.2. Tokens: Create an application [here](https://apps.twitter.com/)
4. Run it!

# Cronjob
This will tweet your stats at 23:59 everyday and redirects output to /dev/null:

```
59 23 * * * python3 /path/to/pihole_tweeter.py >/dev/null 2>&1
```
