numbers = [12, 18, 24, 30, 36]
result1 = any(x>35 for x in numbers)
result2 = all(x%6==0 for x in numbers)
print(result1)
print(result2)