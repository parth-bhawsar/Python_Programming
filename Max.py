numbers = [9, 8, 15, 91, 23, 42]
Biggest = numbers[0]
i=0
length = len(numbers)-1
while i<=length:
    if numbers[i]>Biggest:
        Biggest = numbers[i]

    i+=1
print(Biggest)