numbers = [5, 12, 7, 20, 31, 18, 40, 9, 50]
result = {x:x*x for x in numbers if x%2==0 and x>10}
print(result)