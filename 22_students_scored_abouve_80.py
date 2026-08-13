students = [
    ("Rahul", 72),
    ("Aman", 91),
    ("Priya", 84),
    ("Karan", 67),
    ("Neha", 95)
]

result = sorted(students,key=lambda x: x[1], reverse=True
                )
result2 = list(filter(lambda x:x[1]>=80,result))
result3 = [x[0] for x in result2]
print(result3)