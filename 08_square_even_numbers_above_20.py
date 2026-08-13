numbers = [5, 12, 18, 21, 24, 31, 36]
results = [x*x for x in numbers if x%2==0 and x>20]
print(results)