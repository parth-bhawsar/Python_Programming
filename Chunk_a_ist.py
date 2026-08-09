num = [1,2,3,4,5,6,7,8,9]
k = 3
value = []
for i in range(0,len(num),k):
    value.append(num[i:i+k])
print(value)