import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user to specify the desired length of the password

def password_generator():
   
   try:
       length = int(input("Enter the desired length of the password: "))

       if length <= 0:
            print("Invalid input! Please enter a positive number.")
            password_generator()

       else:
             # Generate and display the password
            password = generate_password(length)
            print("Generated Password: ", password,"\n want to create another password?")
            y_or_N=input("Enter Y or N = ")
            if y_or_N=='Y':
                password_generator()
            elif  y_or_N=='N':
                print("stopped")
            else:
                print("Error")
   
   except ValueError:
    print("Invalid input! Please enter a valid number for the password length.")
    password_generator()


password_generator()