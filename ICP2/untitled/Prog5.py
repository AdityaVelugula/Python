lst = []
lst2 = []
# number of elements as input
n = int(input("Enter number of students : "))
print("Please enter weights")
# iterating till the range
for i in range(0, n):
    ele = int(input())
# adding the element
    lst.append(ele)

for i in lst:
    kgs = ("{: .2f}".format(float(i * 0.453592)))
    lst2.append(kgs)

print("Convert list of weights in Kilograms",lst2)