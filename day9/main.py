# # # even numbers sum 
# # # print("Welcome to the even number printer from ur given list")
# # # list=[]
# # # count=int(input("Enter the nunbers you have in your list"))

# # # for i in range(count):
# # #     inlist=int(input("Enter the element you wanna add in the list"))
# # #     list.append(inlist)



# # # evensum=0
# # # for i in list:
# # #     if (i)%2==0:
# # #         evensum=evensum+i



# # # print("Sum of even numbers from your given list is",evensum)







# # #countvowels from string
# # print("Welcome to Vowel count from any string ")
# # str_inp=input("Enter the string you wanna search")



# # def vowelcount():
# #     count=0
# #     for i in (str_inp):
# #         if i=="a" or i=="e" or i=="i"or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
# #             count=count+1
# #     return count
        
# # vowelcount=vowelcount()


# # print(vowelcount)







# #find the second largest number in the list without using builtin loop
# print("Welcome to the second largest element finder from the list")



# list=[]


# count=int(input("Enter the count of your list"))
 
# for i in range(count):
#     inp=int(input("Enter the number you want to add"))
#     list.append(inp)



# max1=list[0]
# for i in (list):
#     if i>max1:
#         max1=i
# list.remove(max1)
# max2=list[0]
# for i in list:
#     if i>max2:
#         max2=i
# print (max2)
count=int(input("Enter the count of your list"))
list=[]
 
for i in range(count):
    inp=int(input("Enter the number you want to add"))
    list.append(inp)
temp=0
start=0
end=len(list)-1
while start<end:
    list[start],list[end] = list[end],list[start]        
    start+=1
    end-=1



print(list)



