__author__ = 'rmuhamedgaliev'

import subprocess
import re
import json

name = "check_disk"

p = subprocess.Popen("df -h", stdout=subprocess.PIPE, shell=True)
dfdata, _ = p.communicate()

dfdata = dfdata.replace("Mounted on", "Mounted_on")

columns = []
output = dfdata.strip(' \t\n\r').split("\n")
for line in range(1, len(output)):
    base_str = re.sub(' +', ' ', output[line]).split(" ")
    point = {
        "fs": str(base_str[0]),
        "total": base_str[1],
        "used": base_str[2],
        "avail": base_str[3],
        "usage_percent": base_str[4],
        "mounted": base_str[5],
    }
    columns.append(point)

print(json.dumps(columns))