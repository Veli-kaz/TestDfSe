commits = [
    {"author": "Max", "message": "fix bug", "changes": 5},
    {"author": "Anna", "message": "add feature", "changes": 3},
    {"author": "Max", "message": "fix login", "changes": 7},
    {"author": "Tom", "message": "update readme", "changes": 2}
]

n = 0

for i in commits:
    if "fix" in i["message"]:
        n += 1

print(n)

changeperauthore = {"Max": 0, "Anna": 0, "Tom": 0}

for i in commits:
    if i["author"] == "Max":
        changeperauthore["Max"] += 1

    elif i["author"] == "Anna":
        changeperauthore["Anna"] += 1

    elif i["author"] == "Tom":
        changeperauthore["Tom"] += 1

print(changeperauthore)


