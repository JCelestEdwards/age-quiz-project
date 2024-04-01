
#write a code to get a user's name and stoare input as age.
#if user is over 40 print "You're over the hill!"
#maximum age is 100, if user enters more than 100 print Sorry, you're dead.
#if user if 65 or over, print Enjoy your retirement!
#if user is under 13, print you qualify for the kiddies discount 
#if user is 21, print congrats on your 21st!
#for any other age print Age is just a number

def check_age(age):
    """
    Checks the age of the user and prints a corresponding message.

    Parameters:
    - age (int): The age of the user.

    Returns:
    - None
    """
    if age < 13:
        print("You qualify for the kiddies discount.")  # If the age is less than 13
    elif age == 21:
        print("Congrats on your 21st!")  # If the age is exactly 21
    elif age >= 40 and age < 65 and age != 65:
        print("You're over the hill!")  # If the age is between 40 and 64 (inclusive), excluding 65
    elif age >= 65 and age <= 100:
        print("Enjoy your retirement!")  # If the age is between 65 and 100 (inclusive)
    elif age > 100:
        print("Sorry, you're dead.")  # If the age is greater than 100
    else: 
        print("Age is but a number.")  # For all other cases (default)

# Prompt the user to input their age
user_age = input("Hello User! Can you please tell me your age? ")

# Convert the user's input to an integer
age = int(user_age)

# Call the function to check the user's age
check_age(age)