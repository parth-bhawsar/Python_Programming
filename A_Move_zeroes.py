num = [0,0,1,2,3,4,0,5,6,0,7]
lenght = len(num)
i=0
while i<lenght:
    if num[i]==0:
        num.remove(num[i])
        num.append(0)

    i+=1
print(num)