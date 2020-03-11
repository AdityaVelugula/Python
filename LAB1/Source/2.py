from collections import OrderedDict
n = int(input("enter a n value for dictionary 1 :"))
d1 = {}
d2={}
for i in range(n):
    print("Enter the key value:")
    keys = input() # here i have taken keys as strings
    print("Enter the value for the key")
    values = int(input()) # here i have taken values as integers
    d1[keys] = values
n1 = int(input("enter a n value for dictionary 2 :"))
for i in range(n1):
    print("Enter the key value:")
    keys = input() # here i have taken keys as strings
    print("Enter the value for the key")
    values = int(input()) # here i have taken values as integers
    d2[keys] = values
print("*printing dictionary1**")
print(d1)
print("*printing dictionary2**")
print(d2)
m3={k:v for d in[d1,d2] for k,v in d.items()}
print("**dictionaries after concatenation**")
print(m3)
sortedDict = OrderedDict(sorted(m3.items(), key=lambda x: x[1]))
print("**Dictinories after sorting by value*")
print(sortedDict)