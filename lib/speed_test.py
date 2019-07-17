import os
import json

jstring = os.popen("speedtest-cli --json").read()
data = json.loads(jstring)
us = data["upload"]/1000000
ds = data["download"]/1000000
pg = data["ping"]