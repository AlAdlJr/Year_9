# Calculator Ismail.AlAdl

# Input name
name = input("Please input your name ")
print("Hello" , name)

# Setting the While loop variable

choice = 0

# while loop
while choice !=2:
    # Input Operation
    operation = input("What opperation would you like to do? (+,-,*,/) ")

    # Input the numbers
    num1 = int(input("Input your first number "))
    num2 = int(input("Input your second number "))

    # Addition Operation
    if operation == ("+"):
        print(str(num1) , " + ", str(num2)," = " , num1 + num2)

    # Substation Operation    
    elif operation == ("-"):
        print(str(num1) , " - ", str(num2)," = " , num1 - num2)

    #Multiplication Operation
    elif operation == ("*"):
        print(str(num1) , " * ", str(num2)," = " , num1 * num2)

    #Division Operation
    else:
        print(str(num1) , " / ", str(num2)," = " , num1 / num2)
    
    #Repeat or exit choice
    choice=int(input("Press 1 to solve another cualation or press 2 to Exit "))

#Exit program
print("See you soon")