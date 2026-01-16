# print("let's start to make dictionary")

# student={
#     "name":"Ishan",
#     "Course":"Python with ML",
#     "Age":"20"

# }

# print(student["name"])

# student["city"]="pune"

# # print(student.get("name"))
# print(student)

print("Welcome to Employee management system with use of Dictionary")

Employee={
    "Engineer":{
        "101":{
            "Name":"Ashok",
            "Salary (in LPA)":"12.5"
        }
        
    },

    "Management":{
         "201":{
            "Name":"Arvind",
            "Salary (in LPA)":"10.5"
        }

    },

    "others":{
         "301":{
            "Name":"Aditya",
            "Salary (in LPA)":"9.5"
        }

    }
}




def add_employee():
    department=input("In which department do you want to add Employee (E) for Engineering,(M) for Management,(O) for others such as other supporting staff..")
    if(department=="E"):
        dep="E"
    elif(department=="M"):
        dep="M"
    elif(department=="O"):
        dep="O"
    else:
        print("Wrong Department Key!!")
        
    if department:
        addid=input("Enter the Id of the Employee you want to add (IMP:-plz use display function to see ID's till now to keep the DB precise)")
        addname=input("Enter the employee's name u want to add")
        addsal=float(input("Enter the Salary of that employee (in LPA)"))
        if(dep=="E"):
            Employee["Engineer"][addid]={"Name":addname, "Salary (in LPA)":addsal}
        elif(dep=="M"):
            Employee["Management"][addid]={"Name":addname, "Salary (in LPA)":addsal}
        elif(dep=="O"):
            Employee["others"][addid]={"Name":addname, "Salary (in LPA)":addsal}

def displayall():
    for department,dept_data in Employee.items():
        print(department)
        for emp_id,info in dept_data.items():
            print({emp_id})
            Name=info["Name"]
            Salary=info["Salary (in LPA)"]
            print("Name:",Name)
            print("Salary (In LPA)",Salary)

            
    


displayall()

            

    
