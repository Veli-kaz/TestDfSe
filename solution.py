commits = [
    {"author": "Max", "message": "fix bug", "changes": 5},
    {"author": "Anna", "message": "add feature", "changes": 3},
    {"author": "Max", "message": "fix login", "changes": 7}
]

count = 0

for c in commits:
    if "fix" in c["message"]:
        count += 1

print(count)