numbers = list(map(int, input("Enter numbers: ").split()))

j = 0

while j < len(numbers):
    if numbers[j] in numbers[:j]:
        numbers.pop(j)
    else:
        j += 1

print(numbers)