# 🔥 Problem Statement
# You are given a list of students and their marks.
# Write a program that provides the following menu (in loop):
# Show all students with marks
# Find Topper
# Search student by name
# Add new student + marks
# Remove a studen
# Exit

# 🧩 Skills This Task Test
# Building a clean function-based program
# Updating list data
# Searching
# Using loops
# Using enumerate(
# String & number handling
# Real-world logic structuring

students=["A","B","C","D","E","F"]
marks=[60,76,45,57,84,75]


def showstudents(students,marks):
    print(students)
    print(marks)


def topper(students,marks):
    toppermark=marks[0]
    index=0
    topperstudent=students[0]
    for i in range(len(marks)):
        if(marks[i]>toppermark):
            toppermark=marks[i]
            topperstudent=students[i]
    return topperstudent,toppermark


def search(students,marks):
    index=0
    marksearch=0
    studentsrch=0
    found=0
  
    name=input("Give me the name of the student you wanna search")
    for i, std in enumerate(students):
        if std == name:
            index = i
            marksearch = marks[i]
            studentsrch = students[i]
            found = 1
            break # Stop searching once found
            
    return marksearch, index, studentsrch, found # Send data back!



def addstud(students,marks):
    studentnew=input("Tell me the Name of The student you want to add")
    marksnew=input("Tell me the marks of this new student")
    students.append(studentnew)
    marks.append(marksnew)
    
    




while True:
    print("Welcome to Student Database")
    menuch=int(input("Choose the operation\n" 
     "1)Display all students\n" \
     "2)Find Topper\n" \
     "3)Search for a student\n" \
     "4)Add new student and marks\n" \
     "5)exit"))
    
    if(menuch==1):
        displ=showstudents()
        print(displ)
    elif(menuch==2):
        topperstud,toppermarks=topper(students,marks)
        print(topperstud)
        print(toppermarks)
    elif(menuch==3):
        marksrch,ind,stdsrch,fd=search(students,marks)
        if(fd==1):
            print("Found at ",ind)
            print(marksrch)
            print(stdsrch,"\n")
        else:
            print("NOT FOUND!!\n")
    elif (menuch==4):
        addstud(students,marks)
        print(students)
        print(marks)

        




    elif(menuch==5 ):
        break
    else:
        print("Invalid Option choice")








