employees = [
    ("Rahul", 25000),
    ("Aman", 45000),
    ("Priya", 32000),
    ("Karan", 55000),
    ("Neha", 28000)
]
result = sorted(employees,key=lambda x:x[1],reverse=True)
print(result[0])