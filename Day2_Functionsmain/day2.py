print("🔐 Welcome to the Research Facility 🔐")

name = input("May I know your name, sir? ")
ccode = 2468
print("Greetings,", name)
count=0
age = int(input("Please enter your age: "))
for i in range(3):

 seccode = int(input("Enter the security code: "))

 if age >= 18 and seccode == ccode:
    print(f"Access granted. Welcome, {name}!")
    break
 elif age >= 18 and seccode != ccode:
    print("Security code mismatch. Access denied.")
    count+=1
    
 else:
    print("Access denied. Age restriction.")
 
if(count>=3):
 print("System locked. Contact Admin.")