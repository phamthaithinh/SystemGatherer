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


if len(sys.argv) == 2 and float(sys.argv[1]) < float(sys.argv[2]):
    swap_info = get_meminfo()
    swap_used = swap_info['SwapTotal'] - swap_info['SwapFree']
    free_percent = (swap_info['SwapFree'] / swap_info['SwapTotal']) * 100
    used_percent = 100 - free_percent
    swap = {
        "total": swap_info['SwapTotal'],
        "used": swap_used,
        "used_percent": "%.2f" % used_percent,
        "free": swap_info['SwapFree'],
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
        "Use argument for work with script.\nSample ./check_swap.py [warning_level] [critical_level]\n./check_swap.py 20 40")
    exit(3)
