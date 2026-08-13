employees = [
    ("Rahul", 25000),
    ("Aman", 45000),
    ("Priya", 32000),
    ("Karan", 55000),
    ("Neha", 28000)
]
result = any(x[1]>50000 for x in employees )
result2 = all(x[1]>20000 for x in employees )
print(result)
print(result2)