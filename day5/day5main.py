# # # print("Welcome to the square finder of any number")
# # # num=int(input("Enter the number of which you want to find the square"))
# # # #square function
# # # def square(num):
# # #     square=num*num
# # #     return square

# # # sq=square(num)
# # # print( sq)

# # #now it's taking marks from the user and appending into list

# # print("Hello,Welcome to the program which appends ur marks into list")
# # count=int(input("how many subjects do u have??"))
# # def appendmks(count):
# #     markslist=[]
# #     for i in range(count):
# #         mks = int(input(f"Enter marks for subject {i+1}: "))
# #         markslist.append(mks)
# #     return markslist

# # finallist=appendmks(count)
# # print("Here is your list of marks of sub")
# # print(finallist)


# # def summarks(finallist):
# #     sum=0
# #     for i in finallist:
# #         sum=sum+i
# #     return sum
# # sumall=summarks(finallist)

# # sumcon=input("Do you also want to know sum of it??")
# # if(sumcon.lower()=="yes"):
# #     print (sumall)


# # Topper Finder

# print("Hello, Welcome to the program which finds the Topper from given students")

# count = int(input("How many students do you have? "))

# nmlist = []

# def listcreate(count):
#     markslist = []
#     for i in range(count):
#         name = input("Enter the name of student: ")
#         nmlist.append(name)

#         mks = int(input(f"Enter marks of {name}: "))
#         markslist.append(mks)

#     return markslist, nmlist


# marks, names = listcreate(count)


# def topper(marks, names):
#     highest = marks[0]
#     topp = names[0]      # initialize topper name

#     for i in range(len(marks)):
#         if marks[i] > highest:
#             highest = marks[i]
#             topp = names[i]

#     return highest, topp


# toppermarks, toppername = topper(marks, names)

# print("\n🏆 Topper Details 🏆")
# print("Name:", toppername)
# print("Marks:", toppermarks)



#Debugg challenge


#given code:-
# def avg(lst):
#     sum = 0
#     for i in lst:
#         sum = sum + lst[i]
#     return sum / len(lst)
# average=avg(lst)




#bug1-List itself not declared
#bug2:- Already it's a list so can use i direcly instead of lst[i]
#bug3:-bad name for the sum variable as the sum is built in ...
#corrected code:-
lst=[10,20,30]
def avg(lst):
 tot = 0
 for i in lst:
  tot = tot + i
 return tot / len(lst)
average=avg(lst)


print(average)