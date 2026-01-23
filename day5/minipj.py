accname=["A","B","C"]
pin=[1234,5678,8763]
bal=5000

print("Welcome to the Banking System!!")
name=input("Enter your name")





def withdraw(balance):
 amt=int(input("Enter the amount which you want to withdraw"))
 bal=bal-amt
 print("The balance remaining is"+bal)



for i in accname:
    if(i==name):
        askpin=int(input("Ente the PIN"))
        if(askpin==pin[i]):
                op=int(input("Press: 1 for withdraw,2 for deposit ,3 to check balance "))
                if(op==1):
                    finalbal=withdraw(bal)
                     






#will continue on day 6

                     




