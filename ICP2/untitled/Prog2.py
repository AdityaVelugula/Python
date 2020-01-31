studentNo = int(input("Enter number of students = "))
weightInLB = [(int(input("Enter weight for student :"))) for x in range(studentNo)]
print(weightInLB);
weightInKG = [("{: .2f}".format(float(weightInLB[i] * 0.453592))) for i in range(studentNo)]
print(weightInKG)