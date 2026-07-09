import time
# Building a tool for a company that processes network security logs
# Each log line looks like
# 2026-07-08 14:23:01 | user=alice | ip=192.168.1.5 | action=login | status=success
# 2026-07-08 14:23:15 | user=bob | ip=10.0.0.9 | action=login | status=failed
# 2026-07-08 14:23:16 | user=bob | ip=10.0.0.9 | action=login | status=failed
# 2026-07-08 14:23:17 | user=bob | ip=10.0.0.9 | action=login | status=failed
# 2026-07-08 14:24:02 | user=alice | ip=192.168.1.5 | action=logout | status=success

# Write a function find_suspicious_ips(logs) that takes a list of these lines and returns a list of IP
# Ip addresses that had 3 or more failed login attempts

logs = [
    "2026-07-08 14:23:01 | user=alice | ip=192.168.1.5 | action=login | status=success",
    "2026-07-08 14:23:15 | user=bob | ip=10.0.0.9 | action=login | status=failed",
    "2026-07-08 14:23:16 | user=bob | ip=10.0.0.9 | action=login | status=failed",
    "2026-07-08 14:23:17 | user=bob | ip=10.0.0.9 | action=logout | status=failed",
    "2026-07-08 14:23:16 | user=bob | ip=10.0.0.9 | action=login | status=failed",
    "2026-07-08 14:24:02 | user=alice | ip=192.168.1.5 | action=logout | status=success",
    "broken",
]

key = tuple(logs)

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Starting analysis of {len(args[0])} entries")
        result = func(*args, **kwargs)
        print("Finished analysis.")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        result = func(*args, **kwargs)
        after = time.time()
        print(f"Analysis completed in {after-before} seconds")
        return result
    return wrapper

def cache_results(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = tuple(args[0])
        if key in cache:
            print("Using previous result")
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return result
    return wrapper

def require_logs(func):
    def wrapper(*args, **kwargs):
        if args[0] is None or len(args[0]) == 0:
            print("No logs supplied.")
            return []
        
        result = func(*args, **kwargs)
        return result
    return wrapper

def retry(num):
    def decorator_retry(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Attempt {i+1} failed")

                    if i == num-1:
                        raise e
        return wrapper
    return decorator_retry

@retry(5)
@require_logs
@cache_results
@timer
@logger
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
            print(f"Line {line+1} is malformed")
            continue

        if action == 'login' and status == 'failed':
            
            failed_ips[ip] = failed_ips.get(ip, 0) + 1
            if failed_ips[ip] == 3:
                suspicious_ips.append(ip)

    return suspicious_ips

print(find_suspicious_ips(logs))


