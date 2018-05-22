#user defined input
#A= P(1+rt)
# input: p = 100, rate = 2, period = 5
principle = float(input("Enter Principle: "))
rate = float(input("Enter Rate of Interest (%): "))
period = float(input("Enter Time period: "))

amount = 0 #minimal value of amount
year = 1   #minimal investment duration

while year <= period: #compare given period with min yr value
    #calculation as it is going to store
    amount = principle*(1 + (rate/100) * year)
    print("%d st Year Amount is %.2f" %(year,amount))
    # To increment amount as per SI
    principle = amount
    # counter of year will increment
    year += 1

#print("Amount = %.0f \nInterest rate = %.0f \nPeriod = %.0f \nValue = %.0f \nYear = %.0f"%(amount,inrate,period,value,year))
