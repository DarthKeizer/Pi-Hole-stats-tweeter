import os
import urllib.request, json
import math
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

address = "http://api.ipstack.com/" + ip + "?access_key=" + key + "&output=json&fields=city"

print(address)

with urllib.request.urlopen(address) as url:
    city = json.loads(url.read().decode())['city']

print(city)