products = [
    ("Laptop", 1300),
    ("Mouse", 800),
    ("Monitor", 12000),
    ("Keyboard", 1500),
    ("Phone", 30000)
]
result = [x for x in products if x[1]>1000]
result2 = min(result, key=lambda x: x[1])
print(result2)