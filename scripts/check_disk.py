#!/usr/bin/python3

__author__ = 'rmuhamedgaliev'

import sys
import json
import psutil

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
            print(json.dumps(point))
            exit(0)
        if free_percent < int(sys.argv[2]):
            print(json.dumps(point))
            exit(1)
        if free_percent < int(sys.argv[3]):
            print(json.dumps(point))
            exit(2)
    except FileNotFoundError:
        status = {
            "message": "unknown path"
        }
        print(json.dumps(status))
        exit(3)
else :
    print("Use argument for work with script.\nSample ./check_disk.py [path] [warning_level] [critical_level]\n./check_disk.py / 20 40")
    exit(3)




