#!/usr/bin/python

__author__ = 'rmuhamedgaliev'

import os
import collections
import sys
import json

_ntuple_procusage = collections.namedtuple('loadvg', 'one three five')


def get_proc_avg():
    stat = os.getloadavg()
    return _ntuple_procusage(stat[0], stat[1], stat[2])


def check_normal(one, three, five):
    if (one < float(sys.argv[1])) and (three < float(sys.argv[1])) and (five < float(sys.argv[1])):
        return 0


def check_warning(one, three, five):
        if (one > float(sys.argv[1])) or (three > float(sys.argv[1])) or (five > float(sys.argv[1])):
            return 1


def check_critical(one, three, five):
            if (one > float(sys.argv[2])) or (three > float(sys.argv[1])) or (five > float(sys.argv[2])):
                return 2

if len(sys.argv) == 3 and float(sys.argv[1]) < float(sys.argv[2]):
    avg = get_proc_avg()
    point = {
        "one": avg[0],
        "three": avg[1],
        "five": avg[2]
    }
    if check_normal(avg[0], avg[1], avg[2]) == 0:
        print(json.dumps(point))
        exit(0)
    if check_warning(avg[0], avg[1], avg[2]) == 1:
        print(json.dumps(point))
        exit(1)
    if check_critical(avg[0], avg[1], avg[2]) == 2:
        print(json.dumps(point))
        exit(2)
else:
    print("Use argument for work with script.\nSample ./check_load.py [warning_level] [critical_level]\n./check_load.py 3 5")
    exit(3)
