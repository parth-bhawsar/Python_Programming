numbers = [12, 5, 8, 21, 30, 17, 40, 3]
result = list(map(
    lambda x: x*x,filter(lambda x : x>10,numbers)
))
print(result)