numbers = [5, 12, 18, 7, 20, 25, 30, 40]
result = max((map(lambda x:x*x,filter(lambda x:x%2==0 and x>10,numbers))))
print(result)