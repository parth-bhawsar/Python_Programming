products = [
    ("Laptop", 60000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Headphones", 3000)
]
reslut = {x[0]:x[1]-x[1]*10/100 for x in products if x[1]>=2000}
print(reslut)