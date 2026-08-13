students = [
    ("Rahul", 78),
    ("Aman", 92),
    ("Priya", 65),
    ("Karan", 88),
    ("Neha", 95)
]
result = max(students,key=lambda x:x[1])[0]
print(result)