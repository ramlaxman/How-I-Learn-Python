basic_salary = 1000
bonus_rate = 100
commission_rate = 0.01

number_of_camera = (int(input("Enter the number of cameras: ")))
price =(float(input("Enter the price for one camera: ")))

bonus = (bonus_rate * number_of_camera)
commission = (commission_rate * number_of_camera * price)

#spacing is very important inside double quoted columns.

print("Bonus        =   %6.2f" % bonus)
print("Commission   =   %6.2f" % commission)
print("Gross salary =   %6.2f" % (basic_salary + bonus + commission))