University = {
    "Computer Science": {
        "CS101": "Intro to Python",
        "CS102": "Data Structures"
    },
    "Mathematics": {
        "MTH101": "Calculus",
        "MTH102": "Linear Algebra"
    },
    "Physics": {
        "PHY101": "Quantum Mechanics"
    }
}




def display():
    for department ,department_data in University.items():
        print (f"{department}")
        for subject,subject_data in department_data.items():
            print(f"{subject}:{subject_data}")



def add_data():
    depart=input("Enter the Department where you want to add the subject for Computer Science (cs),for Mathematics(M),Physics(Ph) ")

    sub_code=input("Enter the code of the subject you want to set")
    sub_name=input("Enter the Name of Subject")
    if(depart=="Cs"):
        University["Computer Science"][sub_code]=sub_name
    elif(depart=="M"):
        University["Mathematics"][sub_code]=sub_name
    elif(depart=="Ph"):
        University["Physics"][sub_code]=sub_name
    
    for department ,department_data in University.items():
        print (f"{department}")
        for subject,subject_data in department_data.items():
            print(f"{subject}:{subject_data}")

    
def delete_data():
    depart=input("Enter the Department where you want to add the subject  Computer Science, Mathematics,Physics (type exactly as named) ")
    sub_code=input("Enter the code of the subject you want to delete")
    


    del University[depart][sub_code]
    print("Subject with subject code ",sub_code,"is deleted Successfully!!")


 











def search_data():
    sub_code=input("Enter the code of the subject you want to search")
    for depart,department_data in University.items():
        if sub_code in department_data:
            sub_name=department_data[sub_code]
            
            print(f"Subject found in {depart} & has subject name",sub_name)
            break
    else:
        print("Subject not found!! ")

search_data()
    