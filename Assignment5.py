#Declaring  a variable

options = ' '

#Display the options

while options != "Q":

   if options == "P":

     print("[P]Print Options")
     print("[C]Convert from Celsius")
     print("[F]Convert from Fahrenheit")
     print("[M]Convert from Miles")
     print("[KM]Convert from Kilometers")
     print("[In]Convert from Inches")
     print("[CM]Convert from Centimeters")
     print("[Q]Quit")

     print()
     # Ask user for options

     options = input("Enter the options [P, C, F, M, KM, IN, CM, Q]? ")

   elif options == "C":
    # Convert from Celsius to fahrenheit
    Celsius = int(input("Celsius temperature: "))  
    temp = (Celsius * 1.8) + 32
    print("Fahrenheit:" + str(temp))
    print()
     
     
   elif options == "C":
    # Convert from Celsius to fahrenheit
    Celsius = int(input("Celsius temperature: "))  
    temp = (Celsius * 1.8) + 32
    print('Fahrenheit:' + str(temp))
    print()