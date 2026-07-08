# Building a tool for a company that processes network security logs
# Each log line looks like
# 2026-07-08 14:23:01 | user=alice | ip=192.168.1.5 | action=login | status=success
# 2026-07-08 14:23:15 | user=bob | ip=10.0.0.9 | action=login | status=failed
# 2026-07-08 14:23:16 | user=bob | ip=10.0.0.9 | action=login | status=failed
# 2026-07-08 14:23:17 | user=bob | ip=10.0.0.9 | action=login | status=failed
# 2026-07-08 14:24:02 | user=alice | ip=192.168.1.5 | action=logout | status=success

# Write a function find_suspicious_ips(logs) that takes a list of these lines and returns a list of IP
# Ip addresses that had 3 or more failed login attempts

logs1 = [
    "2026-07-08 14:23:01 | user=alice | ip=192.168.1.5 | action=login | status=success",
    "2026-07-08 14:23:15 | user=bob | ip=10.0.0.9 | action=login | status=failed",
    "2026-07-08 14:23:16 | user=bob | ip=10.0.0.9 | action=login | status=failed",
    "2026-07-08 14:23:17 | user=bob | ip=10.0.0.9 | action=logout | status=failed",
    "2026-07-08 14:23:16 | user=bob | ip=10.0.0.9 | action=login | status=failed",
    "2026-07-08 14:24:02 | user=alice | ip=192.168.1.5 | action=logout | status=success",
    "broken",
]

logs = []


def find_suspicious_ips(logs):
    '''
    Function that splits each log into ip, status and action results,
    detects whether ips have failed a login three times, if so adds to a suspicious ip list.

    Returns suspicious_ips: list
    '''


    failed_ips = {}
    suspicious_ips = []
    for line in range(len(logs)):

        try:
            split_string = logs[line].split('|')
            ip, status, action = split_string[2].split('='), split_string[4].split('='), split_string[3].split('=')
            ip, status, action = ip[1].strip(), status[1].strip(), action[1].strip()

        except IndexError:
            print(f"Line {line} is malformed")
            continue

        if action == 'login' and status == 'failed':
            
            failed_ips[ip] = failed_ips.get(ip, 0) + 1
            if failed_ips[ip] == 3:
                suspicious_ips.append(ip)

    return suspicious_ips


print(find_suspicious_ips(logs))