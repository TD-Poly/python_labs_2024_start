import json

with open("students.json", "r") as f:
    data = json.load(f)

students = data["students"]

for student in students:
    print(f'ID: {student["id"]}')
    print(f'Name: {student["name"]}')
    print(f'Age: {student["age"]}')
    print(f'Math: {student['grades']["math"]}')
    print(f'Science: {student['grades']["science"]}')
