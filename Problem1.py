ages=[19,22,19,24,20,25,26,24,25,24]
ages.sort()                              # To sort the list
print(ages)
b=min(ages)                              # To find min of list
c=max(ages)                              # To find max of list
print(b)                                 # Printing min of list
print(c)                                 # Printing max of list
ages.append(b)                           # To add min to list
ages.append(c)                           # To add max to list
print(ages)                              # Printing list after adding min,max
length=len(ages)                         # To find length of list
f=(length-1)//2
median=(ages[f]+ages[f+1])/2             # To find median of list
print(median)                            # To print median
print(sum(ages))                         # To print sum
print((sum(ages)/length))                # To print average
print(c-b)                               # To print range