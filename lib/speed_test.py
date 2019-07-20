import os
import json
import math

jstring = os.popen("speedtest-cli --share --json").read()
data = json.loads(jstring)
client = data["client"]
server = data["server"]

print(data)
print("\nclient\n")
print(client)
print("\nISP\n")
print(client["isp"])
print(data["share"])

ulByte = data["bytes_sent"]/1024/1024
print(ulByte)

dlByte = data["bytes_received"]/1024/1024
print(str(dlByte))


us = data["upload"]/1000000
ds = data["download"]/1000000
pg = data["ping"]
isp = client["isp"]
share = data["share"]