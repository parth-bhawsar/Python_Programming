students = [
    ("Rahul", 85),
    ("Aman", 72),
    ("Priya", 95),
    ("Karan", 60)
]

results = sorted(students,key=lambda x:x[1],reverse=True)
print(results)