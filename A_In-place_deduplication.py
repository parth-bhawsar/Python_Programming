sl = [1,1,1,2,2,3,4,4,4,5,5,6,7]
i=0
while i < len(sl)-1:
    if sl[i]==sl[i+1]:
        sl.remove(sl[i])
    else: 
        i+=1
print(sl)