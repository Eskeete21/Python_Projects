contacts = {
    "number": 4,
    "students": [
        {"name": "Eddie Skeete", "email": "eskeete@mtb.com"},
        {"name": "Josh Allen", "email": "jallen@mtb.com"},
        {"name": "LeBron James", "email": "ljames@mtb.com"}
    ]
}

for student in contacts["students"]:
    print(student["name"])