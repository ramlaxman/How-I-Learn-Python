days = int(input("Enter days:"))
year = days / 365
month = days / 30
days = days % 365

print("year = %d month = %d days = %d" %(year, month, days))