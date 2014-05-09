__author__ = 'rmuhamedgaliev'

import subprocess
import re
import time
import sys
import json

name = "check_disk"

p = subprocess.Popen("df", stdout=subprocess.PIPE, shell=True)
dfdata, _ = p.communicate()
dfdata = dfdata.replace("Mounted on", "Mounted_on")

columns = []
output = dfdata.strip(' \t\n\r').split("\n")
for line in range(1, len(output)):
    base_str = re.sub(' +', ' ', output[line]).split(" ")

    if dfdata.find(sys.argv[1]) == -1:
        status = {
            "name": name,
            "status": "unknown",
            "date": time.time(),
            "info": {
                "message": "unknown partitions"
            }
        }
        print(json.dumps(status))
        exit(3)

    if base_str[5] == sys.argv[1]:
        point = {
            "fs": str(base_str[0]),
            "total": base_str[1],
            "used": base_str[2],
            "avail": base_str[3],
            "usage_percent": base_str[4].replace("%", ""),
            "mounted": base_str[5],
        }

        free_percent = 100 - int(base_str[4].replace("%", ""))
        if free_percent > int(sys.argv[2]) and free_percent > int(sys.argv[3]):
            status = {
                "name": name,
                "status": "critical",
                "date": time.time(),
                "info": {
                    "partition": point
                }
            }
            print(json.dumps(status))
            exit(0)
        if free_percent < int(sys.argv[2]):
            status = {
                "name": name,
                "status": "warning",
                "date": time.time(),
                "info": {
                    "partition": point
                }
            }
            print(json.dumps(status))
            exit(1)
        if free_percent < int(sys.argv[3]):
            status = {
                "name": name,
                "status": "critical",
                "date": time.time(),
                "info": {
                    "partition": point
                }
            }
            print(json.dumps(status))
            exit(2)




