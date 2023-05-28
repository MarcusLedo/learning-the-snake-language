students = []

with open("names_ages.csv") as file:
    for line in file:
        name, age = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["age"] = age
        students.append(student)

def get_name(student):
    return student['name']

for student in sorted(students, key = get_name):
    print(f"Name: {student['name']}     Age: {student['age']}")