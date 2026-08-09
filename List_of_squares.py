import random

num = []
element = 90
for i in range(element):
    num.append(random.randint(1, 100))

print(num)
sq=[]
j=0
while j<element:
    sq.append(num[j]*num[j])
    j+=1
print(sq)