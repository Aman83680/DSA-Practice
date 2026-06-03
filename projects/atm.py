#atm simulation
b=10000
pin='aman1234'
print("1.Check your Balance.")
print("2.Do You want to Deposit ?")
print("3.Do you want to withdrawl?")
print("4.Change PIN")
print("5.Exit")
n=int(input())
if n==1:
    print("Your current balance: ₹",b)
elif n==2:
    print("Deposit Your Cash:")   
    f=int(input())    
    c=f+b
    print("Your New balance: ₹",c)
elif n==3:
    def login_required(func):
        def inner():
            password = input("Enter ATM PIN: ")
            if password == "aman123":
                func()
            else:
                print("Access Denied")
        return inner    
    @login_required
    def profile():
        print("Enter the amount you want to withdrawl :")
        global b
        w = int(input("Enter amount to withdraw: "))
        if w <= b:
            b = b - w
            print("Please collect your cash")
            print("Available balance: ₹", b)
        else:
            print("Insufficient Balance")
    profile()
elif n == 4:
    old_pin = input("Enter old PIN: ")
    if old_pin == pin:
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin:
            pin = new_pin
            print("PIN changed successfully")
        else:
            print("PIN does not match")
    else:
        print("Wrong old PIN")
elif n==5:
    print("Exit")
    print("Thank You for Visitig us.")
    print("You Dont make any Choice.")
else:
    print("Invalid Choice")












   




