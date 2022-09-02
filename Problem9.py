studentWtlist=list()                               # creating an empty list for students weight
n=int(input("Enter no of students: "))             # To read input from user for no of students
for i in range(n):
    studentwt=float(input("Enter weight of student " +str(i+1)+": ")) # To get weight of student from user
    studentWtlist.append(studentwt*0.454)          # To convet weight to kilogram from lbs
a=['%.2f' % elem for elem in studentWtlist]        # converting the values not more than 2 precision values
print(a)                                           # printing the values of weight in kilograms