employees = [
    ("Rahul", 25000),
    ("Aman", 35000),
    ("Priya", 22000),
    ("Karan", 45000),
    ("Neha", 30000)
]

reslut = {x[0]:x[1] for x in employees if x[1]>=30000}
print(reslut)