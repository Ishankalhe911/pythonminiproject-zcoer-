print("Hello,Welcome to the Average,Min,Max from the student data set")
print("Enter the details of each student one by one and fill the details")
count=int(input("Enter total number of students in your dataset"))

#create list
mkslist=[]
nmlist=[]
for i in range(count):

 name=input("Enter the name of student")
 marks=int(input("Enter the total marks of that student"))
 mkslist.append(marks)
 nmlist.append(name)




def find_max(mkslist, nmlist):
    mx = mkslist[0]
    nm = nmlist[0]
    for i in range(len(mkslist)):  # use len(), not count
        if mkslist[i] > mx:
            mx = mkslist[i]
            nm = nmlist[i]
    return mx, nm


def find_min(mkslist, nmlist):
    mn = mkslist[0]
    nm = nmlist[0]
    for i in range(len(mkslist)):
        if mkslist[i] < mn:
            mn = mkslist[i]
            nm = nmlist[i]
    return mn, nm




def avg(mkslist,count):
 sum=0
 
 for i in range(count):
 
  sum=sum+mkslist[i]
 avg=sum/count
 return avg


optionbr=int(input("Give me what you want in this data-set 1 for avg,2 for max,3 for min"))

if optionbr == 1:
    print("Average Marks:", avg(mkslist, count))
elif optionbr == 2:
    maxmarks, maxname = find_max(mkslist, nmlist)
    print(f"Highest Marks: {maxmarks} by {maxname}")
elif optionbr == 3:
    minmarks, minname = find_min(mkslist, nmlist)
    print(f"Lowest Marks: {minmarks} by {minname}")
else:
    print("Invalid Option!")














