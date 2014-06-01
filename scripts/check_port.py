#!/usr/bin/python

__author__ = 'rmuhamedgaliev'

import socket
import sys
import json


def check_server(address, port):
    s = socket.socket()
    print("Attempting to connect to %s on port %s" % (address, port))
    try:
        s.connect((address, port))
        print("Connected to %s on port %s" % (address, port))
        s.close()
        return True
    except socket.error as e:
        print("Connection to %s on port %s failed: %s" % (address, port, e))
        s.close()
        return False


if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = sys.argv[2]
    result = check_server(ip, int(port))
    if result:
        output = {
            "port": port,
            "ip": ip,
            "status": result
        }
        print(json.dumps(output))
        sys.exit(0)
    else:
        output = {
            "port": port,
            "ip": ip,
            "status": result
        }
        print(json.dumps(output))
        sys.exit(2)
else:
    print(
        "Use argument for work with script.\nSample ./check_port.py [ip] [port] [critical_level]\n./check_port.py 127.0.0.1 22")
    exit(3)


