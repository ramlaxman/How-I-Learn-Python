#program to reverse tuples order
data = ("Ram Bhosale","india", "Python")
# For understanding, name, country, language =  data
print(data)
reverse = reversed(data)
print(tuple(reverse))		#reverse is not keywords

'''# how to reverse list
for i in reversed(data):
    print(i)
list(reversed((data)))'''