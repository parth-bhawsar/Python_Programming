import random

num = []
element = 90
for i in range(element):
    num.append(random.randint(1, 100))

print(num)
even =[]
odd =[]
j=0
while j<element:
    if num[j]%2==0:
       even.append(num[j])
    else:
       odd.append(num[j])

    j+=1
print("Even List:",even)
print("Odd List:",odd)