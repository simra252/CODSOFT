def calculator():
   # Prompt the user for input
   print("\nCodeSoft task# Simple Calculator")
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))

   print("Select operation:")
   print("+\t-\t*\t/")

   # Prompt the user to choose an operation
   choice = input("Enter choice (+, -, *, or /): ")

   # Perform the calculation and display the result
   if choice == '+':
       print(num1,choice,num2,end=" = ")
       print(num1 + num2)
       print("perform more calculations")
       calculator()
   elif choice == '-':
       print(num1,choice,num2,end=" = ")
       print(num1 - num2)
       print("perform more calculations")
       calculator()
   elif choice == '*':
        print(num1,choice,num2,end=" = ")
        print(num1 * num2)
        print("perform more calculations")
        calculator()
   elif choice == '/':
        if num2 == 0:
           print("Error! Division by zero.\nplease provide valid input")
           calculator()
        else:
           print(num1,choice,num2,end=" = ")
           print( num1 / num2)
           print("perform more calculations")
           calculator()
   else:
        print("Invalid input! Please enter a valid choice (+, -, *, or /).")
        calculator()

calculator()
