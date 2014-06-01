#!/usr/bin/python

__author__ = 'rmuhamedgaliev'

import re
import json
import sys


def get_meminfo():
    re_parser = re.compile(r'^(?P<key>\S*):\s*(?P<value>\d*)\s*kB')
    result = dict()
    for line in open('/proc/meminfo'):
        match = re_parser.match(line)
        if not match:
            continue
        key, value = match.groups(['key', 'value'])
        result[key] = int(value)
    return result


if len(sys.argv) == 3 and float(sys.argv[1]) < float(sys.argv[2]):
    swap_info = get_meminfo()
    total = swap_info['MemTotal']
    used = swap_info['Active']
    free = total - used
    free_percent = (free / total) * 100
    used_percent = 100 - free_percent
    swap = {
        "total": total,
        "used": used,
        "used_percent": "%.2f" % used_percent,
        "free": free,
    }
    if free_percent > float(sys.argv[1]) and free_percent > int(sys.argv[1]):
        print(json.dumps(swap))
        exit(0)
    if free_percent < int(sys.argv[2]):
        print(json.dumps(swap))
        exit(1)
    if free_percent < int(sys.argv[3]):
        print(json.dumps(swap))
        exit(2)
else:
    print(
        "Use argument for work with script.\nSample ./check_memory.py [warning_level] [critical_level]\n./check_memory.py 20 40")
    exit(3)
