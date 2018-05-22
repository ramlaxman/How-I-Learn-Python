print("Welcome to Average Calculation Program!\n")

# user input for total numbers 
total_nos = int(input("Enter Total Numbers for which you want to calculate sum & avg: "))
# sum for total and counter for increment/decrement of operation
sum = counter = 0

#To avoid retyping each time
print("Enter Only Integers:")

# while means जोपर्यंत
while counter < total_nos:
    numbers = int(input(""))
    sum = sum + numbers
    counter = counter + 1
average = float(sum)/total_nos
print("Total numbers are= %d Sum = %d Avg = %.2f" %(total_nos, sum, average))










'''#!/usr/bin/env python3
# input of total numbers for calculation
N = 2
# sum of total numbers
sum = 0
# total count of numbers
count = 0

while count < N:
    number = float(input(""))
    sum = sum + number
    count = count + 1
average = float(sum)/N
print("N = %d, sum = %.1f" %( N, sum ))
print("average = %.1f" %average)'''