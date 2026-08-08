n=[1,1,2,3,4,5,6,7,8,9]
i=0
while i < 9:
  if n[i] in n[:i]:
    n.pop(i)
  else:
    i+=1
print(n)