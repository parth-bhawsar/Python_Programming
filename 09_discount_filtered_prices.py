prices = [100, 250, 80, 400, 150, 50]
discount = 10
filt = list(filter(lambda x:x>100,prices))
mp = list(map(lambda x:x-x*discount/100,filt))
print(mp)