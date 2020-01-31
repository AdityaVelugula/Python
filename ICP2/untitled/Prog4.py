lst = []
# number of elements as input
n = int(input("Enter number of students : "))
print("Please enter weights")
# iterating till the range
for i in range(0, n):
    ele = int(input())
# adding the element
    lst.append(ele)

# printing the list
print("Given the list of weights in the lbs(pounds)",lst)
# converting the student weights from Lbs to Kgs
kgs = [("{: .2f}".format(float(i * 0.453592)))for i in lst]
print("Convert list of weights in Kilograms",kgs)