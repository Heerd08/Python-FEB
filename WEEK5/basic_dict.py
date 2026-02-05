records = [
    (1, "alice", ["login", "view", "logout"]),
    (2, "bob", ["login", "view"]),
    (3, "alice", ["login", "purchase"]),
    (4, "david", ["login", "view", "purchase", "logout"]),
]

unique_users = set()
activity_count = {}
user_activity_map = {}
user_total = {}

for record in records:
    user_id = record[0]
    username = record[1]
    activities = record[2]

    # add user
    unique_users.add(username)

    if username not in user_activity_map:
        user_activity_map[username] = []
        user_total[username] = 0

    for activity in activities:
        # count activities
        if activity not in activity_count:
            activity_count[activity] = 0
        activity_count[activity] = activity_count[activity] + 1

        # add activity to user (avoid duplicates)
        if activity not in user_activity_map[username]:
            user_activity_map[username].append(activity)

        user_total[username] = user_total[username] + 1

# sort user activities
for username in user_activity_map:
    user_activity_map[username].sort()

# find most active user
max_count = 0
most_active_user = ""

for username in user_total:
    count = user_total[username]

    if count > max_count:
        max_count = count
        most_active_user = username
    elif count == max_count:
        if username < most_active_user:
            most_active_user = username

result = {
    "unique_users": unique_users,
    "activity_count": activity_count,
    "user_activity_map": user_activity_map,
    "most_active_user": most_active_user
}

print(result)
