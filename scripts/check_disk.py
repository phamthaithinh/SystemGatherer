#!/usr/bin/python

__author__ = 'rmuhamedgaliev'

import os
import collections
import sys
import json

_ntuple_diskusage = collections.namedtuple('usage', 'total used free free_percent used_percent')

def get_mount_point(pathname):
    pathname= os.path.normcase(os.path.realpath(pathname))
    parent_device= path_device= os.stat(pathname).st_dev
    while parent_device == path_device:
        mount_point= pathname
        pathname= os.path.dirname(pathname)
        if pathname == mount_point: break
        parent_device= os.stat(pathname).st_dev
    return mount_point

def get_mounted_device(pathname):
    pathname= os.path.normcase(pathname)
    try:
        with open("/proc/mounts", "r") as ifp:
            for line in ifp:
                fields= line.rstrip('\n').split()
                if fields[1] == pathname:
                    return fields[0]
    except EnvironmentError:
        pass
    return None

def get_fs_space(pathname):
    stat = os.statvfs(pathname)
    free = stat.f_bavail * stat.f_frsize
    total = stat.f_blocks * stat.f_frsize
    used = (stat.f_blocks - stat.f_bfree) * stat.f_frsize
    free_percent = (free / total) * 100
    used_percent = 100 - free_percent
    return _ntuple_diskusage(total, used, free, "%.2f" % free_percent, "%.2f" % used_percent)

if len(sys.argv) == 4:
    try:
        disk = get_fs_space(sys.argv[1])
        point = {
            "total": disk[0],
            "used": disk[1],
            "usage_percent": disk[4],
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
