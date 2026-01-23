print("🎓 Welcome to the Grade Average Calculator!")

# Ask user for number of subjects
subno = int(input("Enter the number of subjects: "))

def gradeavg(subno):
    total = 0
    for i in range(subno):
        marks = float(input(f"Enter marks for subject {i+1}: "))
        total += marks  # add marks to total
    average = total / subno
    return average


def grade(average):
    if(average>80):
        print("A Grade!!!")
    elif(average>70):
        print("B Grade")
    elif(average>60):
        print("C Grade")
    else:
        print("D Grade")









# Call the function
avg=gradeavg(subno)
grade(avg)
