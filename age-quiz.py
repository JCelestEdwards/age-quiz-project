
#write a code to get a user's name and stoare input as age.
#if user is over 40 print "You're over the hill!"
#maximum age is 100, if user enters more than 100 print Sorry, you're dead.
#if user if 65 or over, print Enjoy your retirement!
#if user is under 13, print you qualify for the kiddies discount 
#if user is 21, print congrats on your 21st!
#for any other age print Age is just a number

user_age = input("Hello User! Can you please tell me your age? ")
age = int(user_age)

if age < 13:
    print("You qualify for the kiddies discount.")
elif age == 21:
    print("Congrats on your 21st!")
elif age >=40 and age < 65 and age != 65:
    print(" You're over the hill!")
elif age >= 65 and age <= 100:
    print("Enjoy your retirement!")
elif age > 100:
    print("Sorry, you're dead.")
else: 
    print("Age is but a number.")
print(age)


