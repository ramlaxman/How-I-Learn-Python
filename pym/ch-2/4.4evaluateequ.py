sum = 0.0
print(" i\t sum")
for i in range(1, 11):
    sum += 1.0 / i
    print("%2d %6.1f" % (i , sum))

'''
#using while loop
sum = 0.0
i = 1 
while i < 11:
    sum += 1.0 / i
    print("%2d %6.1f" % (i , sum))
    i +=1
'''