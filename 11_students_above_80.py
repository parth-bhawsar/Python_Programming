students = [
    ("Rahul", 78),
    ("Aman", 92),
    ("Priya", 65),
    ("Karan", 88),
    ("Neha", 95)
]
new = [x[0] for x in students if x[1]>80]
print(new)