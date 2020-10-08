
print(14%10)

num = 4
round_check = num % 10

if round_check >= 5:
    roundedup_num = 10 - round_check
    revised_value = num + roundedup_num
    print(revised_value)



else:
    roundeddown_num = num - round_check
    revised_value = num - roundeddown_num
    print(roundeddown_num)


