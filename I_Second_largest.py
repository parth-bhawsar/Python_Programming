num = [1,32,2,3,43,34,45,54,4]

largest = 0
second= 0
for i in num:
    if i>largest:
         second = largest
         largest = i
    elif i> second and i!= largest:
        second = i
print("Largest:",largest)
print("Secound Largest:",second)
