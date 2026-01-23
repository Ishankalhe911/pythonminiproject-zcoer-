# #looping practice first

# print("Welcome to Even no printer from list")
# count=int(input("Enter number of you want to add as elements in the list"))
# numlist=[]
# for i in range(count):
#     number=int(input("Enter the the number you wanna add"))
#     numlist.append(number)
# print(numlist)




# def evenno(numlist):
#     evennumlist=[]
#     for i in (numlist):
#         if(i%2==0):
#             evennumlist.append(i)
#     return evennumlist
        
# evennums=evenno(numlist)
# print(evennums)



#max without max function
names=["A","B","C"]
marks=[65,58,89]
highest=marks[0]
i=0
for i in range(len(marks)):
    if(highest<marks[i]):
        highest=marks[i]
    ind=i
print(highest)
print(names[ind])
