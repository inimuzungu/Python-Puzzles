
lst_notprime = [0, 1]
lst_prime = [2, 5]
lst_div = [2, 3, 5, 7, 11]


#input number

print("Please input a number")
user_input = int(input())

#test user input
if user_input % 2 != 0 or user_input % 3 != 0 or user_input % 5 != 0 or user_input % 7 != 0 or user_input % 11 != 0:
    print("Prime Number")
elif user_input % 2 == 0 or user_input % 3 == 0 or user_input % 5 == 0 or user_input % 7 == 0 or user_input % 11 == 0:
    print("Composite Number")
else:
    print("Neither a Prime nor Composite Number.")

#if user_input = 2 or 5: print "Prime"

#if user_input divided by lst_div != 0: print "Prime" else print "Composite"





"""
if user_input == 2 or user_input == 5 or user_input == 0 or user_input == 1:
    print(f"The number {user_input} is NOT a prime number.")
elif user_input % 2 == 0:
    print(f"The number {user_input} is NOT a prime number.")
"""

