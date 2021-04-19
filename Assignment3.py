# Enter full names
print('Enter your first and last name: ')
fname=input('fname') #First Name
lname=input('lname') #Last Name
fullnames=fname+"" +lname
print(fullnames)
print()
 # Enter phone, email
print('Enter the customer\'s Phone Number: ')
phone=input('phone') #Phone Number
print('Enter the customer\'s Email Address: ')
email=input('email') #Email Address
print() 
# Price of a used car
price=10000
has_good_credit=True
if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"Down Payment:{down_payment}")
print()
print('Full Names: ',fullnames)
print('Phone: ',phone)
print('Email: ',email)
print('Down Payment: ',down_payment)
    