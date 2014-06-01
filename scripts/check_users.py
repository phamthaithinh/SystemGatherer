__author__ = 'rmuhamedgaliev'

import json
import sys
import psutil

def users_check():
    result = []
    for user in psutil.get_users():
        result.append(
            {
                "name": user[0],
                "time": user[3]
            }
        )
        return result

if len(sys.argv) == 3 and int(sys.argv[1]) < int(sys.argv[2]):
    users = users_check()
    if len(users) < int(sys.argv[1]):
        print(json.dumps(users))
        sys.exit(0)
    elif len(users) > int(sys.argv[1]):
        print(json.dumps(users))
        sys.exit(1)
    elif len(users) > int(sys.argv[2]):
        print(json.dumps(users))
        sys.exit(1)
else:
    print(
        "Use argument for work with script.\nSample ./check_users.py [warn_count_users] [critical_count_users]\n./check_users.py 3 10")
    exit(3)

