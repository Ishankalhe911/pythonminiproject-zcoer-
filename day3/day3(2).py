#list version
print("Welcome to the Student Grader using LIST")
name=input("Tell me your name")
subcount=int(input("Tell me how many subjects do u have in total??"))

def listcreate(subcount):
    mkslist=[]
 
    for i in range (subcount):
     marks=int(input("Tell me the marks of the subject"))
     mkslist.append(marks) 
    return mkslist

marklist=listcreate(subcount)
print(f"{name}'s marks list: ", marklist)



def avg(marklist):
   totalmks=0
   for i in range(subcount):
      totalmks=totalmks+marklist[i]
   avg=totalmks/subcount
   return avg
average_marks=avg(marklist)
print(average_marks)

 
 
 
 



