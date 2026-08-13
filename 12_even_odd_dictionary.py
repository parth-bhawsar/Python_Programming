numbers = [4, 7, 12, 15, 20, 23, 30, 31]
result = {x:"Even" if x%2==0 else "Odd" for x in numbers if x>10}
print(result)