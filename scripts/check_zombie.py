#!/usr/bin/python

__author__ = 'rmuhamedgaliev'

import json
import psutil
import sys

process = {}

for pid in psutil.pids():
    if (psutil.Process(pid).status() == psutil.STATUS_ZOMBIE):
        process[psutil.Process(pid).name()] = pid

if len(sys.argv) == 2:
    if len(process) > 0:
        result = []
        for pc, pid in process.items():
            result.append(
                {
                    "name": pc,
                    "pid": pid,
                    "status": psutil.Process(process[pid]).status()
                }
            )
        print(json.dumps(result))
        sys.exit(2)
    else:
        result = {
            "name": "",
            "pid": "",
            "status": "OK"
        }
        print(json.dumps(result))
        sys.exit(0)
else:
    print(
        "Use argument for work with script.\nSample ./check_zombie.py\n./check_zombie.py")
    exit(3)