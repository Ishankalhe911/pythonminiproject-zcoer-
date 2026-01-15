# print("Welcome to List Palindrome Checker")
# count=int(input(("Firstly tell me how many elements you wanna keep in your list")))
# list=[]
# for i in range(count):
#     el=int(input("Tell me the element you wanna add in the list"))
#     list.append(el)
# print(list)
# start=0
# end=len(list)-1
# is_palindrome=True

# while start<end:
#     if list[start]!=list[end]:
#         is_palindrome=False
#         break
#     start+=1
#     end-=1

# if is_palindrome:
#     print("It's a Pallindrome")
# else:
#     print("It's not a Pallindrome")


#The second task is to count the number of each element without using dictionary

print("Welcome to List Frequency Checker")
count = int(input("Firstly tell me how many elements you wanna keep in your list: "))
data = []
for i in range(count):
    el = int(input("Tell me the element you wanna add in the list: "))
    data.append(el)
print(data)

numb = []  # Track unique elements found
for i in range(count):
    num = data[i]
    skipcnt = 0
    
    # Check if already counted
    for k in range(len(numb)):
        if num == numb[k]:
            skipcnt = 1
            break  # Added break for efficiency
    
    if skipcnt == 0:
        freq = 0
        for j in range(count):
            if data[j] == num:
                freq += 1
        
        numb.append(num)  # Append only once after counting
        print("Frequency of element", num, "is", freq)
