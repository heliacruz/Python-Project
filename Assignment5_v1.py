#Declaring the variables
options = ""

#Display the options
while options != "Q":

    # Ask user for the options
    options = input("Enter the options [P, C, F, M, KM, In, CM,Q]?")
    print()

    if options == "P":
        print("[P]Print Options")
        print("[C]Convert from Celcius to Fahrenheit")
        print("[F]Convert from Fahrenheit to Celcius")
        print("[M]Convert from Miles to Kilometers")
        print("[KM]Convert from Kilometers to Miles")
        print("[In]Convert from Inches to Centimeters")
        print("[CM]Convert from Centimeters to Inches")
        print("[Q]Quit")
        print()
            
    elif options == "C":

        # Convert from Celcius to Fahrenheit
        celsius = int(input("Celsius temperature: "))
        temp = (celsius * 1.8) + 32
        print("Fahrenheit:" + str(temp))
        print()

    elif options == "F":

        #Convert from Fahrenheit to Celcius
        fahrenheit = int(input("fahrenheit temperature: "))
        temp = (fahrenheit - 32) * 0.5556
        print("Celsius:" + str(temp))
        print()
        
    elif options == "M":
        #Convert from Mile to Kilometers
        miles = float(input("miles: "))
        kilometer = miles * 1.609344
        print("Kilometers: " + str(kilometer))
        print()

    elif options == "KM":
        #Convert from Kilometers to Mile
        kilometers = float(input("kilometers: "))
        miles = (kilometers / 1.609)
        print("Miles: " + str(miles))
        print()


    elif options == "In":
        #Convert from Inches to Centimeters
        inches = float(input("inches: "))
        centimeters = (inches * 2.54)
        print("Centimeters: " + str(centimeters))
        print()
        
    elif options == "CM":
        #Convert from Centimeters to Inches
        centimeters = float(input("centimeters: "))
        inches = centimeters / 2.54
        print("Inches: " + str(inches))
        print()

    else:
        print("Invalid input!!!")
        print()
