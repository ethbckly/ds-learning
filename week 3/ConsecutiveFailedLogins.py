logs = [
    "user=alice status=success",
    "user=alice status=failed",
    "user=alice status=failed",
    "user=alice status=success",
    "user=alice status=failed",
    "user=bob status=failed",
    "user=bob status=failed",
    "user=bob status=failed",
]

def find_locked_accounts(logs):
    failed_logins = {}
    locked_accounts = []
    for line in logs:
        split_line = line.split(' ')
        user, status = (split_line[0].split('='))[1], (split_line[1].split('='))[1]
        print(user, status)
        if status == 'failed':
            failed_logins[user] = failed_logins.get(user, 0) + 1
            if failed_logins[user] == 3:
                locked_accounts.append(user)
        if status == 'success':
            failed_logins[user] = 0
    return locked_accounts

print(find_locked_accounts(logs))