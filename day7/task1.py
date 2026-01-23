#enumerated list(when u have list and you want index as well as the value from it without using the len function)and it stores 
#in the form of turples
nums=[10,20,30,40,50,60,70,80,90]
highest=nums[0]
index=0
for i,value in enumerate(nums):
    if(highest<value):
        highest=value
        index=i
print(index,highest)


