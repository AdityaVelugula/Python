from itertools import combinations
n = int(input("Enter number of elements : "))
lis=[]
for i in range(0, n):
    ele = int(input())
    lis.append(ele)

output = set()
for i in range(1, len(lis) +1):
    oc = list(combinations(lis, i))
    output.update(oc)
print(output)
