students = [
    ("Rahul", 78),
    ("Aman", 92),
    ("Priya", 65),
    ("Karan", 88),
    ("Neha", 95)
]

reslut = {x[0]:x[1] for x in students if x[1]>=80}
print(reslut)