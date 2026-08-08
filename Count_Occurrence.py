import random

num = []

for i in range(900):
    num.append(random.randint(1, 100))

print(num)
length = len(num)-1
value = int(input("Enter number = "))
i = 0
count = 0
while i <= length:

    if value == num[i]:
        count += 1

    i += 1
print(count)
