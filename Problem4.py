it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]
print(len(it_companies))                            # To print length of it_companies
it_companies.add("Twitter")                         # To add twitter to set of it_companies
print(it_companies)                                 # To print set of it_companies after adding twitter
it_companies1={"TCS","Wipro","Infosys","Capgemini"}
it_companies.update(it_companies1)                  # To add another set of companies to it_companies
print(it_companies)
it_companies.remove("Wipro")                        # To remove one company from set of it_companies
print(it_companies)                                 # To print set of it_companies after removing one company

# Difference between remove() and discard() methods are remove will raise an error when the specified element
# doesn't exists whereas discard will not throw error.

print(A.union(B))                                   # To join A and B
print(A.intersection(B))                            # Intersection of A & B
print(A.issubset(B))                                # To find A is subset of B
print(A.isdisjoint(B))                              # To find A is disjoint of B
print(A.union(B))                                   # To find A union B
print(B.union(A))                                   # To find B union A
print(A.symmetric_difference(B))                    # To find symmetric diff b/w A and B
A.clear()
print(A)                                            # To clear set A
B.clear()
print(B)                                            # To clear set B
ageset=set(age)                                     # To convert list to set
print(ageset)                                       # To print set
listlength=len(age)                                 # To find length of list
print(listlength)                                   # To print length of list age
setlength=len(ageset)                               # To find length of set
print(setlength)                                    # To print length of set

# Length of the set is less than list because duplicate elements are removed.