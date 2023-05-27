students = [
    {"name" : "Marcus Ledo", "age" : 24, "height" : 1.74},
    {"name" : "Rodrigo Scarlert", "age" : 43, "height" : 1.79},
    {"name" : "Heitor Howls", "age" : 32, "height" : 1.67},
    {"name" : "Hugo Darwin", "age" : 38, "height" : 1.83}
]

for student in students:
    print(f"Name : {student['name']} || Heigth {student['height'] : .2f}")