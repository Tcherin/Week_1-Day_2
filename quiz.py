my_number = 7

user_value = int (input("please guess a number: "))

while user_value != my_number:
    if user_value < my_number:
        print("That's too low!")
    if user_value > my_number:
        print("That's too high!")

user_value = int(input("Sorry, try again!"))

print("You got it!")