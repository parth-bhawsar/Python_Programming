numbers = [90, 8, 15, 1, 23, 42]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)