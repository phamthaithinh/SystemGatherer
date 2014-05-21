__author__ = 'rmuhamedgaliev'

import time
import sys
import json
import os

import psutil

name = "check_disk"

if len(sys.argv) == 4:
    try:
        disk = psutil.disk_usage(sys.argv[1])
        point = {
            "total": disk[0],
            "used": disk[1],
            "usage_percent": disk[3],
            "free": disk[2],
        }
        free_percent = 100 - float(disk[3])
        if free_percent > float(sys.argv[2]) and free_percent > int(sys.argv[3]):
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
        if free_percent < int(sys.argv[2]):
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
        if free_percent < int(sys.argv[3]):
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
    except FileNotFoundError:
        status = {
            "name": name,
            "status": "unknown",
            "date": int(round(time.time() * 1000)),
            "info": {
                "message": "unknown path"
            }
        }
        print(json.dumps(status))
        exit(3)




