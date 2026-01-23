print("Welcome to advanced Student Grade management system")

user=input("Are you Teacher (T) or a Student (S)?")

student=["Ishan","Rohit","Rohan"]
marks=[1,2,3]
def check_result(student,marks):
    for i in range(len(student)):
        print(student[i], ":-",marks[i]) 
        

def check_topper(marks):
    max=marks[0]
    for i in range (len(marks)):
        if(max<marks[i]):
            max=marks[i]


def add_student(student,marks):
    add_std=input("Enter the Name of the student you want to add!")
    add_stdmks=int(input("Enter the Marks of the Student you want to add!!"))
    student.append(add_std)
    marks.append(add_stdmks)
    print(student)
    print("Student Added!!")

def del_student(student,marks):
    stud=input("Enter the Name of the student who's data you want to delete,permanantly")
    for i in range(len(student)):
            if student[i] == stud:
            # Use pop(i) to remove the element at that position in BOTH lists
                student.pop(i)
                marks.pop(i)
                print(f"Record for {stud} has been deleted.")
                break # Exit the loop once we find and delete them



            



        

        
   
        

if(user=="S"):
    print("Welcome Student!!")
    operations=input("Select operations 1)See result (R) 2)See Topper (T)")
    if(operations=="R"):
        check_result(student,marks)
    if (operations=="T"):
         check_topper(marks)

elif(user=="T"):
    CN=1
    while(CN==1):
     print("Welcome Teacher!!")
     operations=input("Select operations 1)Add Student (A) 2)Delete Student (D)  3)See Result (R)  4) See Topper (T) ")
     if (operations=="A"):
        add_student(student,marks)
     elif(operations=="D"):
        del_student(student,marks)



     elif(operations=="R"):
        check_result(student,marks)
     elif (operations=="T"):
         check_topper(marks)
     cn=input("Do you want to continue? (Y) or (N)")
     if(cn=="N"):
        CN=0
        
        


    
