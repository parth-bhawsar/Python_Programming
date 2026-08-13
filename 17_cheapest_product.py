products = [
    ("Laptop", 60000),
    ("Mouse", 800),
    ("Monitor", 12000),
    ("Keyboard", 1500)
]
result = min(products,key=lambda x:x[1])
print(result)