logs = [
    "user=bob action=logout",
    "user=alice action=login"
]

def most_active_user(logs):
    users = {}
    for line in logs:
        split_line = line.split(' ')
        user = (split_line[0].split('='))[1]
        users[user] = users.get(user, 0) + 1
        most_active = max(users, key=users.get)

    for user, count in users.items():
        if count == users[most_active] and user < most_active:
            most_active = user
        else:
            continue

    return most_active

        

print(most_active_user(logs))

