#!/usr/bin/python

__author__ = 'rmuhamedgaliev'

import json
import psutil
import sys

process = {}

for pid in psutil.pids():
    process[psutil.Process(pid).name()] = pid

if len(sys.argv) == 2:
    if sys.argv[1] in process:
        result = {
            "name": sys.argv[1],
            "pid": process[sys.argv[1]],
            "status": psutil.Process(process[sys.argv[1]]).status()
        }
        print(json.dumps(result))
        sys.exit(0)
    else:
        result = {
            "name": sys.argv[1],
            "pid": process[sys.argv[1]],
            "status": psutil.Process(process[sys.argv[1]]).status()
        }
        print(json.dumps(result))
        sys.exit(2)
else:
    print(
        "Use argument for work with script.\nSample ./check_process.py process_name\n./check_process.py md")
    exit(3)