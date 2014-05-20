__author__ = 'rmuhamedgaliev'

import psutil
import sys
import json
import time

name = "memory_info"


memory = psutil.phymem_usage()

if len(sys.argv) == 3:
    point = {
        "total": memory[0],
        "used": memory[3],
        "avail": memory[1],
        "usage_percent": memory[2],
        "free": memory[4],
    }

    free_percent = 100 - float(memory[2])
    if free_percent > int(sys.argv[1]) and free_percent > int(sys.argv[2]):
        status = {
            "name": name,
            "status": "ok",
            "date": int(round(time.time() * 1000)),
            "info": {
                "partition": point
            }
        }
        print(json.dumps(status))
        exit(0)
    if free_percent < int(sys.argv[1]):
        status = {
            "name": name,
            "status": "warning",
            "date": int(round(time.time() * 1000)),
            "info": {
                "partition": point
            }
        }
        print(json.dumps(status))
        exit(1)
    if free_percent < int(sys.argv[2]):
        status = {
            "name": name,
            "status": "critical",
            "date": int(round(time.time() * 1000)),
            "info": {
                "partition": point
            }
        }
        print(json.dumps(status))
        exit(2)
