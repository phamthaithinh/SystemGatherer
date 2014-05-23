#!/usr/bin/python3

__author__ = 'rmuhamedgaliev'

import psutil
import sys
import json
import time

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
        print(json.dumps(point))
        exit(0)
    if free_percent < int(sys.argv[1]):
        print(json.dumps(point))
        exit(1)
    if free_percent < int(sys.argv[2]):
        print(json.dumps(point))
        exit(2)
else:
    print("Use argument for work with script.\nSample ./check_memory.py [warning_level] [critical_level]\n./check_memory.py 20 40")
    exit(3)
