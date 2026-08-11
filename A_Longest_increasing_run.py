num =[1,2,3,2,4,5,6,7,3,8,9]
length = len(num)
Current_length = 1
longest_length = 1
i = 1
while i<length:
    if num[i]>num[i-1]:
        Current_length +=1
        if longest_length < Current_length:
            longest_length = Current_length
    else:
        Current_length=1

    i+=1
    
print(longest_length)