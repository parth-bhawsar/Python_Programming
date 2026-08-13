numbers = [12, 5, 18, 7, 30, 21, 40, 91] 
result = max(filter(lambda x:x%2==0 and x>10,numbers)) 
print(result)