import math #get access to math.pi


print("")
print("How many digits would you like to round off pi by?")
print("Please note: You value can't be larger than 10")

round_n = input()
int_n = int(round_n)

while int_n < 0 or int_n > 10:
    print("")
    print("Invalid input.")
    print("Please enter a number between 1 and 10.")

    round_n = input()
    int_n = int(round_n)
else:
    print("")
    print(f"You have chosen to round pi to the {int_n}th decimal place.")
    pi_rounded = round(math.pi, int_n)
    print(pi_rounded)










