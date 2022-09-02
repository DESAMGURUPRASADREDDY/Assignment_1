dog=dict()                                     # Create an empty dictionary dog
dog["name"]="Liger"                            # To add name to the dog
dog["color"]="Brown"                           # To add color to the dog
dog["Breed"]="German shepherd"                 # To add breed name to the dog
dog["Legs"]=4                                  # To add no of legs to the dog
dog["age"]=9                                   # To add age to the dog
print(dog)                                     # To print dog

student=dict()                                     # Create an empty dictionary student
student["first_name"]="Guru Prasad Reddy"          # To add first name to the student
student["last_name"]="Desam"                       # To add last name to the student
student["gender"]="Male"                           # To add gender to the student
student["marital status"]="Single"                 # To add marital status to the student
student["skills"]=["C","Java","Scala"]             # To add skills to the student
student["country"]="USA"                           # To add country to the student
student["address"]="4916W 108 Terrace Cambridge"   # To add country to the student
print(student)                                     # To print student
print(len(student))                                # To print length of student
print(student["skills"])                           # To get skills of student
print(type(student["skills"]))                     # To get type of skills of student
student["skills"].extend(["Python","SQL"])           # To modify skils of student
print(student["skills"])                           # To print student skills after modifying
print(student.keys())                              # To get keys of student dictionary as list
print(student.values())                            # To get values of student dictionary as list