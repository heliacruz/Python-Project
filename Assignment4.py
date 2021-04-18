# Enter the price of the House you wish to buy
print("Enter the house price")
price = int(input())

#Enter your Credit Score
print("Enter your Credit Score")
CreditScore = int(input())

# Enter the first name
print("Enter the first name")
first_name = input()

# Enter the last_name
print("Enter the last name")
last_name = input()

fullnames = first_name + "" + last_name

# Enter the email
print("Enter the email address")
email = input()

# Enter the phone number
print("Enter the phone number")
phone = input()

# Enter the mailing address
print("Enter the mailing address")
mailing = input()

# Enter the City
print("Enter the City")
City = input()

# Enter the State
print("Enter the State")
State = input()

# Enter the Zipcode
print("Enter the zipcode")
zipcode = input()


#Qualify for loans with the best interest rates
if CreditScore >= 780 and 850:
    print("Excellent Credit")
    downPayment = float(0.0 * price)
    print("Zero Down Payment: ")

#Usually qualify for loans with the best interest rates
elif CreditScore >= 740 and 779:
    print("Very Good")
    downPayment = float(0.1 * price)
    print("Downpayment: " + str(downPayment))

#May face slightly higher loan Interest rates
elif CreditScore >= 720 and 739:
    print ("Above Average")
    downPayment = float(0.3 * price)
    print("Downpayment: " + str(downPayment))

#May qualify for most loans of higher Interest rates
elif CreditScore >= 680 and 719:
    print ("Average")
    downPayment = float(0.6 * price)
    print("Downpayment: " + str(downPayment))

#May qualify for most loans at significantly higher Interest rates
elif CreditScore >= 620 and 679:
    print ("Below Average")
    downPayment = float(0.18 * price)
    print("Downpayment: " + str(downPayment))

#Usually has some credit issues; will probably
elif CreditScore >= 580 and 619:
    print("Below Average")
    downPayment = float(0.18 * price)
    print("Downpayment: " + str(downPayment))

# Usually has some credit issues; will probably not 
elif CreditScore >= 580 and 619:
    print ("Poor Credit Score")
    downPayment = float(0.2 * price)
    print("Downpayment: " + str(downPayment))

#Facing extreme credit issue
elif CreditScore < 520:
    print ("Poor Credit Score")
    downPayment = float(0.25 * price)
    print("Downpayment: " + str(downPayment))
else:
    print("invalid output")

print("First name is : " + fullnames)
print("Physical address: " + mailing)
print("City : " + City)
print("State : " + State)
print("Zipcode : " + zipcode)