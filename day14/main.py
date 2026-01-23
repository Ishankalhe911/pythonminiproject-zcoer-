# dict={
#     "name":"Ishan",
#     "grade":[87.5,98.2,54.5,78,67],
#     "cgpa":"8.5"



# }


# #trying to access the 3rd marks from the grade list
# #list element from a dictionary
# # print(dict["grade"][2])
# dict["grade"][2]=85
# print(dict)


#store in dictionary these random values
#table:"a piece of furniture","list of facts & figures"
#cat: "a small animal"

# dict={}

# dict["table"]=["a piece of furniture ","list of facts & figures"]
# dict["cat"]=["a small animal"]


# print(dict)

# seta={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(seta))



#a dynamic student marks storing system with help of set
# dict={}

# print("Enter marks of student for storing the marks of the student")
# studentname=input("Enter your name ")
# no_sub=int(input("Enter the Number of subject "))
# sub_list=[]
# for i in range(no_sub):
#     sub_inp=input("Enter the marks of the subject")
#     sub_list.append(sub_inp)

# dict[studentname]=sub_list
# print(dict)
#-------------------------------------------------------------------------------
#u have given a problem where u were to store 9,9.0 in a set(uniquely)

seta={9,(9.0,)}
print(seta)
#so as 9,9.0 will have same hash code in python to store in set u have to store 9.0 in a tuple and for that "," is required after the value
