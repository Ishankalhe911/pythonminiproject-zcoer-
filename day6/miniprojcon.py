#so first of all we will declare names and balance
names=["A","B","C"]
pin=[]
balance=[5000,8000,10000]
print("Welcome to banking application")


namein=input("Enter your name")


#functions declarations
def withdrawl(index,balance):
    amt=int(input("enter the amt you wanna withdraw"))
    finalamt=(balance[index])-amt
    (balance[index])=finalamt
    return finalamt



def deposit(index,balance):
    amt=int(input("enter the amt you wanna withdraw"))
    finalamt=(balance[index])+amt
    balance[index] = finalamt

    return finalamt


def checkbal(index,balance):
    finalamt=(balance[index])
    return finalamt















for i in range(len(names)):
    if(namein==names[i]):
        index=i
while True:
    choice=int(input("Okay,Now tell me which operation do you wanna perform 1 for withdrawl,2 for deposit 3 for balance and press 4 to exit "))
    if(choice==1):
        result=withdrawl(index,balance)
        print(result)
    elif choice==2:
        result=deposit(index,balance)
        print(result)

    elif choice==3:
        result=checkbal(index,balance)
        print(result)
    elif choice==4:
        print("Thank you for banking")
        break
    else:
        print("Invalid Choice")



